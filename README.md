# Hack Note Sync

WordPress自動同期システム - GitHubからWordPressへの記事自動投稿システム

## 🚀 概要

このプロジェクトは、GitHubリポジトリに保存されたMarkdown記事を自動的にWordPressサイトに同期・投稿するシステムです。記事の作成から公開まで完全自動化し、技術ブログの運用効率を大幅に向上させます。

## ✨ 主要機能

### 📝 記事管理
- **Markdown記事作成**: `articles/`フォルダでの記事管理
- **自動HTML変換**: Markdown記法からWordPress対応HTMLへの変換
- **英語スラッグ生成**: SEO対応の自動URL生成
- **カテゴリー自動分類**: ファイル名からの技術カテゴリー推定

### 🎨 アイキャッチ画像
- **自動画像生成**: 記事内容に応じたアイキャッチ画像の自動設定
- **複数プロバイダー対応**: Unsplash + Pixabay + Pexels
- **フォールバック機能**: 画像取得失敗時の自動切り替え
- **カテゴリー統一**: 技術分野ごとの一貫したデザインテーマ

### 🔒 安全性
- **下書き投稿**: 自動投稿は下書きステータスで安全確認
- **品質チェック**: 最小文字数・タイトル必須などの品質フィルター
- **事前確認**: 投稿前のプレビュー・承認機能
- **差分検出**: 変更された記事のみを処理

## 📁 プロジェクト構造

```
hack-note-sync/
├── articles/                    # Markdown記事ファイル
├── utils/
│   └── image_generator.py      # アイキャッチ画像生成
├── scripts/
│   ├── add_featured_images.py  # 一括画像追加
│   └── emergency_cleanup.py    # 緊急クリーンアップ
├── sync_to_wordpress.py        # メイン同期スクリプト（無効化済み）
├── sync_to_wordpress_safe.py   # 安全版同期スクリプト
├── config.yaml                 # 設定ファイル
└── sync_log.json              # 同期ログ
```

## 🛠️ セットアップ

### 1. 依存関係のインストール
```bash
pip install requests pyyaml
```

### 2. 設定ファイルの作成
```yaml
# config.yaml
wordpress:
  url: "https://your-site.com"
  username: "your-username"
  password: "your-app-password"

sync:
  articles_dir: "./articles"
  log_file: "./sync_log.json"

seo:
  default_description: "企業の業務効率化に役立つ技術情報をお届けします。"
  site_name: "Your Site Name"
  author: "Your Name"
```

### 3. WordPress設定
- アプリケーションパスワードの生成
- REST API の有効化確認

## 🚀 使用方法

### 安全な記事同期
```bash
# 事前確認付きの安全な同期
python3 sync_to_wordpress_safe.py
```

### アイキャッチ画像の一括追加
```bash
# 既存記事への画像追加
python3 scripts/add_featured_images.py
```

## 📊 ワークフロー

1. **記事作成**: `articles/`フォルダにMarkdownファイルを作成
2. **品質チェック**: 自動的な記事品質検証
3. **プレビュー**: 投稿予定記事の確認
4. **承認**: ユーザーによる投稿承認
5. **投稿**: WordPressに下書きとして投稿
6. **画像設定**: アイキャッチ画像の自動生成・設定
7. **手動公開**: 管理画面での最終確認・公開

## 🎯 対応技術カテゴリー

- **AWS**: Lambda, EC2, S3等のクラウドサービス
- **Docker**: コンテナ技術・デプロイメント
- **GitHub**: バージョン管理・CI/CD
- **Python**: プログラミング・データサイエンス
- **JavaScript**: ウェブ開発・フロントエンド
- **WordPress**: CMS・ウェブサイト構築
- **TradingView**: 金融・チャート分析
- **AI・機械学習**: 人工知能・データ分析
- **インフラ**: サーバー・ネットワーク

## 🔧 技術仕様

### 画像プロバイダー
- **Unsplash**: 高品質技術系画像
- **Pixabay**: 豊富な無料画像ライブラリ
- **Pexels**: プロフェッショナル画像

### WordPress REST API
- 記事投稿: `/wp-json/wp/v2/posts`
- メディア管理: `/wp-json/wp/v2/media`
- カテゴリー管理: `/wp-json/wp/v2/categories`

## 🚨 安全機能

### 品質チェック
- 最小文字数: 500文字以上
- タイトル必須: H1見出しの存在確認
- ファイル形式: Markdownファイルのみ処理

### 投稿制御
- 下書きステータス: 自動投稿は非公開
- 事前確認: 投稿前のユーザー承認
- 差分検出: 変更ファイルのみ処理

## 📈 今後の予定

- [ ] S3ストレージ対応
- [ ] GitHub Actions復旧
- [ ] 記事内容の自動生成改善
- [ ] SEO最適化強化
- [ ] 投稿スケジューリング機能

## 🤝 コントリビューション

1. このリポジトリをフォーク
2. フィーチャーブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 📞 サポート

問題や質問がある場合は、GitHubのIssuesページでお知らせください。

---

*企業の業務効率化に役立つ技術情報の自動配信システム*
