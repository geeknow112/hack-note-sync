Docker + WP 環境構築/AWS CloudFront + S3 + ACM ホスティング環境
docker,WordPress,AWS,CloudFront,S3,ACM
docker-wordpress-aws-cloudfront-s3

Docker + WP 環境構築/AWS CloudFront + S3 + ACM ホスティング環境

【課題】ローカルでWordPressの実行環境を作りたい。
<p>WebでWordPressのサービスは多いけど、ローカルで使うとなると、PHPやMySQLやApacheをインストールしたり、WordPressをインストールしたりと環境を作るのに時間がかかる。xampやbitnamiなどのオールインワンのツールもあるが、PCが複数台あったりするとその都度作業環境を作らないといけないから手間がかかる。</p>

【要件】実行環境・インフラの共有
【設計】Dockerでの実行環境整備

【要件】Docker上でWordPressをインストール
【設計】ここはLamp構築と同じ。centos8で構築。

【要件】WordPressで静的コンテンツを出力したい。
【設計】simple staticプラグイン

【要件】WordPressで静的コンテンツを出力したい。
【設計】static pressプラグイン

【要件】WordPressで共通CSSを作りたい。
【設計】code snippetsプラグイン

【要件】WordPressで共通PHP Functionを作りたい。
【設計】code snippetsプラグイン

【要件】WordPressでショートコードを作りたい。 ※特定の記事で同じ文章を使いまわせる用のショートコードを即座に用意するには。
【設計】code snippetsプラグイン

【要件】WordPressで共通目次を作りたい。
【設計】Table Of Contents Plusプラグイン

【要件】WordPressでCSVインポートしたい。
【設計】Really Simple CSV Importプラグイン

【要件】WordPressでCSVエクスポートしたい。
【設計】WP Ultimate CSV Import/WP Ultimate Exporterプラグイン

【要件】S3バケットを用意してWordPressの静的コンテンツをアップロードする。自動アップロードできるならしたい。
【設計】Static Press + WordPress S3プラグイン

【要件】ドメイン取得とSSL設定
【設計】AWS Route53でドメイン取得 + AWS ACMでSSL取得

【要件】CDN設定
【設計】Route53 &gt; ACM &gt; AWS CloudFront &gt; S3静的コンテンツ、の順でアクセスできるように設定

　

## Docker 関連のまとめ
https://hack-note.com/summary/docker-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

