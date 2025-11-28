#!/usr/bin/env python3
"""
記事解析テスト（認証不要）
"""

import os
import re
import hashlib

def parse_markdown(filepath):
    """Markdownファイルを解析してメタデータと本文を抽出"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # タイトル抽出（最初のH1）
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else os.path.basename(filepath).replace('.md', '')
    
    # カテゴリー推定（ファイル名から）
    filename = os.path.basename(filepath)
    category = guess_category(filename)
    
    # タグ抽出（見出しから）
    tags = extract_tags(content)
    
    # メタディスクリプション生成
    description = generate_description(content)
    
    return {
        'title': title,
        'content': content[:200] + '...',  # 最初の200文字のみ表示
        'category': category,
        'tags': tags,
        'description': description,
        'filename': filename
    }

def guess_category(filename):
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

def extract_tags(content):
    """コンテンツから関連タグを抽出"""
    # 見出しからキーワードを抽出
    headings = re.findall(r'^#{2,6} (.+)$', content, re.MULTILINE)
    tags = []
    
    for heading in headings[:5]:  # 最初の5個の見出しから
        # 技術用語を抽出
        tech_words = re.findall(r'\b[A-Z][a-z]+\b|\b[A-Z]{2,}\b', heading)
        tags.extend(tech_words)
    
    return list(set(tags))[:10]  # 重複除去、最大10個

def generate_description(content):
    """メタディスクリプションを生成"""
    # 最初の段落を取得
    paragraphs = content.split('\n\n')
    for para in paragraphs:
        if para.strip() and not para.startswith('#'):
            # HTMLタグとMarkdown記法を除去
            clean_text = re.sub(r'[#*`\[\]()]', '', para)
            return clean_text[:150] + '...' if len(clean_text) > 150 else clean_text
    return "企業の業務効率化に役立つ技術情報をお届けします。"

def test_new_articles():
    """新規追加記事のテスト"""
    articles_dir = "./articles"
    new_articles = [
        "github_vscode_collaboration_guide.md",
        "tradingview_csv_import_advanced.md"
    ]
    
    print("🚀 新規記事解析テスト開始")
    print("=" * 50)
    
    for filename in new_articles:
        filepath = os.path.join(articles_dir, filename)
        if os.path.exists(filepath):
            print(f"\n📄 解析中: {filename}")
            print("-" * 30)
            
            article_data = parse_markdown(filepath)
            
            print(f"📝 タイトル: {article_data['title']}")
            print(f"🏷️ カテゴリー: {article_data['category']}")
            print(f"🔖 タグ: {', '.join(article_data['tags'])}")
            print(f"📋 説明: {article_data['description']}")
            print(f"📊 内容プレビュー: {article_data['content']}")
        else:
            print(f"❌ ファイルが見つかりません: {filename}")

if __name__ == "__main__":
    test_new_articles()
