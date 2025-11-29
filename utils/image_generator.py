#!/usr/bin/env python3
"""
自動アイキャッチ画像生成システム
"""

import requests
import re
import os
import base64
from urllib.parse import urlparse

class ImageGenerator:
    def __init__(self, wp_url, wp_user, wp_pass):
        self.wp_url = wp_url
        credentials = f"{wp_user}:{wp_pass}"
        token = base64.b64encode(credentials.encode()).decode()
        self.headers = {
            'Authorization': f'Basic {token}',
            'Content-Type': 'application/json'
        }
    
    def extract_keywords(self, title):
        """記事タイトルからキーワードを抽出"""
        # 日本語の括弧や記号を除去
        clean_title = re.sub(r'[【】\[\]（）()「」『』]', ' ', title)
        
        # 技術キーワードを抽出
        tech_keywords = [
            'AWS', 'Lambda', 'Python', 'Docker', 'GitHub', 'WordPress',
            'JavaScript', 'React', 'Vue', 'Django', 'Laravel', 'PHP',
            'MySQL', 'PostgreSQL', 'Redis', 'Nginx', 'Apache', 'Linux',
            'Ubuntu', 'CentOS', 'API', 'REST', 'GraphQL', 'JSON',
            'HTML', 'CSS', 'Bootstrap', 'Sass', 'TypeScript', 'Node.js',
            'Express', 'MongoDB', 'Firebase', 'Heroku', 'Vercel',
            'TradingView', 'AI', 'Machine Learning', 'Deep Learning'
        ]
        
        keywords = []
        for keyword in tech_keywords:
            if keyword.lower() in clean_title.lower():
                keywords.append(keyword)
        
        # 一般的なキーワードも追加
        if 'サーバー' in title or 'server' in title.lower():
            keywords.append('server')
        if '開発' in title or 'development' in title.lower():
            keywords.append('development')
        if '自動化' in title or 'automation' in title.lower():
            keywords.append('automation')
        
        return keywords[:3]  # 最大3個
    
    def search_unsplash_image(self, keywords):
        """Unsplash APIで画像を検索"""
        # より安定したデモ画像URL
        demo_images = {
            'aws': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&w=1200&q=80',
            'lambda': 'https://images.unsplash.com/photo-1518709268805-4e9042af2176?ixlib=rb-4.0.3&w=1200&q=80',
            'python': 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?ixlib=rb-4.0.3&w=1200&q=80',
            'docker': 'https://images.unsplash.com/photo-1605745341112-85968b19335b?ixlib=rb-4.0.3&w=1200&q=80',
            'github': 'https://images.unsplash.com/photo-1556075798-4825dfaaf498?ixlib=rb-4.0.3&w=1200&q=80',
            'wordpress': 'https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?ixlib=rb-4.0.3&w=1200&q=80',
            'javascript': 'https://images.unsplash.com/photo-1579468118864-1b9ea3c0db4a?ixlib=rb-4.0.3&w=1200&q=80',
            'server': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?ixlib=rb-4.0.3&w=1200&q=80',
            'development': 'https://images.unsplash.com/photo-1461749280684-dccba630e2f6?ixlib=rb-4.0.3&w=1200&q=80',
            'automation': 'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?ixlib=rb-4.0.3&w=1200&q=80',
            'default': 'https://images.unsplash.com/photo-1518709268805-4e9042af2176?ixlib=rb-4.0.3&w=1200&q=80'
        }
        
        # キーワードマッチング
        for keyword in keywords:
            if keyword.lower() in demo_images:
                return demo_images[keyword.lower()]
        
        # キーワードがない場合はデフォルト
        return demo_images['default']
    
    def download_image(self, image_url):
        """画像をダウンロード"""
        try:
            response = requests.get(image_url)
            if response.status_code == 200:
                return response.content
        except Exception as e:
            print(f"画像ダウンロードエラー: {e}")
        return None
    
    def upload_to_wordpress(self, image_data, filename):
        """WordPressに画像をアップロード"""
        try:
            # メディアアップロード用のヘッダー
            upload_headers = {
                'Authorization': self.headers['Authorization'],
                'Content-Disposition': f'attachment; filename="{filename}"',
                'Content-Type': 'image/jpeg'
            }
            
            response = requests.post(
                f"{self.wp_url}/wp-json/wp/v2/media",
                headers=upload_headers,
                data=image_data
            )
            
            if response.status_code == 201:
                return response.json()['id']
                
        except Exception as e:
            print(f"WordPress画像アップロードエラー: {e}")
        
        return None
    
    def set_featured_image(self, post_id, image_id):
        """投稿にアイキャッチ画像を設定"""
        try:
            response = requests.post(
                f"{self.wp_url}/wp-json/wp/v2/posts/{post_id}",
                headers=self.headers,
                json={'featured_media': image_id}
            )
            
            return response.status_code == 200
            
        except Exception as e:
            print(f"アイキャッチ設定エラー: {e}")
            return False
    
    def generate_featured_image(self, post_id, title):
        """記事にアイキャッチ画像を自動生成・設定"""
        print(f"🎨 アイキャッチ生成中: {title}")
        
        # キーワード抽出
        keywords = self.extract_keywords(title)
        print(f"📝 キーワード: {', '.join(keywords)}")
        
        # 画像検索
        image_url = self.search_unsplash_image(keywords)
        if not image_url:
            print("❌ 画像が見つかりませんでした")
            return False
        
        # 画像ダウンロード
        image_data = self.download_image(image_url)
        if not image_data:
            print("❌ 画像ダウンロードに失敗しました")
            return False
        
        # WordPressにアップロード
        filename = f"featured-{post_id}.jpg"
        image_id = self.upload_to_wordpress(image_data, filename)
        if not image_id:
            print("❌ 画像アップロードに失敗しました")
            return False
        
        # アイキャッチ設定
        if self.set_featured_image(post_id, image_id):
            print(f"✅ アイキャッチ設定完了: 画像ID {image_id}")
            return True
        else:
            print("❌ アイキャッチ設定に失敗しました")
            return False
