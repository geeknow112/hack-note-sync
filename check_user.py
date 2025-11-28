#!/usr/bin/env python3
"""
ユーザー情報確認
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

print("🔍 ユーザー情報確認中...")

# 現在のユーザー情報を取得
response = requests.get(
    f"{WP_URL}/wp-json/wp/v2/users/me",
    headers=headers
)

if response.status_code == 200:
    user_info = response.json()
    print("✅ 認証成功")
    print(f"👤 ユーザー名: {user_info.get('name')}")
    print(f"📧 メール: {user_info.get('email')}")
    print(f"🔑 権限: {user_info.get('roles')}")
    print(f"🆔 ユーザーID: {user_info.get('id')}")
else:
    print(f"❌ 認証失敗: {response.status_code}")
    print(f"📋 エラー: {response.text}")

# 投稿権限をテスト（下書きで）
print("\n📝 投稿権限テスト中...")
test_post = {
    'title': 'テスト投稿（下書き）',
    'content': 'これは権限テスト用の下書きです。',
    'status': 'draft'  # 下書きで試す
}

response = requests.post(
    f"{WP_URL}/wp-json/wp/v2/posts",
    headers=headers,
    json=test_post
)

if response.status_code == 201:
    print("✅ 投稿権限あり")
    result = response.json()
    print(f"📊 下書きID: {result['id']}")
else:
    print(f"❌ 投稿権限なし: {response.status_code}")
    print(f"📋 エラー: {response.text}")
