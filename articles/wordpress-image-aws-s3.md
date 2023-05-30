【解説】wordpressの画像をAWS S3に置く方法
wordpress,aws,s3
wordpress-image-aws-s3

こんにちは。今回は、wordpressについて初心者エンジニアに向けて、aws s3に画像を置く方法について解説します。

## aws s3とは？

aws s3とは、amazon web services(aws)のオブジェクトストレージサービスです。aws s3を利用することで、大量のデータやファイルを安全に保管することができます。また、クラウド上にデータを格納することで、耐久性や可用性が高くなるため、安心して利用することができます。

## wordpressの画像データの格納先

wordpressは画像ファイルを「wp--content/uploads/」ディレクトリ内に保存します。このディレクトリに格納された画像は、ローカルサーバー上に保存されます。しかし、この方法では、webサイトにアクセスするたびに画像ファイルを送信する必要があり、サイトの表示速度が低下する原因となってしまいます。

そこで、aws s3とwordpressを連携させることで、画像ファイルをaws s3に格納することができるようになります。この方法であれば、サイト表示速度が向上することが期待できます。

## wordpressの画像データを移行するには

wordpressの画像データをaws s3に移行するためには、awsマネジメントコンソールから、s3バケットを作成する必要があります。その後、aws s3とwordpressを連携させるプラグインをインストールすることで、画像ファイルをaws s3に送信することが可能になります。

## おススメのプラグイン

wordpressとaws s3を連携させるためには、以下のプラグインがおすすめです。

1.aws s3 offload media

aws s3 offload mediaは、wordpressの画像ファイルをaws s3に移行することが可能なプラグインです。aws s3 offload mediaを利用すれば、wordpressの投稿ページ内で画像をアップロードすると、自動的にaws s3にアップロードされるようになります。

2.media cloud

media cloudは、aws s3だけでなく、google cloud storageやmicrosoft azureといったクラウドストレージサービスとwordpressを連携させることができるプラグインです。また、クラウドストレージサービスとwordpressとの同期機能も搭載しており、手動でファイルを送信する手間を省くことができます。

以上、wordpressの画像をaws s3に置く方法について解説しました。aws s3を利用することで、wordpressのサイト表示速度を向上させることができるため、是非利用してみてください。

## wordpress + AWS の勉強をしたいならこちらもおススメ
- [TechAcademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3A%2F%2Ftechacademy.jp%2Fhtmlcss-trial%3Futm_source%3Dmoshimo%26utm_medium%3Daffiliate%26utm_campaign%3Dtextad)
- [オンラインスクール DMM WEBCAMP PRO](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=ON)

【参考記事】
- [wordpress画像をamazon s3で管理する方法](https://globaleffect.me/how-to-upload-wordpress-images-to-amazon-s3/)
- [wordpressとaws s3を連携させてサイト表示速度をupしよう！](https://www.tt2-works.com/wordpress-aws-s3/) 


## Wordpress案件を実際に取っていく方法をまとめました
プロのエンジニアになるには、独学を続けるより案件を実際に受注した方が近道です。
フリーランスエンジニアとしてやっていくにはどこかのタイミングで
案件を獲っていかないといけません。
最初から全てうまくいくことは稀でしょう。
となると、うまくいかないことを前提として最速で案件を回していった方が効率的です。

スキルを磨く勉強はほどほどにして、いかにして案件を獲っていくかを考えましょう。

https://hack-note.com/programming/engineer-freelance-wordpress/

