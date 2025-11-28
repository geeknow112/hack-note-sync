#!/usr/bin/env python3
"""
単一記事投稿テスト
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

# 投稿データ
post_data = {
    'title': '【テスト】GitHub同期システムの動作確認',
    'content': '''
# GitHub同期システムテスト

このテスト記事は、GitHubリポジトリからWordPressへの自動同期システムの動作確認用です。

## システムの特徴
- GitHubにコミットすると自動でWordPressに投稿
- Markdownファイルから自動でHTML変換
- カテゴリーとタグの自動分類

## 技術スタック
- Python
- WordPress REST API
- GitHub Actions

---
*自動投稿システムによる投稿テストです。*
''',
    'status': 'publish',
    'categories': [939]  # インフラカテゴリー
}

print("🚀 WordPress投稿テスト開始")
print(f"📝 投稿先: {WP_URL}")
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
