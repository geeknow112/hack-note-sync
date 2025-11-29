#!/usr/bin/env python3
"""
緊急: 意図しない一括投稿の削除
"""

import requests
import base64
from datetime import datetime

# 設定
WP_URL = "https://hack-note.com"
USERNAME = "myu"
PASSWORD = "QEBX aUmp 8ljk yXr6 OTyQ UjCd"

def delete_todays_posts_except_lambda():
    """AWS Lambda記事以外の今日の投稿を削除"""
    credentials = f"{USERNAME}:{PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()
    headers = {
        'Authorization': f'Basic {token}',
        'Content-Type': 'application/json'
    }
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 今日の投稿を取得
    all_posts = []
    page = 1
    
    while True:
        response = requests.get(
            f"{WP_URL}/wp-json/wp/v2/posts",
            headers=headers,
            params={
                'after': f'{today}T00:00:00',
                'per_page': 100,
                'page': page,
                '_fields': 'id,title'
            }
        )
        
        if response.status_code != 200:
            break
            
        posts = response.json()
        if not posts:
            break
            
        all_posts.extend(posts)
        page += 1
        
        if len(posts) < 100:
            break
    
    # AWS Lambda記事は保持
    lambda_post_id = 15469
    posts_to_delete = [p for p in all_posts if p['id'] != lambda_post_id]
    
    print(f"🗑️ 削除対象: {len(posts_to_delete)}件")
    print(f"✅ 保持: AWS Lambda記事 (ID: {lambda_post_id})")
    
    # 削除実行
    deleted_count = 0
    for post in posts_to_delete:
        try:
            response = requests.delete(
                f"{WP_URL}/wp-json/wp/v2/posts/{post['id']}",
                headers=headers,
                params={'force': True}
            )
            
            if response.status_code == 200:
                deleted_count += 1
                print(f"✅ 削除: ID:{post['id']} - {post['title']['rendered']}")
            else:
                print(f"❌ 削除失敗: ID:{post['id']}")
                
        except Exception as e:
            print(f"❌ エラー: ID:{post['id']} - {str(e)}")
    
    print(f"\n🎉 削除完了: {deleted_count}/{len(posts_to_delete)}件")

if __name__ == "__main__":
    print("🚨 緊急クリーンアップ開始")
    delete_todays_posts_except_lambda()
