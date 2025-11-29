#!/usr/bin/env python3
"""
安全な同期システム - 事前確認・差分検出・品質チェック付き
"""

import os
import json
import hashlib
import requests
import base64
import re
from datetime import datetime

class SafeWordPressSyncer:
    def __init__(self, config_file='config.yaml'):
        import yaml
        with open(config_file, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        
        self.wp_url = self.config['wordpress']['url']
        self.wp_user = self.config['wordpress']['username']
        self.wp_pass = self.config['wordpress']['password']
        
        credentials = f"{self.wp_user}:{self.wp_pass}"
        token = base64.b64encode(credentials.encode()).decode()
        self.headers = {
            'Authorization': f'Basic {token}',
            'Content-Type': 'application/json'
        }
        
        self.sync_log = 'sync_log.json'
        self.articles_dir = 'articles'
    
    def is_valid_article(self, filepath, content):
        """記事として有効かチェック"""
        filename = os.path.basename(filepath)
        
        # 1. Markdownファイルのみ
        if not filename.endswith('.md'):
            return False, "Markdownファイルではありません"
        
        # 2. 最小文字数チェック（500文字以上）
        if len(content) < 500:
            return False, f"文字数不足: {len(content)}文字（最小500文字）"
        
        # 3. タイトル存在チェック
        if not content.startswith('#'):
            return False, "タイトル（# 見出し）がありません"
        
        # 4. 除外ファイル
        exclude_patterns = [
            'README.md',
            'test_',
            'sample_',
            '_temp',
            'draft_'
        ]
        
        for pattern in exclude_patterns:
            if pattern in filename:
                return False, f"除外パターン: {pattern}"
        
        return True, "OK"
    
    def get_pending_articles(self):
        """投稿予定の記事を取得"""
        log_data = self.load_sync_log()
        pending = []
        
        for filename in os.listdir(self.articles_dir):
            filepath = os.path.join(self.articles_dir, filename)
            
            if not os.path.isfile(filepath):
                continue
            
            # ファイルハッシュ計算
            current_hash = self.get_file_hash(filepath)
            
            # 同期済みかチェック
            if filename in log_data:
                if log_data[filename]['hash'] == current_hash:
                    continue  # 変更なし
                else:
                    action = "更新"
            else:
                action = "新規"
            
            # 記事として有効かチェック
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            is_valid, reason = self.is_valid_article(filepath, content)
            
            pending.append({
                'filename': filename,
                'filepath': filepath,
                'action': action,
                'valid': is_valid,
                'reason': reason,
                'size': len(content)
            })
        
        return pending
    
    def preview_sync(self):
        """同期プレビュー"""
        pending = self.get_pending_articles()
        
        valid_articles = [p for p in pending if p['valid']]
        invalid_articles = [p for p in pending if not p['valid']]
        
        print("📋 同期プレビュー")
        print("=" * 50)
        
        if valid_articles:
            print(f"✅ 投稿予定: {len(valid_articles)}件")
            for article in valid_articles:
                print(f"  • {article['action']}: {article['filename']} ({article['size']}文字)")
        
        if invalid_articles:
            print(f"\n❌ 除外: {len(invalid_articles)}件")
            for article in invalid_articles:
                print(f"  • {article['filename']}: {article['reason']}")
        
        if not valid_articles:
            print("📝 投稿する記事がありません")
            return False
        
        return valid_articles
    
    def confirm_sync(self, articles):
        """同期確認"""
        print(f"\n🚨 {len(articles)}件の記事を投稿します。よろしいですか？")
        print("⚠️  この操作は取り消せません。")
        
        while True:
            response = input("続行しますか？ (yes/no): ").lower().strip()
            if response in ['yes', 'y']:
                return True
            elif response in ['no', 'n']:
                return False
            else:
                print("yes または no で答えてください")
    
    def get_file_hash(self, filepath):
        """ファイルハッシュ計算"""
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    
    def load_sync_log(self):
        """同期ログ読み込み"""
        if os.path.exists(self.sync_log):
            with open(self.sync_log, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_sync_log(self, log_data):
        """同期ログ保存"""
        with open(self.sync_log, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, ensure_ascii=False, indent=2)
    
    def safe_sync(self):
        """安全な同期実行"""
        print("🔍 記事をスキャン中...")
        
        # プレビュー
        articles = self.preview_sync()
        if not articles:
            return
        
        # 確認
        if not self.confirm_sync(articles):
            print("❌ 同期をキャンセルしました")
            return
        
        print("\n🚀 同期開始...")
        # 実際の同期処理はここに実装
        print("✅ 安全な同期システムが準備できました")

if __name__ == "__main__":
    syncer = SafeWordPressSyncer()
    syncer.safe_sync()
