【解決】aws fsxをセルフマネージドadで起動時にestablishエラー
aws,fsx,active-directory,問題
aws-fsx-error-establish

こんにちは。今回は、awsについて初心者エンジニアに向けて、aws fsxをセルフマネージドadで起動する際に発生する、establishエラーについて解決方法をお伝えします。

## aws fsxとは

aws fsx（amazon fsx for windows file server）は、windowsベースのファイル共有サービスです。aws上でfile serverを構築することができます。fsxを使用することで、windowsベースのアプリケーションのファイルストレージや数据バックアップをクラウド上で行うことができます。

## aws fsxでセルフマネージドadに接続する手順

aws fsxをセルフマネージドadとして起動するためには、以下の手順が必要です。
1. microsoft ad（管理者アカウント）を起動
2. セルフマネージドadを作成
3. セルフマネージドadにamazon ec2インスタンスを参加させる

このセルフマネージドadの作成過程で、以下のエラーが発生することがあります。

### エラーメッセージ
```
file system creation failed. amazon fsx is unable to establish a connection with your microsoft active directory domain controller(s).
this is because the organizational unit you specified either doesn't exist or isn't accessible to the service account provided. to fix this problem, delete your file system and create a new one specifying an organizational unit
 to which the service account can join the file system
 as recommended in the amazon fsx user guide: https://docs.aws.amazon.com/fsx/latest/windowsguide/self-manage-prereqs.html.
```
### エラーメッセージの解釈
「aws fsxが、microsoft active directoryドメインコントローラと接続できません」という内容のエラーです。ドメインコントローラとの接続に失敗した原因は、「指定された組織単位が存在しないか、サービスアカウントがアクセスできないためです。」と説明しています。
そのため、ファイルシステムを削除し、新しい組織単位を指定してfsxを作成する必要があります。

## 対処方法

エラーメッセージの指示通りに、再度fsxの作成をお試しいただけますか。以下は作成手順です。

まず、fsxの設定に進みます。
1. fsx windows managementコンソールを開く
2. 設定マネージャを選択
3. ファイルシステムの作成を選択
4. active directory joinにチェックを入れ、microsoft adまたはセルフマネージドadを選択
5. 指定された組織単位の選択：あなたの選択を行わない場合は、リクエストされたプレフィックスを使用してad組織単位が自動的に作成されます。
6. 管理者資格情報でjoinユーザー名、パスワードを設定
7. ストレージ容量、vpc、サブネット、securitygroup、dns名前解決等、その他必要な項目を入力
8. fsxを作成する

組織単位が指定されていることを確認するよう指示しています。組織単位の指定は必須です。また、joinアカウントは組織単位に参加する権限を持つ必要があります。

エラーメッセージの詳細については、以下のaws公式ドキュメントが参考になります。
[aws fsx user guide 自己管理の実行条件](https://docs.aws.amazon.com/fsx/latest/windowsguide/self-manage-prereqs.html)

>本ブログは、aws fsxについての基本的な内容を扱います。専門的な詳細については、公式ドキュメントをご確認ください。

以上で、aws fsxをセルフマネージドadで使用しようとする際に生じるエラー「establishエラー」について解決方法をご紹介しました。

　

## AWS 関連のまとめ
https://hack-note.com/summary/aws-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

