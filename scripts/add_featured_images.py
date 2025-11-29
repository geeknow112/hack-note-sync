#!/usr/bin/env python3
"""
既存投稿にアイキャッチ画像を一括追加
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
import base64
from utils.image_generator import ImageGenerator

# 設定
WP_URL = "https://hack-note.com"
USERNAME = "myu"
PASSWORD = "QEBX aUmp 8ljk yXr6 OTyQ UjCd"

def get_posts_without_featured_image():
    """アイキャッチ画像がない投稿を取得"""
    credentials = f"{USERNAME}:{PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()
    headers = {
        'Authorization': f'Basic {token}',
        'Content-Type': 'application/json'
    }
    
    posts_without_image = []
    page = 1
    
    while True:
        response = requests.get(
            f"{WP_URL}/wp-json/wp/v2/posts",
            headers=headers,
            params={
                'per_page': 20,
                'page': page,
                '_fields': 'id,title,featured_media'
            }
        )
        
        if response.status_code != 200:
            break
            
        posts = response.json()
        if not posts:
            break
        
        for post in posts:
            if post['featured_media'] == 0:  # アイキャッチなし
                posts_without_image.append({
                    'id': post['id'],
                    'title': post['title']['rendered']
                })
        
        page += 1
        if len(posts) < 20:  # 最後のページ
            break
    
    return posts_without_image

def main():
    print("🎨 アイキャッチ画像一括追加開始")
    print("=" * 50)
    
    # アイキャッチなしの投稿を取得
    posts = get_posts_without_featured_image()
    print(f"📊 アイキャッチなし投稿: {len(posts)}件")
    
    if not posts:
        print("✅ 全ての投稿にアイキャッチが設定済みです")
        return
    
    # 画像生成システム初期化
    image_gen = ImageGenerator(WP_URL, USERNAME, PASSWORD)
    
    # 各投稿にアイキャッチを追加
    success_count = 0
    for i, post in enumerate(posts, 1):  # 全件処理
        print(f"\n[{i}/{len(posts)}] 処理中...")
        print(f"📄 ID: {post['id']}")
        print(f"📝 タイトル: {post['title']}")
        
        if image_gen.generate_featured_image(post['id'], post['title']):
            success_count += 1
        
        # API制限を考慮して少し待機
        import time
        time.sleep(1)  # 1秒に短縮
        
        # 100件ごとに進捗表示
        if i % 100 == 0:
            print(f"\n🔄 進捗: {i}/{len(posts)}件完了 (成功: {success_count}件)")
    
    print(f"\n🎉 完了: {success_count}/{len(posts)}件成功")

if __name__ == "__main__":
    main()
