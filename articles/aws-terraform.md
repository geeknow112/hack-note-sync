AWS Terraform
AWS,Terraform
aws-terraform

知りたかったlaC実践術
---1-Terraform
特集
ではじめる。 AWS構成管理
インフラを自動で構築&コードで管理
Terraformの世界へ」
ようこそ!
リソース作成/更新/削除の
流れをつかもう TheD野村 友規のむらともき)
p.18
Terraformで作る
AWS環境
コーディングによる。 インフラ構築を体験 Cha森茂 洋(もりしげひろし)
p.26
30 チームでTerraformを 活用していくには
環境差異を抑え、 CI/CDへ導入しよう Authの深 さかざわしゅん)
140 Terraform運用の Tipsとハマりどころ
コードの最適化と
管理のコツ Ch星川 真麻ほしかわまお).46
Amazon Web Services(AWS)をはじめ、クラウドサービスはITインフラの構築を劇的に便利にしました。ただ、インフラの管理 が不要になったかというとそうではなく、サーバ、DB、ネットワークなどさまざまなリソースの面倒をみなければいけないことに変わり はありません。システムが複雑になればリソースも増え、端末や専用の管理画面だけでは管理が追いつかないこともあるでしょう。
宣言的なコードでインフラを構築・管理できるオープンソースの Infrastructure as Code(lac) ツールで、とくにクラウドサービスのリソースを扱うことを得意としています。特集ではAWSを例に、Terraformによるインフラ管理 の流れ、AWS環境構築の手順、チームでTerraformを使っていくための機能、効率的な運用のためのTips を紹介します。 Torraformでどれだけインフラ管理が楽になるか、ぜひ体験してください。


----

知りたかった1ac実践術
=101m Terraform 営編成管理
インフラを自動で構築&コードで管理)
Terraformの世界へ
ようこそ!
リソース作成/更新/削除の、
流れをつかもう
Arthum 野村 友規(のむらとした Twitter @tmknom URL https://nekunemateablog.com
Intrastructure as Code(lac)は難しく思われがちですが、 Terraformのコードは読みやすく、コマンドの操作もシンプルです。 また採用実績も多く、情報も豊富です。本章でTerratormによ るリソース作成/更新/削除のワークフローを体験して、laC実 践の第一歩を踏み出しましょう。
---
Terraformとは
Terraformはインフラストラクチャを安全か つ効率的に管理するツールです。いわゆる Infrastructure as Code(IaC)を実戦でき、宣言 的にコードを記述します。
IaCではインフラストラクチャの構築・運用 に、ソフトウェア開発のベストプラクティスを 導入可能です。バージョン管理やコードレ ビュー、CI/CDなどを活用し、高品質で変化に 強いシステムの構築をサポートします。また、 Terraformの利点として、変更前に何が起きる か確認できる点は特筆すべきでしょう。実環境 へ変更を反映する前に、本当に変更してよいか 判断する機会が与えられるため、開発者は安心 してシステムを変更できます。
なんとなく1aCは難しそうという印象を持っ ている人もいるでしょう。しかしTerraformを 使えば「作って壊して」が簡単にできるため、実 はインフラストラクチャ自体の学習にも有用で す。採用企業が多いため、日本語のナレッジも たくさん見つかります。また、英語ですが公式 ドキュメント1も読みやすく、情報収集しやす い環境が整っています。 そして何より強調したいのは、Terraformの
#1) https://www.terraform.io/docs/
---
ポテンシャルと楽しさです。Terraformからイ ンフラストラクチャを操る全能感は格別な体験 です。まだTerraform を触ったことがなければ、 本特集はあなたのために存在します。この機会 に、ぜひ一緒にチャレンジしましょう!
Terraformo ワークフロー
Terraform lă AWS. Google Cloud Platform, Microsoft Azureなどの主要パブリッククラウ ドに対応しています。またGitHub、Datadog、 PagerDutyなど、ソフトウェア開発やシステム 運用でよく使われる多数のサービスにも対応し ています。各種サービスが提供するAPIを Terraform から実行でき、複数のサービスを統 一的に運用できます。
Terraformでは、次のようなワークフローで インフラストラクチャを管理します。
1.コードを書く 2. 変更内容を確認する 3.実環境へ変更を反映する
本特集ではサンプルコードやコマンド実行例 がいくつも登場します。そこでお勧めしたいの が、実際に手を動かしながら読み進めることで す。手元で実行してみるといろいろな発見があ ります。第1章のサンプルコードはGitHubまで #2) https://github.com/tmknom hello-terraform
---

公開しているので、こちらもご活用ください。
それではインストールからはじめて、さっそ くTerraformを体験してみましょう。
Terraformの、 インストール
Terraformのインストールには、各種OSの パッケージ管理ツールが手軽です。たとえば macOSであれば、次のように Homebrewでイン ストールできます。
$ brew install hashicorp/tap/terraform
WindowsやLinuxでも同様に、パッケージ管 理ツールを経由してインストールできます。ま たマニュアルインストールも可能で、パイナリ ファイルをダウンロードしてPATHに通せば動 きます。詳細は公式のインストールドキュメン ト3を参照しましょう。 インストールしたらバージョンを確認します。
$ terraform --version Terraforn v1.0.11
本特集ではAWSを題材にします。そこで TerraformからAWSを操作できるよう、クレ デンシャルを設定します。
クレデンシャルの設定
まずはAWS CLIをインストールします。 次にAWSマネジメントコンソールから 「Administrator Access」ポリシーがアタッチされ たアクセスキーを払い出します。
そしてaws configureコマンドを実行し、 先ほど払い出したアクセスキーを入力します (図1)。
注3) https://earm.hashicorp.com/tutorials/terraform/install
di
注4)https://docs.aws.amazon.com/ja_jp/cli/latest/
userguide/ 5) https://docs.aws.amazon.com/ja_jp/1AM/latest/User
Guide/id_credentials_access-keys.html
---

▼図1 アクセスキーとデフォルトリージョンの設定
$ aws configure AWS Access Key ID [None]: XXXXXXXX AWS Secret Access key [None]: XXXXXXXX Default region nane [None]: ap-northeast-1 Default output format [None.):
また、デフォルトリージョンには東京リージョ ン(ap-northeast-1)を指定します。
最後にaws sts get-caller-identity コ マンドを実行します。
S aws sts get-caller-identity
これでエラーにならなければクレデンシャル は正しく設定できています。またこの時点で AWS CLIと同様に、Terraformも設定したク レデンシャルを認識してくれます。
なお、AdministratorAccess ポリシーは強力 な権限です。クレデンシャルの管理にはくれぐ れも注意しましょう。
コードの実装
クレデンシャルを設定したら、次は実装です。 適当なディレクトリへ移動し、main.tfファイル を作成します。
Sakdir hello && cd hello Stouch main.tf
main.tfファイルをエディタで開き、リスト1 のように実装します。
リスト1はEC2インスタンスを作成するコー ドです。このコードは HCL(HashiCorp Configuration Language)という言語で記述され ています。まだ何も説明していませんが、なん となくコードの意味が理解できるのではないで しょうか。HCLでは構築手順ではなく、楽し たいものは何かを記述します。構築手順はTerra form が自動的に調整し、正しい手順で実行して くれます。 リスト1は2つのブロックで構成されています。
---

マリスト1リソースとプロバイダの定義
VE2 Terraform 0716
$ terraforn init
resource "aws instance" "hello" { ami
= "ami-0701e21c502689c31" instance_type = "t2.micro"
Initializing the backend...
provider "aws" {
region = "ap-northeast-1"
Terraforn has been successfully initialized!
V3 #TMBOHE
$ terraform plan
Terraforn will perform the following actions:
#aws_instance.hello will be created + resource "aws_instance" "hello" { + ami
= "ami-6701e21c502689c31" + instance_type = "t2.micro" + availability zone = (known after apply)
Plan: 1 to add,
to change, 0 to destroy.
---

最初は resourceブロックです。resource ブロック にはEC2インスタンスのようなリソースを定義し ます。リスト1ではAMI(Amazon Machine Image) にAmazon Linux 2(ami-0701-21c502689c31)、 インスタンスタイプにt2.microをそれぞれ指定し ています。
次のproviderプロックでは、クラウドプロバ イダの設定を記述します。リスト1ではデフォル トリージョンに東京リージョン(ap-northeast-1) を指定しています。
なお以降のコードでは誌面の都合から providerプロックを割愛しますが、常に記述す ることをお勧めします。そうすると実行環境に 依存せずリソースを操作でき、余計なトラブル を防止できます。
リソースの作成
コードを実装したら、いよいよTerraformの 実行です。ここではリスト1のコードを使って、 AWSを操作します。 なおTerraformは、main.tfファイルを作成し
---

たディレクトリで実行します。別のディレクト リで実行してもエラーになるため注意しましょ
あ、初期化
Terraformでは最初に初期化が必要です。図 2のように terraform init コマンドを実行し ましょう。するとAWSの操作に必要なバイナ リファイルをダウンロードします。 「これで下準備は完了です。
おかわに実行内容の確認
次にterraform plan コマンドを実行し、こ れから何が起きるか確認しましょう(図3)。
何やらたくさん出力されますが、よく見ると リスト1に基づいてami Pinstance_typeが設定 されています。また「+」マークとともに、aws_ instance.hello will be createdのようなメッ セージも出力されます。これは「新規リソース作 成」を意味します。
このようにTerraformでは実環境を変更する 前に、実行内容を把握できます。変更前という
---

▼84 実行内容の最終確認
$ terrafore apply
Plan: 1 to add, 0 to change, 0 to destroy.
Do you want to perform these actions?
Terrafore will perform the actions described above. Only 'yes' will be accepted to approve.
Enter a value:
▼四5実環境への反映
Enter a value: yes
ws_instance.hello: Creating... avs_instance.hello:Still creating... [10s elapsed] aws_instance.hello:Still creating... [20s elapsed] ONS instance.hello: Creation complete after 22s Cid 1-2cccófef03c6781)
Apply conplete! Resources: 1 added,
changed,
destroyed.
▼図6 EC2インスタンスの作成
0
Nameマ
インスタンス ID 1.02ccc6fef03c6781ea
インスタンス... の実行中 @a
インスタンス... t2.micro
ステータスチェ... 02/2 のチェックに
---

のがミソです。いきなり実行するのではなく、 開発者が確認するステップを挟むことで、安全 なシステム運用を可能にします。 さらに、実環境への反映
ここまでで問題がなければ、実際に反映しま す。使うのは terraform apply コマンドです。 実行すると、図4のようにあらためて図3と同 様の実行内容が表示され、本当に反映して問題 ないか最終確認が行われます。
「Enter a value」と表示されたら、図5のよう に yesと入力しましょう。するとEC2インスタ ンスが作成されます。
Apply complete!と表示されれば成功です。併 せて AWSマネジメントコンソールでも確認し ましょう。
図6のように表示されていれば完璧です。こ れであなたも無事Terraformデビューを果たし ました。今こそ祝杯をあげるときです。
---

Terraformの世界へようこそ!
リソースの更新
祝杯をあげて少し余韻に浸ったら、作成した EC2インスタンスを変更してみましょう。
あさこにリソースの設定変更
リスト1のresource ブロックをリスト2のよ うに変更します。変更点は tagsの部分です。見 てのとおりName タグを追加しています。
マリスト2Nameタグの追加
resource "aws_instance" "hello" { ami
="ani-0701e21c502689c31" instance_type%3D"t2.micro"
tags = {
Nane = "hello"
---

▼図7 リソース設定変更の確認
S terraform plan
Terraforn will perform the following actions:
Waws instance.hello will be updated in-place resource "aws instance" "hello" { id
= "1-02ccc6fef03c6781e" tags
%3D + "Nane" = "hello"
Plan:0 to add, 1 to change, 0 to destroy.
▼図8 リソース設定変更の反映
S terraforn apply
Enter a value: yes
avs_instance.hello:Modifying... Kid=i-02ccc6fef03c6781e] aws_instance.hello: Modifications.complete after 2s[id=i-02ccc6fef05c678101
Apply complete! Resources:
added, 1 changed, 8 destroyed.
¥89 EC2インスタンスへタグを追加
Name hello
イ ンスタンス ID 1 02ccc6terf03c67a1e
インスタンス... マ
M e
インスタンス... t2.micro
ステータスチェ... 02/2のチェックに。
の
---

図7のようにterraform plan コマンドを実 行し、変更点を確認します。
図7では「+」マークが先頭に付いていた行が 「~」マークに変化して、aws_instance.hello will be updated in-placeのようなメッセージが出力 されています。これは「既存リソースの変更」を 意味します。
注目したいのは、Terraformは先ほど作成し たEC2インスタンスを正しく認識している点で す。そしてコードと実環境の状態を比較して、 差分のみ変更します。そのためここではName タグの追加が予告されています。では terraform apply コマンドを実行します(図8)。
AWSマネジメントコンソールで確認すると、 図9のように Name タグが追加されています。
---

ここにリソースの再作成 別のパターンも試してみましょう。今度はリ スト2のresourceブロックをリスト3のように 変更します。変更点は amiの部分です。少しわ かりづらいですが、Amazon Linux 2(ami-0701 e21c502689c31) 5 Ubuntu (ami-Odf99b3a834 9462c6)へAMIを変更しています。
マリスト3 AMIの変更
resource "aws_instance" "hello" ani
13"ami-0df99b3a8349462c6" instance_type = "t2.micro"
tags = {
Name = "hello"
---

V10 W-
OHJE
S terrafora plan
Terraform will perform the following actions:
W aws_instance.hello must be replaced -/ resource "aws instance" "hello" {
= "ani-2701e21c502689c31" -> "ani-Odf99b3a8349462c6" N forces replacement availability_zone = "ap-northeast-1a" -> (known after apply
ani
Plan: 1 to add,
to change, 1 to destroy.
▼図11 リソース再作成の反映
$ terraform apply
Enter a value: yes
ws_instance.hello: Destroying... Cid=1-02cccófef03c6781e] ONS instance.hello: still destroying... Cid=1-02cccófef83c6781e, 10 elapsed aws instance.hello: Still destroying... Cid=1-2cccófef03c6781e, 2os elapsed) aws_instance.hello: Destruction complete after 29s ws_instance.hello: Creating... ws_instance.hello: Still creating... [10s elapsed] aws_instance.hello: Still creating... (20s elapsed aws instance.hello: Creation complete after 22s Cid=1-03feel98f12ffb28a)
Apply complete! Resources: 1 added,
changed, 1 destroyed.
---

それでは terraform plan コマンドを実行し ましょう(図10)。
今度は「-/+マークが付き、aws_instance. hello must be replacedのようなメッセージが出 力されます。これは「既存リソースを削除し、新 規リソースを作成する」という意味です。
シレッと出力されますが、このメッセージは 要注意です。この変更はリソース削除を伴いま す。つまりシステムの構成しだいではサービス ダウンを引き起こします。コードの修正は1行 ですが、Nameタグの追加とはまったく異なる 挙動を予告しています。
ここでワンポイントアドバイスです。terra form plan コマンド実行時には、最後に出力さ れる「N to destroy」の部分を必ず確認しましょ う。Nの部分にゼロ以外が入っていたら要チェッ クです。どのリソースが削除されるのか、サー
---

ビスに影響は出るのか念入りに確認します。
またplan結果をよく見るとamiの部分には、 forees replacementというメッセージも出力さ れています。このメッセージから、AMI IDの 変更が再作成の要因だと判断できます。
ここでは我々しか影響を受けないので、気に せず terraform apply コマンドを実行します (図11)。
すると最初に既存のEC2インスタンスが削除 され、次に新しいEC2インスタンスが作成され ました。terraform plan コマンドが予告した とおりの振る舞いです。
AWSマネジメントコンソールでも確認しま しょう。図12のように最初のEC2インスタン スが削除され、新しいEC2インスタンスが立ち 上がっています。
---

▼図12 EC2インスタンスの再作成
ステータスチェ...
Nameマ hello
インスタンス ID 1-02ccc6fef03c6781e 1-03fee098f12ffb28日
インスタンス... インスタンス...マ
終了済み@ 12.micro の実行中の9t2.micro
1
hello
2
/2 のチェックに!
be destroyedのようなメッセージが出力されま リソースの削除
す。これは「リソース削除」を意味します。
またterraform apply コマンドと同様に、本 せっかく作成したEC2インスタンスですが、 当に削除していいか確認されます。名残惜しい 削除しましょう。 terraform destroy コマン ですがyesと入力します(図14)。 ドを実行します(図13)。
最後にAWSマネジメントコンソールを確認 「-」マークとともに、aws_instanee.hello willし ます。すると図15のようにEC2インスタン
---

▼図13 リソース削除の確認 $ terrafora destroy Terraforn will perform the following actions:
#aws_instance.hello will be destroyed - resource "aws instance" "hello" { - ani
= "ani-8df99b3a8349462c6" -> null - availability_zone = "ap-northeast-1a" -> null
Plan:
to add,
to change, 1 to destroy.
Do you really want to destroy all resources?
Terraform will destroy all your managed infrastructure, as shown above. There is no undo. Only 'yes' will be accepted to confirm.
Enter a value:
14 W-HOW
Enter a value: yes
Bws instance.hello: Destroying... Cid 1-03feel98f12ffb28a) aws instance.hello: Still destroying... Cid=1-03fee898f12ffb28a, 10s elapsed) aws instance.hello: Still destroying... Lid=1-03fee898f12ffb28a, 2es elapsed) aws_instance.hello: Destruction complete after 28s
Destroy complete! Resources: 1 destroyed. ..M..)
V 15 EC21223220
ステータスチェ...
Name hello hello
インスタンス ID 1-02 ccclef03c6781e 1-03fee8f2fb28
インスタンス...
#723 @ * * Qe
インスタンス...
2.micro t2.micro
---

スが削除されています。
コードを整える
一般的なソフトウェア開発と同様に、Terra formでも読みやすさは大切です。ここでは簡単 に実践できるテクニックを2つ紹介します。
このコードをフォーマットする
Terraformではコードフォーマット機能が標 準提供されています。terraform fmt コマンド を実行しましょう。するとコードの見た目を整 えてくれます。-recursive オプションを付け れば、サブディレクトリ配下もフォーマットさ れて便利です。
$ terraform fmt -recursive
あそこにファイルレイアウトを整える14 しかし
本章では main.tf というファイル名を使用しま した。しかしTerraformでは拡張子が「tt」であ れば、ファイル名を自由に付けることが可能で す。またTerraformはカレントディレクトリの tf ファイルをすべて読み込みます。
そこでコードが長くなってきた場合はファイ ルを複数に分割し、適切なファイル名を付けま しょう。これだけでコードの見通しがよくなり ます。
ceum
不要なリソースは放置しない
個人の学習用途で作成したリソースは、不要 になった時点で削除しましょう。作成したリソー スをそのまま放置すると、AWSのような従量課 金サービスでは、意図せぬ請求につながります。 あらためて作りなおすこともTerraformなら簡単 です。いらなくなったらこまめに消す、これが Terraform学習の黄金律です。
---

クレデンシャルを守る。
Terraformに限らず、IaCでは強力な権限を 持つクレデンシャルの使用頻度が高くなりがち です。本特集でも Administrator Access ポリシー を使用しています。そのため、クレデンシャル の扱いには注意が必要です。
実装したコードはすべてバージョン管理すべ きですが、クレデンシャルは例外です。うっか りクレデンシャルをコードへ川め込んでしまい、 そのままGitHubなどで公開してしまうと危険で す。第三者にクレデンシャルを不正利用されて クラウド破産してしまう、という事例はいく つも存在します。
この問題を防ぐため、ツールを導入しましょ う。候補はいくつか存在しますが、手軽なのは 「git-secrets7」です。git-secretsを導入すると、 コードにアクセスキーが含まれていないかチェッ クできます。いつもどおりGitを使えばコミッ ト時に自動チェックされるため、絶大な効果が あります。
まとめ
第1章ではTerraformのインストールにはじ まり、基本的なワークフローを一通り体験しま した。第2章からはより踏み込んでTerraform の使い方を学びます。 またTerraformをもっと学びたくなった場合 は、拙著「実践Terraform』がお勧めです。ECS Fargateなどの本格的なシステム構築や、本番 運用を前提にした知見が凝縮されています。手 前みそですが、日本語で書かれたTerraform本 では定番の1冊です!50
注6)クラウド破産とはクラウドサービス利用者が「意図せず の調求される」ことを指す俗語です。
7) https://github.com/awslabs/git-secrets 注8)野村友規インプレスR&D、2019年
https://nextpublishing.jp/book/10983.html
---

## AWS 関連のまとめ
https://hack-note.com/summary/aws-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

