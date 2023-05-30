【簡単】WordpressをAWS Lightsailで最安で使う方法
wordpress,aws,lightsail
wordpress-aws-lightsail

# はじめに
この記事では、Wordpressを使ってブログを始める読者に
AWS Lightsailを使って最安でサーバーを立てることを解説しています。
以下の手順で実行することができます。

# 手順
## 1. Lightsailインスタンスの作成

まず、AWS Lightsailでインスタンスを作成します。

- AWSコンソールにログインし、Lightsailを開きます。
- 「インスタンスを作成」をクリックします。
- インスタンスのオペレーティングシステムを「Linux/Unix」に設定し、インスタンスのサイズを「512MB RAM、1 vCPU、20GB SSD」に設定します。
- インスタンスの場所を指定し、インスタンス名を設定します。
- 「作成」をクリックして、インスタンスを作成します。

## 2. Wordpressのインストール

次に、Wordpressをインストールします。

- Lightsailインスタンスにログインします。
- ApacheとPHPをインストールします。
```
sudo apt-get update
sudo apt-get install apache2 php mysql-server php-mysql -y
```
- Wordpressをダウンロードし、展開します。
```
cd /var/www/html
sudo wget https://wordpress.org/latest.tar.gz
sudo tar -xzvf latest.tar.gz
```
- Wordpressの設定を行います。
```
sudo mv wordpress/* ./
sudo rm -rf wordpress
sudo chown -R www-data:www-data /var/www/html/
```
- データベースを作成します。
```
sudo mysql -u root -p
CREATE DATABASE wordpress;
CREATE USER 'wp_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON wordpress.* TO 'wp_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```
- ブラウザで、LightsailインスタンスのパブリックIPにアクセスし、Wordpressのインストールを完了します。

## 3. セキュリティグループの設定

最後に、セキュリティグループの設定を行います。

- Lightsailの「ネットワーク」タブから、インスタンスのセキュリティグループを編集します。
- HTTP（ポート80）とHTTPS（ポート443）の入力を許可する規則を追加します。

以上の手順で、最安でAWSでWordpressを使うことができます。ただし、この方法は小規模なサイト向けであり、高トラフィックのサイトには適していません。より高度な機能を必要とする場合は、AWSの他のサービス（例えばEC2やRDS）を使用することを検討することをお勧めします。

# その他のお悩み
他のお悩みにも下記の記事で回答しています。

## LightsailでもEC2みたいにAuto Scalingできますか？
https://zenn.dev/gk12/articles/aws-lightsail-auto-scaling

## 高トラフィック時にがくるようになったら、AWS Lightsailから通常のEC2に移行はどうやればいいですか？
https://zenn.dev/gk12/articles/aws-lightsail-to-ec2

## AWS LightsailでWordpressを使う際に、データベースはどれがいいんだろう？
https://zenn.dev/gk12/articles/aws-lightsail-with-database

## Amazon Aurora ServerlessとRDSの比較：どちらを選ぶべきですか？
https://zenn.dev/gk12/articles/aws-comp-rds-aurora-serverless

## LightsailとRDSで月間PV数別のコストの概算がしりたい。
https://zenn.dev/gk12/articles/aws-lightsail-comp-cost

## AWS LightsailでもEC2みたいに開発環境は作れるの？
https://zenn.dev/gk12/articles/aws-lightsail-development-environment

## Wordpress案件を実際に取っていく方法をまとめました
プロのエンジニアになるには、独学を続けるより案件を実際に受注した方が近道です。
フリーランスエンジニアとしてやっていくにはどこかのタイミングで
案件を獲っていかないといけません。
最初から全てうまくいくことは稀でしょう。
となると、うまくいかないことを前提として最速で案件を回していった方が効率的です。

スキルを磨く勉強はほどほどにして、いかにして案件を獲っていくかを考えましょう。

https://hack-note.com/programming/engineer-freelance-wordpress/

