【簡単】awsの作業をcliで効率化する - workspaces編
aws,workspaces,cli,効率化
aws-workspaces-cli-wakeup

こんにちは。今回は、awsについて初心者エンジニアに向けて、awsのサービスの一つである「amazon workspaces」を利用した作業をcliで効率化する方法について解説します。

## awsとは

aws(amazon web services)とは、amazon.comの子会社であるamazon web services, inc.が提供するクラウドコンピューティングサービスです。awsを使用することで、インフラストラクチャの管理やサービスの展開を簡単に行うことができます。また、awsは多数のサービスを提供しているため、利用することで企業や個人の業務を効率的に行うことができます。

## amazon workspacesとは

amazon workspacesとは、awsが提供するクラウドデスクトップサービスです。従来のデスクトップpcを使う場合と同様に、windowsやlinuxをはじめとするオペレーティングシステムを操作することができます。また、リモートアクセスすることにより、場所やデバイスを問わずに作業が可能となります。

## cliとは

cli(command line interface)とは、コマンドラインから直接操作するインターフェースのことです。cliを使用することで、視覚的なアシストなどが少ない分、細かな設定を自由自在に行うことができます。awsの場合、cliを使用することで、複雑な作業を自動化することができ、効率的な作業を行うことができます。

## workspacesをcliで起動する

workspacesは、コンソール上からも起動できますが、cliを使うことで手軽に一括起動することができます。以下のコマンドを使用することで、aws cliでworkspacesを起動することができます。

```sh
aws workspaces start-workspaces --start-workspace-requests file://workspaces.json
```

このコマンドにより、workspacesの起動リクエストが送信され、workspacesが起動します。ここで、`workspaces.json`というファイルを作成し、起動するworkspace情報を記述しておく必要があります。

`workspaces.json`の例を以下に示します。

```json
{
  "startworkspacerequests": [
    {
      "workspaceid": "ws-xxxxxx"
    },
    {
      "workspaceid": "ws-yyyyyy"
    }
  ]
}
```

このファイルでは、"workspaceid"の部分に、起動したいworkspacesのidを指定する必要があります。また、複数のworkspacesを同時に起動する場合は、"startworkspacerequests"の配列にそれぞれのworkspacesの情報を記述する必要があります。

## バッチ処理で複数workspacesを起動する方法

複数のworkspacesを起動する場合、cliを使った起動リクエストの手間が大きくなることがあります。この場合、シェルスクリプトを使用することで、一度に複数のworkspacesを起動することができます。

以下は、bashを使ったシェルスクリプトの例です。

```sh
#!/bin/bash

# スタートする workspaces を格納する配列
workspaces=(
  ws-xxxxxx
  ws-yyyyyy
  ws-zzzzzz
)

# workspaces を起動するコマンド
command="aws workspaces start-workspaces --start-workspace-requests file://workspaces.json"

# workspaces の id をファイルに出力する
echo "{\"startworkspacerequests\": [" > workspaces.json
for workspace in "${workspaces[@]}"
do
    echo "{\"workspaceid\": \"$workspace\"}," >> workspaces.json
done

echo "]}" >> workspaces.json

# workspaces 起動処理のコマンドを実行
eval $command
```

このシェルスクリプトでは、起動するworkspacesのidを配列に格納しています。この配列を用いて、workspacesの起動リクエストを作成し、aws cliを使用して一括起動しています。

## まとめ

今回は、awsのサービスの一つである「amazon workspaces」をcliで起動する方法について解説しました。複数のworkspacesを起動する場合、シェルスクリプトを使用して一括起動する事ができるため、作業の効率化に役立ちます。awsやcliについてこれから勉強する初心者エンジニアの方は、ぜひ参考にしてみてください。

>本記事は、awsやcliに詳しい人向けの内容となっております。

>workspacesの起動や利用には、awsの各種設定が必要となります。
>必ず、awsの公式ドキュメントなどで各種セキュリティ設定を行った上で、ご利用ください。

　

## AWS Workspaces 関連まとめ
https://hack-note.com/summary/aws-workspaces-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

