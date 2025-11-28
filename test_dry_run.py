#!/usr/bin/env python3
"""
同期システムのドライランテスト
実際には投稿せずに、投稿データの準備まで確認
"""

import os
import json
from sync_to_wordpress import WordPressSyncer

class DryRunSyncer(WordPressSyncer):
    def __init__(self):
        # 設定を直接定義（認証情報不要）
        self.config = {
            'wordpress': {
                'url': 'https://hack-note.com',
                'username': 'test_user',
                'password': 'test_pass'
            },
            'sync': {
                'articles_dir': './articles',
                'log_file': './sync_log_dry_run.json'
            }
        }
        self.wp_url = self.config['wordpress']['url']
        self.wp_user = self.config['wordpress']['username'] 
        self.wp_pass = self.config['wordpress']['password']
        self.articles_dir = self.config['sync']['articles_dir']
        self.sync_log = self.config['sync']['log_file']
    
    def post_to_wordpress(self, article_data, update_id=None):
        """ドライラン: 実際には投稿せず、データ構造のみ確認"""
        print(f"📝 投稿データ準備完了: {article_data['title']}")
        print(f"   カテゴリー: {article_data['category']}")
        print(f"   タグ: {', '.join(article_data['tags'])}")
        print(f"   説明: {article_data['description'][:100]}...")
        
        # 模擬レスポンス
        class MockResponse:
            status_code = 201
            def json(self):
                return {'id': 999, 'link': 'https://hack-note.com/test-post'}
        
        return MockResponse()

def main():
    print("🚀 同期システム ドライランテスト開始")
    print("=" * 50)
    
    # 新規記事のみテスト
    test_articles = [
        "github_vscode_collaboration_guide.md",
        "tradingview_csv_import_advanced.md"
    ]
    
    syncer = DryRunSyncer()
    
    for filename in test_articles:
        filepath = os.path.join(syncer.articles_dir, filename)
        if os.path.exists(filepath):
            print(f"\n📄 処理中: {filename}")
            print("-" * 30)
            
            try:
                # 記事データを解析
                article_data = syncer.parse_markdown(filepath)
                
                # 投稿データ準備（ドライラン）
                response = syncer.post_to_wordpress(article_data)
                
                if response.status_code == 201:
                    print("✅ 投稿データ準備成功")
                else:
                    print("❌ エラー")
                    
            except Exception as e:
                print(f"❌ 例外: {str(e)}")
        else:
            print(f"❌ ファイルが見つかりません: {filename}")
    
    print("\n" + "=" * 50)
    print("✅ ドライランテスト完了")
    print("💡 実際の投稿には認証情報の設定が必要です")

if __name__ == "__main__":
    main()
