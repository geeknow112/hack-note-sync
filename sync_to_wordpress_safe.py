#!/usr/bin/env python3
"""
安全な同期システム - 事前確認・差分検出・品質チェック付き
"""

import os
import json
import hashlib
import requests
import base64
import re
from datetime import datetime

class SafeWordPressSyncer:
    def __init__(self, config_file='config.yaml'):
        import yaml
        with open(config_file, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        
        self.wp_url = self.config['wordpress']['url']
        self.wp_user = self.config['wordpress']['username']
        self.wp_pass = self.config['wordpress']['password']
        
        credentials = f"{self.wp_user}:{self.wp_pass}"
        token = base64.b64encode(credentials.encode()).decode()
        self.headers = {
            'Authorization': f'Basic {token}',
            'Content-Type': 'application/json'
        }
        
        self.sync_log = 'sync_log.json'
        self.articles_dir = 'articles'
    
    def is_valid_article(self, filepath, content):
        """記事として有効かチェック"""
        filename = os.path.basename(filepath)
        
        # 1. Markdownファイルのみ
        if not filename.endswith('.md'):
            return False, "Markdownファイルではありません"
        
        # 2. 最小文字数チェック（500文字以上）
        if len(content) < 500:
            return False, f"文字数不足: {len(content)}文字（最小500文字）"
        
        # 3. タイトル存在チェック
        if not content.startswith('#'):
            return False, "タイトル（# 見出し）がありません"
        
        # 4. 除外ファイル
        exclude_patterns = [
            'README.md',
            'test_',
            'sample_',
            '_temp',
            'draft_'
        ]
        
        for pattern in exclude_patterns:
            if pattern in filename:
                return False, f"除外パターン: {pattern}"
        
        return True, "OK"
    
    def get_pending_articles(self):
        """投稿予定の記事を取得"""
        log_data = self.load_sync_log()
        pending = []
        
        for filename in os.listdir(self.articles_dir):
            filepath = os.path.join(self.articles_dir, filename)
            
            if not os.path.isfile(filepath):
                continue
            
            # ファイルハッシュ計算
            current_hash = self.get_file_hash(filepath)
            
            # 同期済みかチェック
            if filename in log_data:
                if log_data[filename]['hash'] == current_hash:
                    continue  # 変更なし
                else:
                    action = "更新"
            else:
                action = "新規"
            
            # 記事として有効かチェック
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            is_valid, reason = self.is_valid_article(filepath, content)
            
            pending.append({
                'filename': filename,
                'filepath': filepath,
                'action': action,
                'valid': is_valid,
                'reason': reason,
                'size': len(content)
            })
        
        return pending
    
    def preview_sync(self):
        """同期プレビュー"""
        pending = self.get_pending_articles()
        
        valid_articles = [p for p in pending if p['valid']]
        invalid_articles = [p for p in pending if not p['valid']]
        
        print("📋 同期プレビュー")
        print("=" * 50)
        
        if valid_articles:
            print(f"✅ 投稿予定: {len(valid_articles)}件")
            for article in valid_articles:
                print(f"  • {article['action']}: {article['filename']} ({article['size']}文字)")
        
        if invalid_articles:
            print(f"\n❌ 除外: {len(invalid_articles)}件")
            for article in invalid_articles:
                print(f"  • {article['filename']}: {article['reason']}")
        
        if not valid_articles:
            print("📝 投稿する記事がありません")
            return False
        
        return valid_articles
    
    def confirm_sync(self, articles):
        """同期確認"""
        print(f"\n🚨 {len(articles)}件の記事を投稿します。よろしいですか？")
        print("⚠️  この操作は取り消せません。")
        
        while True:
            response = input("続行しますか？ (yes/no): ").lower().strip()
            if response in ['yes', 'y']:
                return True
            elif response in ['no', 'n']:
                return False
            else:
                print("yes または no で答えてください")
    
    def get_file_hash(self, filepath):
        """ファイルハッシュ計算"""
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    
    def load_sync_log(self):
        """同期ログ読み込み"""
        if os.path.exists(self.sync_log):
            with open(self.sync_log, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_sync_log(self, log_data):
        """同期ログ保存"""
        with open(self.sync_log, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, ensure_ascii=False, indent=2)
    
    def post_to_wordpress(self, article_data):
        """WordPressに記事を下書きとして投稿（アイキャッチ画像付き）"""
        # カテゴリーID取得
        category_id = self.get_category_id(article_data['category'])
        
        post_data = {
            'title': article_data['title'],
            'slug': article_data['slug'],
            'content': article_data['content'],
            'status': 'draft',  # 非公開（下書き）で投稿
            'categories': [category_id],
            'meta': {
                'description': article_data['description']
            }
        }
        
        response = requests.post(
            f"{self.wp_url}/wp-json/wp/v2/posts",
            headers=self.headers,
            json=post_data
        )
        
        # 投稿成功時にアイキャッチ画像を設定
        if response.status_code == 201:
            post_id = response.json()['id']
            self.set_featured_image(post_id, article_data['title'])
        
        return response
    
    def set_featured_image(self, post_id, title):
        """投稿にアイキャッチ画像を自動生成・設定"""
        from utils.image_generator import ImageGenerator
        
        try:
            image_gen = ImageGenerator(self.wp_url, self.wp_user, self.wp_pass)
            success = image_gen.generate_featured_image(post_id, title)
            
            if success:
                print(f"🎨 アイキャッチ画像設定完了")
            else:
                print(f"⚠️ アイキャッチ画像設定に失敗")
                
        except Exception as e:
            print(f"❌ アイキャッチ画像エラー: {str(e)}")
    
    def get_category_id(self, category_name):
        """カテゴリー名からIDを取得（存在しない場合は作成）"""
        # カテゴリー一覧取得
        response = requests.get(
            f"{self.wp_url}/wp-json/wp/v2/categories",
            headers=self.headers,
            params={'search': category_name}
        )
        
        if response.status_code == 200:
            categories = response.json()
            for cat in categories:
                if cat['name'] == category_name:
                    return cat['id']
        
        # カテゴリーが存在しない場合は作成
        create_response = requests.post(
            f"{self.wp_url}/wp-json/wp/v2/categories",
            headers=self.headers,
            json={'name': category_name}
        )
        
        if create_response.status_code == 201:
            return create_response.json()['id']
        
        return 1  # デフォルトカテゴリー

    def safe_sync(self):
        """安全な同期実行"""
        print("🔍 記事をスキャン中...")
        
        # プレビュー
        articles = self.preview_sync()
        if not articles:
            return
        
        # 確認
        if not self.confirm_sync(articles):
            print("❌ 同期をキャンセルしました")
            return
        
        print("\n🚀 同期開始...")
        
        # 実際の投稿処理
        success_count = 0
        for article in articles:
            print(f"\n📝 投稿中: {article['filename']}")
            
            # Markdownを解析
            with open(article['filepath'], 'r', encoding='utf-8') as f:
                content = f.read()
            
            article_data = self.parse_markdown(article['filepath'], content)
            
            # WordPress投稿
            response = self.post_to_wordpress(article_data)
            
            if response.status_code == 201:
                result = response.json()
                print(f"✅ 下書き投稿成功: {result['link']}")
                success_count += 1
                
                # ログ更新
                log_data = self.load_sync_log()
                log_data[article['filename']] = {
                    'post_id': result['id'],
                    'hash': self.get_file_hash(article['filepath']),
                    'created_at': datetime.now().isoformat(),
                    'title': article_data['title'],
                    'status': 'draft'
                }
                self.save_sync_log(log_data)
            else:
                print(f"❌ 投稿失敗: {response.text}")
        
        print(f"\n🎉 同期完了: {success_count}/{len(articles)}件成功")
        print("📋 全て下書きとして投稿されました。管理画面で確認・公開してください。")
    
    def parse_markdown(self, filepath, content):
        """Markdownファイルを解析してメタデータを抽出"""
        filename = os.path.basename(filepath)
        
        # タイトル抽出（最初のH1見出し）
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
        else:
            title = filename.replace('.md', '').replace('_', ' ').replace('-', ' ').title()
        
        # カテゴリー推定
        category = self.estimate_category(filename)
        
        # 英語スラッグ生成
        slug = self.generate_english_slug(filename, title)
        
        # メタディスクリプション生成
        description = self.generate_description(content)
        
        # MarkdownをHTMLに変換
        html_content = self.markdown_to_html(content)
        
        return {
            'title': title,
            'content': html_content,
            'category': category,
            'description': description,
            'slug': slug,
            'filename': filename
        }
    
    def estimate_category(self, filename):
        """ファイル名からカテゴリーを推定"""
        category_patterns = {
            'AWS': ['aws-', 'lambda-', 'ec2-', 's3-'],
            'Python': ['python-', 'django-', 'flask-'],
            'Docker': ['docker-', 'container-'],
            'GitHub': ['github-', 'git-'],
            'JavaScript': ['js-', 'javascript-', 'node-'],
            'WordPress': ['wordpress-', 'wp-'],
            'TradingView': ['tradingview-', 'trading-'],
            'AI・機械学習': ['ai-', 'ml-', 'deep-learning-'],
            'インフラ': ['infra-', 'server-', 'nginx-', 'apache-']
        }
        
        filename_lower = filename.lower()
        
        for category, patterns in category_patterns.items():
            for pattern in patterns:
                if filename_lower.startswith(pattern):
                    return category
        
        return 'その他'
    
    def generate_english_slug(self, filename, title):
        """ファイル名とタイトルから英語スラッグを生成"""
        base_slug = filename.replace('.md', '').replace('_', '-')
        slug = re.sub(r'[^a-zA-Z0-9\-]', '', base_slug)
        slug = re.sub(r'-+', '-', slug).strip('-')
        
        if not slug:
            english_parts = re.findall(r'[a-zA-Z]+', title)
            if english_parts:
                slug = '-'.join(english_parts).lower()
            else:
                slug = 'article'
        
        return slug.lower()
    
    def generate_description(self, content):
        """コンテンツからメタディスクリプションを生成"""
        paragraphs = content.split('\n\n')
        for paragraph in paragraphs:
            if not paragraph.startswith('#') and not paragraph.startswith('```'):
                clean_text = re.sub(r'<[^>]+>', '', paragraph)
                clean_text = clean_text.replace('\n', ' ').strip()
                if len(clean_text) > 50:
                    if len(clean_text) > 160:
                        clean_text = clean_text[:157] + '...'
                    return clean_text
        
        return "企業の業務効率化に役立つ技術情報をお届けします。"
    
    def markdown_to_html(self, markdown_text):
        """基本的なMarkdown記法をHTMLに変換"""
        html = markdown_text
        
        # 見出し変換
        html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
        html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
        html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
        html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
        
        # コードブロック変換
        html = re.sub(r'```(\w+)?\n(.*?)\n```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
        
        # インラインコード変換
        html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
        
        # 太字変換
        html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
        
        # リスト変換
        lines = html.split('\n')
        in_list = False
        result_lines = []
        
        for line in lines:
            if re.match(r'^- ', line):
                if not in_list:
                    result_lines.append('<ul>')
                    in_list = True
                item = re.sub(r'^- (.+)', r'<li>\1</li>', line)
                result_lines.append(item)
            else:
                if in_list:
                    result_lines.append('</ul>')
                    in_list = False
                result_lines.append(line)
        
        if in_list:
            result_lines.append('</ul>')
        
        # 段落変換
        html = '\n'.join(result_lines)
        paragraphs = html.split('\n\n')
        html_paragraphs = []
        
        for p in paragraphs:
            p = p.strip()
            if p and not p.startswith('<'):
                p = f'<p>{p}</p>'
            html_paragraphs.append(p)
        
        return '\n\n'.join(html_paragraphs)

if __name__ == "__main__":
    syncer = SafeWordPressSyncer()
    syncer.safe_sync()
