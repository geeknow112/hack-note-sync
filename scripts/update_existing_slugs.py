#!/usr/bin/env python3
"""
既存投稿のスラッグを英語に修正
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

# 修正対象の投稿
posts_to_update = [
    {
        'id': 15000,
        'new_slug': 'tradingview-csv-import-advanced-guide'
    },
    {
        'id': 15001, 
        'new_slug': 'github-vscode-team-development-guide'
    }
]

print("🔧 既存投稿のスラッグ修正開始")

for post in posts_to_update:
    print(f"\n📝 投稿ID {post['id']} を修正中...")
    
    # スラッグ更新
    update_data = {
        'slug': post['new_slug']
    }
    
    response = requests.post(
        f"{WP_URL}/wp-json/wp/v2/posts/{post['id']}",
        headers=headers,
        json=update_data
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ 修正成功: {result['link']}")
    else:
        print(f"❌ 修正失敗: {response.status_code}")
        print(f"📋 エラー: {response.text}")

print("\n🎉 スラッグ修正完了")
