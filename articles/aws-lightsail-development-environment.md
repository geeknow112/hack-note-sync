AWS Lightsailでの開発環境構築の設定手順
AWS,Lightsail,vim,tmux
aws-lightsail-development-environment

>本記事は、AWS Lightsailを使用した開発環境構築について解説します。AWSの基本的な知識がある方を対象とし、初心者向けに解説しています。

## はじめに

こんにちは。今回は、AWS初心者に向けて、AWS Lightsailでの開発環境構築について解説します。AWSは、クラウドコンピューティングサービスの中でも特に大規模なもので、初めて触れる方には敷居が高く感じられることもあるかと思います。そこで、AWSの中でもLightsailを使用して、手軽に簡単に開発環境を構築する方法を解説します。

## AWS Lightsailとは

AWS Lightsailは、AWSのクラウドサービスの中でも、比較的手軽に利用できるサービスです。サービス名にあるように、仮想サーバーに必要なリソース（CPU、メモリ、ストレージなど）を事前に定義して、提供される「インスタンス」を簡単に作成することができます。また、Amazonが提供する多数のサービスとの統合も容易で、初めてAWSを触る方にも使いやすいと言われています。

## AWS Lightsailでの開発環境構築

### 1. AWSアカウントの作成とLightsailのインスタンス作成

まずは、AWSアカウントを作成します。アカウント作成後、Lightsailのコンソール画面に入り、新しいインスタンスを作成します。ここでは、Amazon Linux 2を使用することを想定して進めていきます。

### 2. SSH接続

インスタンスが作成されたら、SSH接続を行います。SSH接続には、ターミナルソフトウェアが必要です。Macの場合は、標準でTerminalアプリがありますが、Windowsの場合は、PuTTYやGit Bashなどを使用すると良いでしょう。

以下は、SSH接続のコマンド例です。

```
$ ssh -i /path/to/key.pem username@public_ip_address
```

ここで、/path/to/key.pemは、インスタンス作成時にダウンロードした秘密鍵のパスを指定します。また、usernameは、作成したインスタンスのユーザー名を指定します。public_ip_addressは、インスタンスのパブリックIPアドレスを指定します。

### 3. vimのインストール

SSH接続後、vimをインストールします。以下のコマンドを実行してください。

```
$ sudo yum install vim -y
```

### 4. tmuxのインストール

次に、tmuxをインストールします。tmuxは、SSH接続したターミナル上で、複数のウィンドウやペインを管理できるツールです。以下のコマンドを実行してください。

```
$ sudo yum install tmux -y
```

### 5. 開発環境の構築

vimとtmuxがインストールされたら、開発環境の構築を行います。ここでは、PythonとFlaskを使用する場合を想定して、開発環境を構築します。以下のコマンドを実行してください。

```
$ sudo yum install python3 -y
$ sudo pip3 install flask
```

以上で、AWS Lightsailでの開発環境構築が完了しました。

## まとめ

AWS Lightsailを使用して、簡単に開発環境を構築する方法を解説しました。初めてAWSを使用する方でも、手軽に使い始めることができます。また、vimやtmuxを使用することで、SSH接続したターミナル上での開発作業もスムーズに行うことができます。AWSを利用して、より高度な開発環境を構築することもできますので、今回の記事を参考に、AWSの利用に挑戦してみてください。

　

## AWS lightsail 関連のまとめ
https://hack-note.com/summary/aws-lightsail-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

