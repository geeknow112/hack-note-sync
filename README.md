# Hack Note Sync

GitHub リポジトリの記事を WordPress に自動同期するシステム

## 🚀 機能

- **自動同期**: GitHub にコミットすると WordPress に自動投稿
- **差分検出**: 変更されたファイルのみ同期
- **カテゴリー自動分類**: ファイル名から適切なカテゴリーを推定
- **SEO最適化**: メタディスクリプション、タグの自動生成
- **英語パーマリンク**: ファイル名から英語スラッグを自動生成
- **Markdown→HTML変換**: WordPress表示用に自動変換
- **エラーハンドリング**: 詳細なログとエラー報告

## 📁 ディレクトリ構造

```
hack-note-sync/
├── articles/           # Markdown記事ファイル
├── code/              # サンプルコード
├── scripts/           # 投稿・修正用スクリプト
├── tests/             # テスト用スクリプト
├── utils/             # ユーティリティ関数
├── .github/workflows/ # GitHub Actions設定
├── sync_to_wordpress.py # メイン同期スクリプト
├── config.yaml        # 設定ファイル
├── main.py            # 実行ファイル
└── requirements.txt   # 依存関係
```

## ⚙️ セットアップ

### 1. WordPress設定

1. WordPress管理画面でアプリケーションパスワードを生成
2. REST APIが有効になっていることを確認

### 2. GitHub Secrets設定

リポジトリの Settings > Secrets で以下を設定:

- `WP_URL`: WordPressサイトURL (https://hack-note.com)
- `WP_USERNAME`: WordPressユーザー名
- `WP_PASSWORD`: アプリケーションパスワード

### 3. ローカル実行

```bash
# 依存関係インストール
pip install -r requirements.txt

# 設定ファイル編集
cp config.yaml.example config.yaml
# config.yamlを編集

# 同期実行
python main.py
```

## 📝 記事の追加方法

1. `articles/` ディレクトリに Markdown ファイルを追加
2. ファイル名で自動カテゴリー分類:
   - `aws-*.md` → AWS カテゴリー
   - `python-*.md` → Python カテゴリー
   - `docker-*.md` → Docker カテゴリー
3. Git にコミット・プッシュで自動同期

## 🔄 同期の仕組み

1. **ファイル変更検出**: MD5ハッシュで変更を検出
2. **メタデータ抽出**: タイトル、カテゴリー、タグを自動生成
3. **英語スラッグ生成**: ファイル名から SEO フレンドリーな URL を作成
4. **Markdown→HTML変換**: WordPress 表示用に自動変換
5. **WordPress投稿**: REST API経由で投稿/更新
6. **ログ記録**: 同期状況を `sync_log.json` に記録

## 📊 カテゴリー自動分類

| ファイル名パターン | カテゴリー |
|------------------|-----------|
| aws-* | AWS |
| python-* | Python |
| docker-* | Docker |
| github-* | GitHub |
| ai-* | AI・機械学習 |
| tradingview-* | TradingView |

## 🛠️ トラブルシューティング

### 認証エラー
- アプリケーションパスワードを再生成
- WordPress REST APIの有効性を確認

### 同期エラー
- `sync_log.json` でエラー詳細を確認
- ファイル形式（UTF-8, Markdown）を確認

## ⚠️ 重要な教訓・注意事項

### パーマリンク設定
- **必須**: WordPressのパーマリンク設定を「投稿名」にする
- **理由**: 日本語URLはSEOに不利、英語URLが推奨
- **対策**: システムが自動で英語スラッグを生成

### Markdown記法の処理
- **問題**: WordPressはMarkdownを直接表示できない
- **解決**: システムが自動でHTML変換を実行
- **注意**: 複雑なMarkdown記法は手動調整が必要な場合あり

### WordPress REST API
- **確認事項**: WordPress 5.6以降で標準搭載
- **認証**: アプリケーションパスワード必須
- **権限**: 投稿者以上の権限が必要

### 既存投稿の修正
- **スラッグ変更**: 既存投稿のURLを変更する場合はリダイレクト設定推奨
- **一括修正**: 大量の投稿修正時はバックアップ必須
- **SEO影響**: URL変更はSEOに影響するため慎重に実施

## 📈 今後の拡張予定

- [ ] 画像の自動アップロード
- [ ] 記事の自動削除同期
- [ ] 複数サイト対応
- [ ] 記事テンプレート機能

## 🤝 貢献

1. Fork this repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

---

**Hack Note** - 企業の業務効率化のための技術情報サイト