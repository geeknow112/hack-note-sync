#!/usr/bin/env python3
"""
既存の投稿済み記事にアイキャッチ画像を追加
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.image_generator import ImageGenerator

# 投稿済み記事のID（今回のテスト投稿分）
existing_posts = [
    {'id': 15662, 'title': '【AWS Lambda】サーバーレス自動化で業務効率を劇的に改善する実践ガイド'},
    {'id': 15663, 'title': 'Docker本番環境デプロイメント完全ガイド：セキュリティとパフォーマンスを両立する実践手法'},
    {'id': 15664, 'title': '【初心者向け】GitHubとVS Codeでチーム開発を効率化する実践ガイド'}
]

def main():
    print("🎨 既存記事にアイキャッチ画像を追加")
    print("=" * 50)
    
    image_gen = ImageGenerator(
        'https://hack-note.com',
        'myu', 
        'QEBX aUmp 8ljk yXr6 OTyQ UjCd'
    )
    
    success_count = 0
    for post in existing_posts:
        print(f"\n📝 処理中: {post['title']}")
        
        if image_gen.generate_featured_image(post['id'], post['title']):
            success_count += 1
            print(f"✅ 完了")
        else:
            print(f"❌ 失敗")
    
    print(f"\n🎉 完了: {success_count}/{len(existing_posts)}件成功")

if __name__ == "__main__":
    main()
