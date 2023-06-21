【基礎】aws msadとは？active directoryを簡単に使うには
aws,msad,active-directory,簡単,手順
aws-msad-about

こんにちは。今回は、awsについて初心者エンジニアに向けて、aws msadについて解説します。aws msadは、microsoft active directoryのクラウドサービス版であり、aws環境内での認証やアクセス制御を管理することができます。ここでは、aws msadの概要や簡単に使うための手順について紹介します。

## aws msad とは？

aws msadは、amazon web services（aws）が提供するmicrosoft active directory（以下、ad）のクラウドサービス版です。aws環境内で、windows ec2インスタンスやrdsなどのサービスに対して、adでの認証やアクセス制御を簡単に行うことができます。また、既存のオンプレミス環境のadとの連携も可能です。

## aws msadの料金は？

aws msadの料金は、利用量に応じて変動します。主な料金は以下の通りです。

- ディレクトリの作成：無料
- 標準ドメインコントローラーのインスタンス料金：$0.056/hour
- 小さいサイズのドメインコントローラーのインスタンス料金：$0.033/hour
- ストレージの使用料：$0.20/gb-month

詳細な料金については、aws公式サイトを参照してください。

>aws msadの料金は、使わない場合でも発生する場合があるため、注意が必要です。また、adの同期やユーザー管理などの機能が利用できるため、利用量によっては費用が高額になることもあります。料金については、必ず事前に確認しておきましょう。

## aws msadとactive directoryでできることの違い

aws msadは、adのクラウド版であるため、一部機能が制限されています。制限される主な機能は以下の通りです。

・gpoの管理が制限される
・ドメインの機能レベルが2008 r2に制限される
・active directory federation services（adfs）の機能が制限される

しかし、aws msadは、aws内で利用できるため、高可用性や耐久性、スケーラビリティなどのメリットがあります。また、aws独自の機能であるaws directory serviceやaws single sign-onとの連携も可能です。

## 使用上の注意点

aws msadを利用する際には、以下のような注意点があります。

・最新バージョン（2012 r2以降）のldapプロトコルを使用する必要がある
・ipv6には対応していない
・active directory-integrated dnsをサポートしていない

また、aws msadを利用する上で必要な手順は以下の通りです。

1. ディレクトリの作成
2. ドメインコントローラーの作成
3. オンプレミスadとの連携（必要に応じて）
4. ec2インスタンスなどの接続確認

詳細な手順については、aws公式ドキュメントを参照してください。

>aws msadは、クラウド上でadを利用することができるため、管理負荷が軽減されるメリットがあります。しかし、料金や利用制限などに注意が必要です。また、正しく利用するためには、手順を正確に把握しておくことが重要です。

参考url：
- aws公式ドキュメント「aws directory service for microsoft active directory」：https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html
- qiita「aws microsoft ad（managed ad）の料金を1ヶ月実測してみた」：https://qiita.com/ohsawa2268/items/303e5a7d54b0a8425b07

　

## AWS 関連のまとめ
https://hack-note.com/summary/aws-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

