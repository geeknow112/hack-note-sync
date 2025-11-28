#!/usr/bin/env python3
"""
スラッグ生成テスト
"""

from sync_to_wordpress import WordPressSyncer

def test_slug_generation():
    syncer = WordPressSyncer()
    
    test_files = [
        "tradingview_csv_import_advanced.md",
        "github_vscode_collaboration_guide.md"
    ]
    
    print("🔍 スラッグ生成テスト")
    print("=" * 50)
    
    for filename in test_files:
        filepath = f"articles/{filename}"
        try:
            article_data = syncer.parse_markdown(filepath)
            print(f"\n📄 ファイル: {filename}")
            print(f"📝 タイトル: {article_data['title']}")
            print(f"🔗 スラッグ: {article_data['slug']}")
            print(f"🏷️ カテゴリー: {article_data['category']}")
            print(f"🔖 タグ: {', '.join(article_data['tags'])}")
        except Exception as e:
            print(f"❌ エラー: {filename} - {str(e)}")

if __name__ == "__main__":
    test_slug_generation()
