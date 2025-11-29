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
        """複数サービスから画像を取得（フォールバック付き）"""
        import random
        
        # 複数サービスの画像プロバイダー
        image_providers = {
            'unsplash': self.get_unsplash_images(),
            'pixabay': self.get_pixabay_images(),
            'pexels': self.get_pexels_images()
        }
        
        # キーワードからカテゴリーを特定
        category = self.determine_category_from_keywords(keywords)
        
        # プロバイダーをランダムに試行
        providers = list(image_providers.keys())
        random.shuffle(providers)
        
        for provider in providers:
            try:
                if category in image_providers[provider]:
                    image_url = random.choice(image_providers[provider][category])
                    # 画像の可用性をテスト
                    if self.test_image_availability(image_url):
                        print(f"📸 画像取得: {provider}")
                        return image_url
            except Exception as e:
                print(f"⚠️ {provider}エラー: {str(e)}")
                continue
        
        # 全て失敗した場合のフォールバック
        return self.get_fallback_image()
    
    def get_unsplash_images(self):
        """Unsplash画像セット"""
        return {
            'AWS': [
                'https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1518709268805-4e9042af2176?ixlib=rb-4.0.3&w=1200&q=80'
            ],
            'Docker': [
                'https://images.unsplash.com/photo-1605745341112-85968b19335b?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1461749280684-dccba630e2f6?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1504639725590-34d0984388bd?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1517077304055-6e89abbf09b0?ixlib=rb-4.0.3&w=1200&q=80'
            ],
            'GitHub': [
                'https://images.unsplash.com/photo-1556075798-4825dfaaf498?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1542831371-29b0f74f9713?ixlib=rb-4.0.3&w=1200&q=80'
            ],
            'その他': [
                'https://images.unsplash.com/photo-1518709268805-4e9042af2176?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1461749280684-dccba630e2f6?ixlib=rb-4.0.3&w=1200&q=80',
                'https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?ixlib=rb-4.0.3&w=1200&q=80'
            ]
        }
    
    def get_pixabay_images(self):
        """Pixabay画像セット"""
        return {
            'AWS': [
                'https://cdn.pixabay.com/photo/2018/05/08/08/44/artificial-intelligence-3382507_1280.jpg',
                'https://cdn.pixabay.com/photo/2020/12/11/16/24/technology-5824678_1280.jpg',
                'https://cdn.pixabay.com/photo/2018/09/27/09/22/artificial-intelligence-3706562_1280.jpg'
            ],
            'Docker': [
                'https://cdn.pixabay.com/photo/2018/01/17/20/22/analytics-3088958_1280.jpg',
                'https://cdn.pixabay.com/photo/2016/11/30/20/58/programming-1873854_1280.png',
                'https://cdn.pixabay.com/photo/2018/05/04/20/01/website-3374825_1280.jpg'
            ],
            'GitHub': [
                'https://cdn.pixabay.com/photo/2015/05/29/09/04/code-788648_1280.jpg',
                'https://cdn.pixabay.com/photo/2016/11/19/14/00/code-1839406_1280.jpg',
                'https://cdn.pixabay.com/photo/2017/06/23/10/48/code-2434271_1280.jpg'
            ],
            'その他': [
                'https://cdn.pixabay.com/photo/2018/05/08/08/44/artificial-intelligence-3382507_1280.jpg',
                'https://cdn.pixabay.com/photo/2016/11/30/20/58/programming-1873854_1280.png'
            ]
        }
    
    def get_pexels_images(self):
        """Pexels画像セット"""
        return {
            'AWS': [
                'https://images.pexels.com/photos/1181671/pexels-photo-1181671.jpeg?auto=compress&cs=tinysrgb&w=1200',
                'https://images.pexels.com/photos/325229/pexels-photo-325229.jpeg?auto=compress&cs=tinysrgb&w=1200',
                'https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=1200'
            ],
            'Docker': [
                'https://images.pexels.com/photos/1181472/pexels-photo-1181472.jpeg?auto=compress&cs=tinysrgb&w=1200',
                'https://images.pexels.com/photos/270348/pexels-photo-270348.jpeg?auto=compress&cs=tinysrgb&w=1200',
                'https://images.pexels.com/photos/1181354/pexels-photo-1181354.jpeg?auto=compress&cs=tinysrgb&w=1200'
            ],
            'GitHub': [
                'https://images.pexels.com/photos/270373/pexels-photo-270373.jpeg?auto=compress&cs=tinysrgb&w=1200',
                'https://images.pexels.com/photos/1181675/pexels-photo-1181675.jpeg?auto=compress&cs=tinysrgb&w=1200',
                'https://images.pexels.com/photos/574071/pexels-photo-574071.jpeg?auto=compress&cs=tinysrgb&w=1200'
            ],
            'その他': [
                'https://images.pexels.com/photos/1181671/pexels-photo-1181671.jpeg?auto=compress&cs=tinysrgb&w=1200',
                'https://images.pexels.com/photos/270348/pexels-photo-270348.jpeg?auto=compress&cs=tinysrgb&w=1200'
            ]
        }
    
    def test_image_availability(self, image_url):
        """画像の可用性をテスト"""
        try:
            response = requests.head(image_url, timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def get_fallback_image(self):
        """フォールバック画像（最後の手段）"""
        return 'https://images.unsplash.com/photo-1518709268805-4e9042af2176?ixlib=rb-4.0.3&w=1200&q=80'
    
    def determine_category_from_keywords(self, keywords):
        """キーワードからカテゴリーを判定"""
        category_mapping = {
            'AWS': ['aws', 'lambda', 'ec2', 's3', 'server'],
            'Docker': ['docker', 'container'],
            'GitHub': ['github', 'git', 'development'],
            'Python': ['python', 'django', 'flask'],
            'JavaScript': ['javascript', 'js', 'node', 'react', 'vue'],
            'WordPress': ['wordpress', 'wp'],
            'TradingView': ['tradingview', 'trading'],
            'AI・機械学習': ['ai', 'ml', 'machine', 'learning'],
            'インフラ': ['infra', 'nginx', 'apache']
        }
        
        for keyword in keywords:
            for category, patterns in category_mapping.items():
                if keyword.lower() in patterns:
                    return category
        
        return 'その他'
    
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
