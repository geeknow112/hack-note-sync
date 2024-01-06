【aws cli】iamユーザーの作成と権限設定
aws,cli
aws_cli_iam

## aws cliを使用したiamユーザーの作成手順

こんにちは。今回は、aws cliについて初心者エンジニアに向けて、iamユーザーの作成と権限設定について解説します。

aws cli（command line interface）は、awsリソースを管理するためのコマンドラインツールです。cliを使用することで、手動操作に比べて効率的にawsリソースを作成および管理することができます。

初心者の方でも扱いやすいように、iam（identity and access management）ユーザーの作成手順について詳しく説明します。iamユーザーは、awsリソースにアクセスするための認証情報（アクセスキーとシークレットアクセスキー）や権限設定を管理するためのエンティティです。

まずはじめに、aws cliをインストールし、設定を行なってください。以下の公式ドキュメントを参考に進めてください。

[installing the aws cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

aws cliのインストールと設定が完了したら、iamユーザーの作成手順に入ります。

### 手順1: aws cliを使用してiamユーザーを作成する

まず、以下のコマンドを実行してiamユーザーを作成します。

```bash
aws iam create-user --user-name <ユーザー名>
```

`<ユーザー名>`には、作成するiamユーザーの名前を入力してください。

### 手順2: iamユーザーにアクセスキーとシークレットアクセスキーを設定する

iamユーザーには、アクセスキーとシークレットアクセスキーが必要です。以下のコマンドを実行して、iamユーザーに設定します。

```bash
aws iam create-access-key --user-name <ユーザー名>
```

`<ユーザー名>`には、アクセスキーとシークレットアクセスキーを設定するiamユーザーの名前を入力してください。

### 手順3: iamユーザーをグループに所属させ、ポリシーを割り当てる

iamユーザーをグループに所属させ、ポリシーを割り当てることで、ユーザーごとの権限を簡単に管理することができます。以下のコマンドを実行して、iamユーザーをグループに所属させます。

```bash
aws iam add-user-to-group --user-name <ユーザー名> --group-name <グループ名>
```

`<ユーザー名>`には、所属させるiamユーザーの名前を入力し、`<グループ名>`には、所属させるグループの名前を入力してください。

また、ポリシーを割り当てるために、以下のコマンドを実行します。

```bash
aws iam attach-group-policy --group-name <グループ名> --policy-arn <ポリシーのarn>
```

`<グループ名>`には、ポリシーを割り当てるグループの名前を入力し、`<ポリシーのarn>`には、割り当てるポリシーのarnを入力してください。

### 手順4: iamユーザーのパスワードポリシーとmfaを設定する

iamユーザーのセキュリティを強化するために、パスワードポリシーとmfa（multi-factor authentication）を設定することができます。以下のコマンドを実行して、iamユーザーにパスワードポリシーを設定します。

```bash
aws iam update-account-password-policy --minimum-password-length <パスワードの最小文字数> --require-uppercase-characters --require-lowercase-characters --require-symbols --require-numbers
```

`<パスワードの最小文字数>`には、パスワードの最小文字数を入力してください。

また、mfaを使用するために、以下のコマンドを実行します。

```bash
aws iam create-virtual-mfa-device --virtual-mfa-device-name <仮想mfaデバイス名>
```

`<仮想mfaデバイス名>`には、仮想mfaデバイスの名前を入力してください。

### 手順5: aws cliを使ったiamユーザーの一時的な認証情報の取得と管理

iamユーザーのアクセスキーとシークレットアクセスキーは、長期的な認証情報ですが、一時的な認証情報を使用することもできます。以下のコマンドを実行して、一時的な認証情報を取得します。

```bash
aws sts get-session-token --serial-number <mfaデバイスのシリアル番号> --token-code <mfaデバイスの認証コード>
```

`<mfaデバイスのシリアル番号>`には、mfaデバイスのシリアル番号を入力し、`<mfaデバイスの認証コード>`には、mfaデバイスの認証コードを入力してください。

このように、aws cliを使ってiamユーザーの作成や権限設定を行うことができます。aws cliを活用することで、簡単かつ効率的にiamユーザーを管理することができます。

参考リンク：
- [aws cli ユーザーガイド](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
- [aws identity and access management ドキュメント](https://docs.aws.amazon.com/iam/index.html)

　

## 【aws cli】関連のまとめ
https://hack-note.com/summary/aws-cli-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

