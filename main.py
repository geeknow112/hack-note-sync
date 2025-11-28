#!/usr/bin/env python3
"""
Hack Note Sync - GitHub to WordPress Auto Sync System
メイン実行ファイル
"""

import sys
import os
from sync_to_wordpress import WordPressSyncer

def main():
    """メイン処理"""
    print("🚀 Hack Note Sync システム開始")
    print("=" * 50)
    
    # 設定ファイルの存在確認
    if not os.path.exists('config.yaml'):
        print("❌ config.yamlが見つかりません")
        print("設定ファイルを作成してください")
        return 1
    
    try:
        # 同期実行
        syncer = WordPressSyncer()
        results = syncer.sync_articles()
        
        # 結果表示
        print("\n" + "=" * 50)
        print("✅ 同期完了")
        print(f"📈 新規記事: {results['new']}件")
        print(f"🔄 更新記事: {results['updated']}件")
        print(f"❌ エラー: {results['errors']}件")
        
        return 0 if results['errors'] == 0 else 1
        
    except Exception as e:
        print(f"❌ システムエラー: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
