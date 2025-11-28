#!/usr/bin/env python3
"""
GitHub to WordPress Auto Sync System
GitHubリポジトリの記事をWordPressに自動同期するシステム
"""

import os
import requests
import base64
import json
import yaml
from datetime import datetime
import hashlib
import re

class WordPressSyncer:
    def __init__(self, config_file='config.yaml'):
        """設定ファイルから初期化"""
        with open(config_file, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        
        self.wp_url = self.config['wordpress']['url']
        self.wp_user = self.config['wordpress']['username']
        self.wp_pass = self.config['wordpress']['password']
        self.articles_dir = self.config['sync']['articles_dir']
        self.sync_log = self.config['sync']['log_file']
        
    def get_auth_header(self):
        """WordPress認証ヘッダーを生成"""
        credentials = f"{self.wp_user}:{self.wp_pass}"
        token = base64.b64encode(credentials.encode()).decode()
        return {'Authorization': f'Basic {token}', 'Content-Type': 'application/json'}
    
    def generate_english_slug(self, filename, title):
        """ファイル名とタイトルから英語スラッグを生成"""
        import re
        
        # ファイル名から基本スラッグを作成
        base_slug = filename.replace('.md', '').replace('_', '-')
        
        # 日本語文字を除去し、英数字とハイフンのみに
        slug = re.sub(r'[^a-zA-Z0-9\-]', '', base_slug)
        
        # 連続するハイフンを単一に
        slug = re.sub(r'-+', '-', slug)
        
        # 前後のハイフンを除去
        slug = slug.strip('-')
        
        # 空の場合はタイトルから生成
        if not slug:
            # タイトルから英語部分を抽出
            english_parts = re.findall(r'[a-zA-Z]+', title)
            if english_parts:
                slug = '-'.join(english_parts).lower()
            else:
                slug = 'article'
        
        return slug.lower()
    
    def parse_markdown(self, filepath):
        """Markdownファイルを解析してメタデータと本文を抽出"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # タイトル抽出（最初のH1）
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else os.path.basename(filepath).replace('.md', '')
        
        # カテゴリー推定（ファイル名から）
        filename = os.path.basename(filepath)
        category = self.guess_category(filename)
        
        # タグ抽出（見出しから）
        tags = self.extract_tags(content)
        
        # メタディスクリプション生成
        description = self.generate_description(content)
        
        # 英語スラッグ生成
        slug = self.generate_english_slug(filename, title)
        
        # MarkdownをHTMLに変換
        html_content = self.markdown_to_html(content)
        
        return {
            'title': title,
            'content': html_content,
            'category': category,
            'tags': tags,
            'description': description,
            'slug': slug,
            'filename': filename
        }
    
    def markdown_to_html(self, markdown_text):
        """基本的なMarkdown記法をHTMLに変換"""
        import re
        
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
    
    def guess_category(self, filename):
        """ファイル名からカテゴリーを推定"""
        category_map = {
            'aws': 'AWS',
            'python': 'Python',
            'docker': 'Docker',
            'github': 'GitHub',
            'wordpress': 'WordPress',
            'django': 'Django',
            'tradingview': 'TradingView',
            'ai': 'AI・機械学習',
            'chatgpt': 'ChatGPT',
            'freee': '会計・税務',
            'tax': '税務',
            'bootstrap': 'フロントエンド',
            'js': 'JavaScript',
            'php': 'PHP',
            'typescript': 'TypeScript',
            'vuejs': 'Vue.js'
        }
        
        for key, category in category_map.items():
            if key in filename.lower():
                return category
        return 'その他'
    
    def extract_tags(self, content):
        """コンテンツから関連タグを抽出"""
        # 見出しからキーワードを抽出
        headings = re.findall(r'^#{2,6} (.+)$', content, re.MULTILINE)
        tags = []
        
        for heading in headings[:5]:  # 最初の5個の見出しから
            # 技術用語を抽出
            tech_words = re.findall(r'\b[A-Z][a-z]+\b|\b[A-Z]{2,}\b', heading)
            tags.extend(tech_words)
        
        return list(set(tags))[:10]  # 重複除去、最大10個
    
    def generate_description(self, content):
        """メタディスクリプションを生成"""
        # 最初の段落を取得
        paragraphs = content.split('\n\n')
        for para in paragraphs:
            if para.strip() and not para.startswith('#'):
                # HTMLタグとMarkdown記法を除去
                clean_text = re.sub(r'[#*`\[\]()]', '', para)
                return clean_text[:150] + '...' if len(clean_text) > 150 else clean_text
        return "企業の業務効率化に役立つ技術情報をお届けします。"
    
    def get_file_hash(self, filepath):
        """ファイルのハッシュ値を計算"""
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    
    def load_sync_log(self):
        """同期ログを読み込み"""
        if os.path.exists(self.sync_log):
            with open(self.sync_log, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_sync_log(self, log_data):
        """同期ログを保存"""
        with open(self.sync_log, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, ensure_ascii=False, indent=2)
    
    def get_category_id(self, category_name):
        """カテゴリー名からIDを取得（存在しない場合は作成）"""
        # カテゴリー一覧取得
        response = requests.get(
            f"{self.wp_url}/wp-json/wp/v2/categories",
            headers=self.get_auth_header()
        )
        
        if response.status_code == 200:
            categories = response.json()
            for cat in categories:
                if cat['name'] == category_name:
                    return cat['id']
        
        # カテゴリーが存在しない場合は作成
        new_category = {
            'name': category_name,
            'slug': category_name.lower().replace(' ', '-')
        }
        
        response = requests.post(
            f"{self.wp_url}/wp-json/wp/v2/categories",
            headers=self.get_auth_header(),
            json=new_category
        )
        
        if response.status_code == 201:
            return response.json()['id']
        return 1  # デフォルトカテゴリー
    
    def post_to_wordpress(self, article_data, update_id=None):
        """WordPressに記事を投稿または更新"""
        category_id = self.get_category_id(article_data['category'])
        
        post_data = {
            'title': article_data['title'],
            'slug': article_data['slug'],
            'content': article_data['content'],
            'status': 'publish',
            'categories': [category_id],
            'tags': article_data['tags'],
            'meta': {
                'description': article_data['description']
            }
        }
        
        if update_id:
            # 更新
            response = requests.post(
                f"{self.wp_url}/wp-json/wp/v2/posts/{update_id}",
                headers=self.get_auth_header(),
                json=post_data
            )
        else:
            # 新規投稿
            response = requests.post(
                f"{self.wp_url}/wp-json/wp/v2/posts",
                headers=self.get_auth_header(),
                json=post_data
            )
        
        return response
    
    def sync_articles(self):
        """記事を同期"""
        sync_log = self.load_sync_log()
        results = {'new': 0, 'updated': 0, 'errors': 0}
        
        for filename in os.listdir(self.articles_dir):
            if not filename.endswith('.md'):
                continue
                
            filepath = os.path.join(self.articles_dir, filename)
            current_hash = self.get_file_hash(filepath)
            
            # ログから前回の同期情報を取得
            file_log = sync_log.get(filename, {})
            last_hash = file_log.get('hash')
            post_id = file_log.get('post_id')
            
            # ファイルが変更されていない場合はスキップ
            if current_hash == last_hash:
                continue
            
            try:
                # 記事データを解析
                article_data = self.parse_markdown(filepath)
                
                # WordPressに投稿
                response = self.post_to_wordpress(article_data, post_id)
                
                if response.status_code in [200, 201]:
                    post_info = response.json()
                    
                    # ログを更新
                    sync_log[filename] = {
                        'hash': current_hash,
                        'post_id': post_info['id'],
                        'last_sync': datetime.now().isoformat(),
                        'title': article_data['title']
                    }
                    
                    if post_id:
                        results['updated'] += 1
                        print(f"✅ 更新: {article_data['title']}")
                    else:
                        results['new'] += 1
                        print(f"🆕 新規: {article_data['title']}")
                else:
                    results['errors'] += 1
                    print(f"❌ エラー: {filename} - {response.text}")
                    
            except Exception as e:
                results['errors'] += 1
                print(f"❌ 例外: {filename} - {str(e)}")
        
        # ログを保存
        self.save_sync_log(sync_log)
        
        print(f"\n📊 同期結果: 新規{results['new']}件, 更新{results['updated']}件, エラー{results['errors']}件")
        return results

def main():
    """メイン処理"""
    syncer = WordPressSyncer()
    syncer.sync_articles()

if __name__ == "__main__":
    main()
