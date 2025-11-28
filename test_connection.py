#!/usr/bin/env python3
"""
WordPress接続テスト
"""

import requests
import base64

def test_wordpress_connection():
    """WordPress REST APIの接続テスト"""
    wp_url = "https://hack-note.com"
    
    # まず認証なしでREST APIの存在確認
    print("🔍 WordPress REST API確認中...")
    
    try:
        response = requests.get(f"{wp_url}/wp-json/wp/v2/posts?per_page=1")
        
        if response.status_code == 200:
            posts = response.json()
            print(f"✅ REST API利用可能")
            print(f"📄 投稿数確認: {len(posts)}件の投稿を取得")
            
            if posts:
                print(f"📝 最新投稿: {posts[0]['title']['rendered']}")
            
            return True
        else:
            print(f"❌ REST APIエラー: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ 接続エラー: {str(e)}")
        return False

def test_categories():
    """カテゴリー一覧取得テスト"""
    wp_url = "https://hack-note.com"
    
    print("\n🏷️ カテゴリー確認中...")
    
    try:
        response = requests.get(f"{wp_url}/wp-json/wp/v2/categories")
        
        if response.status_code == 200:
            categories = response.json()
            print(f"✅ カテゴリー取得成功: {len(categories)}個")
            
            for cat in categories[:5]:  # 最初の5個表示
                print(f"  - {cat['name']} (ID: {cat['id']})")
            
            return True
        else:
            print(f"❌ カテゴリー取得エラー: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ カテゴリー取得エラー: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 WordPress接続テスト開始")
    print("=" * 40)
    
    api_ok = test_wordpress_connection()
    cat_ok = test_categories()
    
    print("\n" + "=" * 40)
    if api_ok and cat_ok:
        print("✅ 接続テスト成功！同期システムが利用可能です")
    else:
        print("❌ 接続テスト失敗")
