【AWS CLI】アクセスキーとシークレットアクセスキーの設定
aws,cli
aws_cli_credentials

## awsアクセスキーとシークレットアクセスキーの概要
aws cli（command line interface）は、aws（amazon web services）のクラウドサービスをコマンドラインから操作するためのツールです。aws cliを使用するためには、アクセスキーとシークレットアクセスキーが必要です。アクセスキーは、awsアカウントの一意の識別子であり、シークレットアクセスキーはアカウントに対する認証情報です。この記事では、aws cliでのアクセスキーとシークレットアクセスキーの取得方法と設定手順について説明します。

参考ブログ記事：
- [aws cli が入って aws の設定する手順](https://qiita.com/soarflat/items/771f5494bec2c98932f9)
- [aws cliの導入と初期設定](https://qiita.com/hiko1129/items/b9a43814228472d13a0e)

## aws cliでのアクセスキーとシークレットアクセスキーの取得方法
aws cliを使用するためには、まずアクセスキーとシークレットアクセスキーを取得する必要があります。

awsマネジメントコンソールにログインし、右上部の「アカウント名」をクリックして表示されるメニューの中から「セキュリティ認証情報」を選択します。次に、「アクセスキー」を選択し、「新しいアクセスキーの作成」をクリックします。すると、アクセスキーidとシークレットアクセスキーが生成されます。

```shell
aws configure

aws access key id [none]: <アクセスキーid>
aws secret access key [none]: <シークレットアクセスキー>
default region name [none]: <リージョン>
default output format [none]: <出力形式>
```

参考ブログ記事：
- [【aws cli】アクセスキーとシークレットアクセスキーの設定](https://architectboard.net/aws/aws-cli%e3%83%bb%e3%82%a2%e3%82%af%e3%82%bb%e3%82%b9%e3%82%ad%e3%83%bc%e3%83%bb%e3%82%b7%e3%83%bc%e3%82%af%e3%83%ac%e3%83%83%e3%83%88%e3%82%a2%e3%82%af%e3%82%bb%e3%82%b9%e3%82%ad%e3%83%bc/)

## aws cliでのアクセスキーとシークレットアクセスキーの設定手順
取得したアクセスキーとシークレットアクセスキーを使用して、aws cliに設定する手順を説明します。

まず、ターミナルを開き、以下のコマンドを入力してaws cliの設定を開始します。

```shell
aws configure
```

すると、アクセスキーid、シークレットアクセスキー、デフォルトのリージョン、出力形式の設定項目が表示されます。

```shell
aws access key id [none]: <アクセスキーid>
aws secret access key [none]: <シークレットアクセスキー>
default region name [none]: <リージョン>
default output format [none]: <出力形式>
```

上記のように順番に入力していきます。アクセスキーidとシークレットアクセスキーは先ほど取得したものを入力します。リージョンと出力形式は任意の値を入力することができます。

設定が完了すると、`~/.aws/credentials` ファイルにアクセスキーとシークレットアクセスキーが保存されます。

参考ブログ記事：
- [aws cliのインストールと設定方法](https://kiyotakeshi.hatenablog.com/entry/2017/05/30/004256)
- [aws cliの利用方法まとめ](https://karatejb.hatenablog.com/entry/aws_cli_summary)

## 環境変数を使用したaws cliのアクセスキーとシークレットアクセスキーの設定
aws cliでは、環境変数を使用してアクセスキーとシークレットアクセスキーを設定することもできます。

まず、環境変数を設定するために、`.bashrc` や `.bash_profile` ファイルを編集します。

```shell
vim ~/.bashrc
```

編集画面が表示されたら、以下のように環境変数を設定します。

```shell
export aws_access_key_id=<アクセスキーid>
export aws_secret_access_key=<シークレットアクセスキー>
```

環境変数を設定したら、保存して終了します。

```shell
source ~/.bashrc
```

この設定により、aws cliは環境変数からアクセスキーとシークレットアクセスキーを取得するようになります。

参考ブログ記事：
- [aws cliのプロファイルを使わずにcliを利用する方法](https://qiita.com/tk_sogn/items/6d121bc1e791830e3437)
- [aws cliの設定と使い方](https://dr-drf.hatenablog.com/entry/2019/09/18/001857)

## aws cliプロファイルを使用したアクセスキーとシークレットアクセスキーの管理
aws cliでは、複数のawsアカウントを使用する場合や、異なるアクセス権限を持つ場合など、複数のアクセスキーとシークレットアクセスキーの管理が必要な場合があります。このような場合には、aws cliプロファイルを使用することで、複数のアカウントや異なるアクセス権限を切り替えながら使用することができます。

まず、aws cliの設定ファイルである `~/.aws/config` ファイルを編集します。

```shell
vim ~/.aws/config
```

編集画面が表示されたら、以下のようにプロファイルを設定します。

```shell
[profile プロファイル名]
region=<リージョン>
output=<出力形式>
```

上記のようにプロファイルごとにリージョンや出力形式を設定することができます。

設定が完了したら、以下のようにプロファイルを指定してaws cliを実行することができます。

```shell
aws --profile プロファイル名 コマンド
```

参考ブログ記事：
- [aws cliで複数アカウントを扱う方法](http://dev.classmethod.jp/articles/multiple-aws-cli-profiles/)
- [aws cliでプロファイルを使って異なるawsアカウントに切り替える方法](https://qiita.com/drizzle/items/c14edd4fc0c0909cdf0a)

　

## 【AWS CLI】関連のまとめ
https://hack-note.com/summary/aws-cli-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

