#!/usr/bin/env python3
"""
TradingView記事投稿
"""

import requests
import base64

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
    content = f.read()

# 投稿データ
post_data = {
    'title': '【TradingView】CSVデータの高度なインポート設定と活用法',
    'content': content,
    'status': 'publish',
    'categories': [954]  # ツールカテゴリー
}

print("🚀 TradingView記事投稿開始")
print(f"📄 タイトル: {post_data['title']}")

# 投稿実行
response = requests.post(
    f"{WP_URL}/wp-json/wp/v2/posts",
    headers=headers,
    json=post_data
)

if response.status_code == 201:
    result = response.json()
    print("✅ 投稿成功！")
    print(f"🔗 URL: {result['link']}")
    print(f"📊 投稿ID: {result['id']}")
else:
    print(f"❌ 投稿失敗: {response.status_code}")
    print(f"📋 エラー: {response.text}")
