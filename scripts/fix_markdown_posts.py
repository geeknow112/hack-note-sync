#!/usr/bin/env python3
"""
既存投稿のMarkdownをHTMLに変換して更新
"""

import requests
import base64
from markdown_to_html import markdown_to_html

# 設定
WP_URL = "https://hack-note.com"
USERNAME = "myu"
PASSWORD = "QEBX aUmp 8ljk yXr6 OTyQ UjCd"

# 認証ヘッダー
credentials = f"{USERNAME}:{PASSWORD}"
token = base64.b64encode(credentials.encode()).decode()
headers = {
    'Authorization': f'Basic {token}',
    'Content-Type': 'application/json'
}

# TradingView記事の内容を読み込み
with open('articles/tradingview_csv_import_advanced.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# MarkdownをHTMLに変換
html_content = markdown_to_html(markdown_content)

# 投稿ID 15000を更新
post_id = 15000
update_data = {
    'content': html_content
}

print(f"🔧 投稿ID {post_id} のMarkdown修正中...")

response = requests.post(
    f"{WP_URL}/wp-json/wp/v2/posts/{post_id}",
    headers=headers,
    json=update_data
)

if response.status_code == 200:
    result = response.json()
    print("✅ Markdown修正成功！")
    print(f"🔗 URL: {result['link']}")
else:
    print(f"❌ 修正失敗: {response.status_code}")
    print(f"📋 エラー: {response.text}")
