Github Actions CI/CD
github,CI/CD
github-actions-for-cicd

開発作業を効率化し、負担を減らすために、CI/CDの導入は重要なツールです。この記事では目の前の作業に追われ、重要とわかっていてもなかなか導入できていない人を対象に、GitHub ペースの CI/CDツール「GitHub Actions」を使ったCI/CDの始め方を説明します。マスターして開発速度向上を目指しましょう！

https://hack-note.com/programming-schools/

<!-- CI/CDとGitHub Actions の概要を紹介し、ハンズオン形式でCI/CDパイプラインの作り方を解説します。 -->
<!-- さらに、本格導入したい人向けの発展的な使い方も取り上げます。本特集で、時短開発の第一歩を踏み出しましょう。 -->
<!-- なお、本特集のサンプルコードは https://github.com/yokawasa/software-design-github-actions-samples からダウンロードできます。-->

# 第1特集 ここから始める時短(開発)
## GitHub Actions で簡単・快適CI/CD
### GitHubベースの高機能な自動化ツールを体験しよう

1. CI/CDEFGitHub Actionsをオススメする理由
豊富な機能と拡張性を兼ね備えた次世代自動化ツール
2. GitHub Actionsによる自動化を体験
ビルドテストデプロイを行うCI/CDバイプラインを構築
3. さらに自動化を進めるために知っておきたいこと
開発フローやタスク実行をすべてGitHubで効率化

---
ここから始める時短開発
GitHub Actionsで簡単・快適CI/CD
GitHubベースのIT高機能な自動化ツールを体験しよう

# CI/CDにはGitHub Actionste オススメする理由
豊富な機能と拡張性を兼ね備えた次世代自動化ツール
第1章では、GitHub Actions を利用するうえで押さえておきたい基礎事 項を解説します。CI/CDの定義を取り上げ、GitHub Actionsの概要、 主要概念、そしてGitHub Actionsの始め方を説明します。実際の使 い方を学ぶ前にまずは基礎をしっかり固めましょう。

---
## CI/CDとは何か、なぜCI/CDが必要なのか
CI/CDとは、それぞれ
- Continuous Integration (継続的インテグレーション)
- Continuous Delivery(継続的デリバリー)もしくはContinous Deployment(継続的デプロイメント)を合わせた 用語です。

CIはコードの変更を起点にコードの静的分析、ビルド、テストなどを自動実行することを意味します。

一方、CDはコードやビルドされた成果物をプロダクトへ自動反映させることを意味します。

CI/CDは、このCIとCDを組み合わせて、一連のソフトウェア開発のライフサイクルにおける処理を自動化することを指します。

これにより、テストやリリース作業から属人性を排除し、人間に起因するミスが防止されます。

そして、その結果、品質が担保され、コード更新からプロダクト反映までのリードタイムの短縮化もできます。

CI/CDは、開発、テスト、リリースというサイクルを回して市場への継続的な価値の提供を目指す、DevOpsの文原でよく話に登場してきますが、まさに、DevOpsの実践に不可欠な手法と言えます。

---
## GitHub Actionsとは?
### GitHub Actionsの概要
GitHub Actions は、コードのビルド、テスト、パッケージ、リリースなどソフトウェア開発の ライフサイクルにおけるワークフローの自動化、 迅速化を可能にするCI/CDサービスです。2019 年11月に正式版がリリースされたばかりで、ほ かのCI/CDツールと比較すると歴史が浅いもの です。しかし、急速に進化を続けており、シン ブルかつ豊富な機能と拡張性、そしてGitHub と の親和性の高さという利点もあって、リリース 以来、多くのユーザーの支持を得ている次世代 自動化ツールと言えます。なお、本稿に記載し た内容は2021年12月時点の情報です。
GitHub Actionsの代表的な特徴に次のような ものがあります。
・GitHubとの親和性:自動化されたワークフ
ローをGitHubリポジトリに直接作成可能 ・豊富なジョブ実行環境の選択肢:Linux、 macOS、Windows それぞれの仮想マシンが GitHubホストで提供されており、仮想マシン 上のDockerコンテナ内でも直接実行可能 ・豊富なワークフローの実行トリガー:リポジ トリで発生するすべての操作イベントのトリ ガーが提供されており、スケジュール実行や 外部イベントをトリガーにしたワークフロー の実行も可能 ・充実した基本機能:シークレット情報を扱う ためのしくみ、ワークフローでのArtifact(成 果物)を保存・取得するしくみ、ワークフロー で利用する依存データをキャッシュするため

---

のしくみなどを提供 ・豊富なアクションの選択肢と充実したエコシ ステム:公開済みのGitHub公式アクション やコミュニティ提供のアクション、自分で作 成したアクションをワークフローで簡単に利 用可能
GitHub Actionsの利用料金
パブリックリポジトリや、後述するセルフホ ストランナーでの利用は無料です。
プライベートリポジトリの場合、ストレージ 使用量とジョブ実行時間が一定量まで無料で利 用可能な枠がありますが、それを超えると従量 課金となっています。この無料枠の量はアカウ ントの種類によって異なります。また、ジョブ 実行時間に対する従量課金は利用OSによって 時間あたりの課金額が異なります。Linuxを基 準とした場合、Windowsは2倍、macOSの場合 は10倍と差があるので注意が必要です。
・無料枠の例:GitHub無料アカウントの場合、
注1)参考リンク:GitHub Actionsの支払いについて URL https://docs.github.com/ja/billing/managing
billing-for-github-actions/about-billing-for-githubactions

---

ストレージは 500MBまで、ジョブ実行時間 は2,000分/月
なお、利用料金の把握は公式に提供されてい る料金計算ツールがあるので、そちらをご利 用ください。
## GitHub Actionsの主要概念
GitHub Actionsの主要コンポーネントと、自 ・動化用の一連の処理を定義するワークフローの 基本構造を紹介します。まず、図1がGitHub Actionsの全体の概略図です。

### イベント
ワークフロー実行のトリガーとなるアクティ ビティのことをイベント(図1の左上部)と呼び ます。GitHub Actionsはリポジトリで発生する 操作イベント(Webhook)をトリガーにワークフ ローを実行できます。また、リポジトリで発生 する操作だけでなく、スケジュールや外部イベ ントをトリガーにして実行したり、手動で実行 したりできます。GitHub Actionsで利用可能な
イベントの詳細は、GitHub 公式 ページ「Events that trigger work flows」をご参照ください。
なお、後述するワークフローを tion
定義するYAMLでは、onシンタッ クスを用いて、どのイベントをワー
クフローのトリガーとするのかを -b2
定義します。リスト1に示すYAML の例では、push イベントをトリガー
として定義しています。
## ワークフローと主要な構成コンポーネント
ワークフローと、ワークフロー
2)unner 30511)
3)URL https://github.com/pricing/
calculator URL https://docs.github.com/ja/
actions/learn-github-actions events-that-trigger-workflows

---
- リストワークフローYAMLの例
```
name: Test Workflow
on:
pushトリガー定番
jobs:
  "job_one:
    name: Job 1 Runner runs-on: ubuntu-20.04 steps: -name:Step1....
run: echo "cnd1" -name:Step2....
run.echo "cade... - name: Step 3
run: echo "cnd3" job_two:
name: Job 2 runs-on: macos-11
ステップ
Job 2
「定義
steps:
Runner
(.. ..)
```
を構成するジョブ、ステップについて、それぞ れのエッセンスを説明します。

### ワークフロー(Workflow)
図1の右に示す図が、ワークフローを表す概 念図です。ワークフローは、1つ以上のジョブ から構成され、1つのワークフローにつき、1つ のYAMLファイルを用意します。トリガーとな るイベントが異なる場合、ワークフローをそれ ぞれ用意します。

### ジョブ(Job)
ジョブとは、1つ以上のステップから構成さ れるタスクの定義です。ワークフローを定義す るYAMLでは、jobsシンタックス下に定義しま す。リスト1のYAMLの例では、job_one と job_ twoの2つのジョブを定義しています。ジョブ は後述するランナーと呼ばれるアプリケーショ ン内で実行されます。ジョブが分割されると、 それぞれ別のランナーアプリケーションインス タンスで実行されるため、ジョブ間のデータ共 有を工夫する必要があります。詳細は、第3章 「ワークフロー内のデータ共有」で解説します。

---

マリスト2ステップ定義例
jobs: sample_job:
runs-on: ubuntu-latest steps:
ステップ利用するアクションの定器 - uses: actions/checkoutav2 - uses: actions/setup-nodeav2 『ステップ:コマンドの定義(シングルライン】 - run: npm install ロステップ:コマンドの定義(マルチライン】 -run:
npmci npn build

### ステップ(Step)
ステップは、ジョブの中で実行される各タス クのことです。ワークフローYAMLではjobs.job_ id.stepsシンタックス下に個々のステップを定義 します(リスト2)。図1の右上部に示すとおり、 各ステップでは、コマンドもしくは後述のアク ションを実行できます。アクションは jobs.job_ id.stepsl".uses シンタックスで、コマンドはjobs, job_id.steps").run シンタックスで定義します。

## アクション(Action)
アクションは、ステップを構成する最小の構 成要素です。前述のとおり、jobs.job_id.steps", uses シンタックスで、各ステップで実行するア クションを指定します。
GitHub Actionsの特徴として、豊富なアク ションの選択肢と充実したエコシステムがあり ます。アクションは、独自に作成したものをワー クフロー内で使用したり、ほかのユーザーと共 有したりできます。また、コミュニティにより 作成・公開されているパブリックリポジトリの アクションを使用することもできます。また、 GitHub公式のアクションやマーケットプレイス に登録・公開されているアクションを利用し、 コマンドと組み合わせることで、たいていの自 動化処理を実現できます。
### アクションの種類
アクションは、3つの作成方法が用意されて

---

表1 アクションの作成方法
|アクションの種類|
|JavaScript アクション|
JavaScriptで記述する ・ランナー上で直接実行される
・言語制約:JavaScript(TypeScriptなどで記述し、その後JavaScriptにコンパイ | 
ルしても可) ・起動時間:ランナー上で直接実行するため、起動が速い。 ・利用可能なランナーOS:Linux.macOS、Windows
アクションの内容を Dockerコンテナとしてパッケージ化する ・ランナー上でコンテナを立ち上げて実行する。
・言語制約:なし(コンテナとしてOSごとパッケージ化するので、自由度が高い) 「Dockerコンテナアクション|
・起動時間:イメージをPull してからコンテナを立ち上げるため、JavaScript より
起動に時間がかかる ・利用可能なランナーOS: Linuxだけ
・複数ステップの処理をバンドルし、1つのアクションとして定義・実行する Composite アクション
|・利用可能なランナーOS:Linux,macOS、Windows
▼表2 利用可能なGitHub ホスト仮想マシンのYAMLラベル 仮想マシン
仮想マシンのYAMLラベル Ubuntu
ubuntu-latest, ubuntu-18.04. ubuntu-20.04 macOS
macos-latest, macos-11, macos-10.15 Windows Server
windows-latest.windows-2019_windows-2022.windows-2016

---

います。JavaScript アクション、Dockerコンテ ナアクション、Compositeアクションの3種類 です。それぞれの概要、特徴は表1のとおりで
独自アクションの作成方法は、本稿では紹介 しません。詳細は、下記の各GitHub公式ページ をご参照ください。
・JavaScript アクション - 「JavaScript アクショ
ンを作成する」 ・Docker コンテナアクション - 「Docker コンテ
ナのアクションを作成する#5」 . Composite 7792-[Creating a composite action*6]

## ランナー(Runner)
ジョブはランナーと呼ばれるアプリケーショ
4) URL https://docs.github.com/ja/actions/creating
actions/creating-a-javascript-action 5) URL https://docs.github.com/ja/actions/creating
actions/creating-a-docker-container-action (注6)(Dhttps://docs.github.com/ja/actions/creating
actions/creating-a-composite-action

---

ンにより実行されます。ユーザーは、実行環境 のホスティングモデルを2種類のランナーから 選択します。なお、ランナーは2019年にOSS として公開されています。

### GitHubホスト型ランナー
GitHubは、ジョブ実行環境として、ランナー がすでにインストールされた仮想マシンを提供 しています。この、GitHubがホスティングする 仮想マシンで実行されるランナーのことを GitHub ホスト型ランナーと呼びます。ユーザー はjobs.job_id.runs_on シンタックスで、どの仮 想マシンでジョブを実行させるのかをラベルで 指定します。リスト1の例では、GitHub ホスト 型ランナーを指定しており、Job 1 と Job 2でそ れぞれUbuntu 20.04(ラベル:ubuntu-20.04)、 macOS Big Sur 11(ラベル:macos-11)を指定 しています。
利用可能なGitHub ホスト仮想マシンと指定可 能なYAMLラベルを表2にまとめます。なお、
7) URE https//github.com/actions/runner

---

最新の情報はGitHub公式ページ「サポートされ ているランナーとハードウェアリソース」をご 参照ください。
また、GitHubホスト型の場合、ジョブ実行の たびにクリーンな仮想マシンインスタンスが提 供されます。料金は、GitHubプランの無料分を 超えると、分単位での従量課金となるので、ご 注意ください。

### セルフホスト型ランナー
ジョプはGitHub ホスト仮想マシン以外にも、 ・独自の環境で実行させることもできます。ラン ーナーを独自の環境にインストールしてGitHub Actionsと通信できるように設定することで、そ の環境をジョブ実行に利用できます。これは、 ジョブを実行するワーカー部分を自分の環境で 動かし、それ以外のすべてをGitHubに管理して もらう方式です。このように、独自環境で実行 されるランナーのことをセルフホスト型ランナー と呼びます。独自環境をジョブ実行に利用する おもなメリットとしては、ハードウェア、OS選 一択の自由度の高さや、ソフトウェア設定などの カスタマイズ性の高さが挙げられます。デメリッ トは、ランナーや仮想マシンの運用管理コスト がかかる点です。
セルフホスト型ランナーの詳細は「自分のラン ナーをホストする」をご参照ください。

## GitHub Actionsの始め方
GitHub Actionsの始め方を、順に説明します。
具体的な手順の説明に入る前に、ツールのUIをざっくり理解しておきましょう。

>8) URL https://docs.github.com/ja/actions/using-github
hosted-runners/about-github-hosted-runners#
supported-runners-and-hardware-resources 9) UND https://docs.github.com/ja/actions/hosting-your
own-runners

---

1. まず、GitHubま10上で任意のご自身のリポジ トリを選んでください。
2. すると、図2のように 「Actions」というタブが表示されるので、クリックします。
3. そのリポジトリで、まだ何もワークフローを作成していない場合は、図3のようなスターター 用テンプレート選択ページが表示されます。
4. ここで表示されるテンプレートは、リポジトリに アップされているコードで利用している言語によって自動的に選択されます。

なお、すでにワークフローを作成している場 合は、ワークフロー一覧ページが表示されます。 その際には、[New workflow]ボタンをクリック することで、同様のテンプレート選択ページが 表示されます。

5. テンプレート一覧ページにあるテンプ レートからどれか1つ選択してください。
6. 図4 の左側の領域のように、Webベースのワークフ ロー編集ページに遷移します。
なお、当然ながら、テンプレートを選択せずにワークフローを編集することも可能です。その場合は、図3の 上部にある「setup a workflow yourself」を選択 してください。

ワークフロー編集ページでは、図4の中央お よび右側のように、アクションの利用時に役に 立つスニペットを簡単に取得できます。
また、このページでは、マーケットプレイスに公開さ れているアクションから、キーワード検索で実 現させたいアクションを探しながら選ぶことも 可能です。

7. そして、ワークフローの編集が完了したら、 福集ページ上部にあるボタン[Start commit]を クリックします。すると、YAMLファイルがコミットされ、設定完了です。
注10) CD https://github.com/

---
テンプレートの YAMLはリポジトリ名/.github/workflows配下 に保存されます。
とても簡単にワークフローを設定できること をご理解いただけたかと思います。慣れてきた

---

方は、このようなスターターワークフローを使 うことなく、直接ワークフローマニフェストファ イルを追加してもよいでしょう。なお、次章以 降では、Starter-workflowからではなく、直接 ワークフローを追加する流れを解説します。

---

ここから始める時短開発
## GitHub Actionsで簡単・快適CI/CD
高機能な自動化ツールを体験しよう

## GitHub Actionsによる) : 自動化を体験
ビルドテスト・デプロイを行う CI/CDパイプラインを構築
第2章では、ローカルで作成したアプリケーションのビルドテストを行う。 ワークフローと、テストしたアプリケーションをコンテナレジストリにデプロ イするワークフローを作って、GitHub Actions によるCI/CDパイプライ ンの構築を体験してみます。

---

本稿では、次の2種類のバイブライン1を構 築します。
・CIパイプライン:簡単なGo言語アプリケー ションのビルドとテストを行う、単一ジョブ のワークフロー ・CI/CDパイプライン:Go言語アプリケーショ ンのテストをしたあとに、コンテナイメージ をビルドし、コンテナレジストリヘpushを行 う、複数ジョブのワークフロー
なお、本稿の実行環境は macOS 11. Go 1.17.1 です。

## CIパイプラインを構築する
### 事前準備
まずは、CIバイプライン構築のために必要な リポジトリとサンプルアプリケーションのファ イルを作成します。

#### リポジトリの作成
GitHubにテスト用のリモートリポジトリを作 成します。なお、すでにテスト用リボジトリを 作成済みの場合は、そのリポジトリ上で進めて いただいてもかまいません。
注1)パイプラインとは一連の処理ステップであり、GitHub
Actionsにおけるワークフローのことです。

---

まずはWebブラウザでGitHub2にアクセス し、ページ右上の[+]ボタンをクリックします。 すると、ドロップダウンメニューが表示される ので、図1のように[New repository]を選択し
次に、新規リポジトリ作成のために必要な情 報を求められます。[Repository name]にリポジ トリ名を入力し、[Create repository]をクリッ クしてください。これで、GitHub上にリポジト リが作成されます。公開範囲はデフォルトで [Private](非公開)になっているので、もし公開 したい場合は同入力ページの[Public]を選択し てください。

#### サンプルコードの用意
サンプルコードをリポジトリに反映します。 まずは、ローカルリポジトリを作成します。こ
2) URL https://github.com/
▼図1 ドロップダウンメニューで[New
repository]を選択する
New repository Import repository New gist New organization New project

---

▼図2ローカルリポジトリを作成する
ディレクトリの作成 $ skdir github-actions-cicd $ cd github-actions-cicd
ローカルリポジトリを新規作成] $ git init

---

こでは「github-actions-cied」というリポジトリ 名にします(図2)。
サンプルで利用するファイルgo.mod(リスト 1)、main.go(リスト2、main_test.go(リスト3) を、先ほどのローカルリポジトリのディレクト リに作成・配置します。
作成したサンプルファイルを、ローカルリボ ジトリにコミットします。
$ git add go.mod main.go main_test.go $ git comnit -m "first comnit"
リモートリポジトリを登録し、サンプルファ イルをリモートリポジトリに反映させます(図 3)。
以上で事前準備は完了です。作成したリポジ トリページに Webブラウザでアクセスすると、 登録したファイルが反映されていることを確認

## ワークフロー作成
GitHub Actionsのワークフローを作成してい きます。ローカルリポジトリの.github/work flows配下に、go.ymlというワークフローファイ ルを作成します(リスト4)。 このワークフローは、mainブランチへのpush

---

VUZ 1 go.mod module github.com/7572/github-actions-cicd
go 1.17

---

マリスト2
```
main.go
package main import "fnt" func Greeting()string {
return "Hello"
func main() {
fmt.println(Greeting)
マリスト3main_test.go
package main import "testing" func TestGreeting(t *testing.D) { want := "Hello" got %3D Greeting() if want != got {
t.Errorf("got % want X9", got, want)
```
をトリガーに実行され、リポジトリをチェック アウトし、Go環境のセットアップ、アプリケー ションのビルドとテストを行います。

## フロー実行
図4のように、ワークフローファイルをリモー トリポジトリの mainブランチに反映(push) しま す。ワークフローファイルでは、mainブランチ へのpushをトリガーイベントとして定義してい るので、このイベントでワークフローが実行さ れます。
リポジトリ名の下にある[Actions]タブをク リックすると、ワークフロー一覧ページに遷移

---

▼図3 リモートリポジトリを登録し、サンプルファイルをpushする
$ git branch - nain リモートの追加 soit remote add origin gitagi thub.com:アカウント名/github-actions-cicd.git,
ローカルにコミットされたサンプルファイルをリモートリポジトリに反映 $ git push u origin main

---

VUA
.github/workflows/go.yml
name: Go test
on: push: branches:
- main
jobs: build:
runs-on: ubuntu-latest steps: #リポジトリをチェックアウト - uses: actions/checkoutav2 # GOREY1727 - name: Set up Go
uses: actions/setup-go@v2 with:
go-version: 1.17 # GOU - DEIL - name: Build
run: go build -v ./... # テストの実行 - name: Test
run: go test -V./...

---

▼図4ワークフローファイルをリモートリポジトリにpush
する
ローカルリポジトリにワークフローファイルをコミット。 $ git add .github/workflows/go.yml Sagit commit -m "add GitHub Actions workflow"
リモートリポジトリにpush $ git push-u origin main
するので、今回新しく実行されたワークフロー をクリックします。すると、図5上のようなサ マリーページに遷移します。ここで、Jobs]ま たは視覚化グラフにあるジョブ名(ここでは build)をクリックすると、図5下の画面に遷移 します。このページでは、ジョブを構成する各 ステップの詳細を確認できます。
CI/CDパイプラインを 人構築する

---

複数ジョブで構成される ワークフローを構築します。 先ほど作成したリスト2を テストしたあとに、別の ジョブでコンテナイメージ をビルドし、コンテナレジ ストリにpushします。
・事前準備
今回のワークフローで は、コンテナイメージを Docker Hub 3 push L す。そのため、事前準備と してDocker Hubへのアク セスに必要なアクセストー クンの取得と、そのトーク ンのGitHubへの登録を行 います。また、コンテナイ メージ作成のためのDocker fileも用意します。
3) URL https://hub.docker.com

---

勝Docker Hubアカウントの用意と
アクセストークンの取得 Docker Hubに移動し、[Sign Up]ページ よりアカウント登録を行ってください。な お、すでにアカウントを持っている場合は、 そちらをご利用ください。
Docker Hubアカウントを作成したら、 Docker Hubにログイン後、[Account Settings]→[Security]ページより、アクセス トークンを作成してください。このトークンは、 Docker CLI LOV-15 Docker Hub 7 クセスする際に必要なものです。なおアクセス 権限(Access Permission)は[Read, Write, Delete]を選択してください。アクセストークン 作成に関する詳細は公式ドキュメントをご参 照ください。
アクセストークンをGitHubに シークレットとして登録 GitHub Actionsでは、トークンやパスワード などのシークレット情報を安全かつ簡単に扱え るしくみを提供しています。シークレットは、 リポジトリの[Settings]タブ→[Secrets]から股
4) URL https://docs.docker.com/docker-hub/access
tokens/

---

マリスト5 Dockerfile
FROM golang: 1.17.1-buster AS builder ARG VERSION=dev WORKDIR /go/src/app COPY main.go. RUN go build -o main main.go FROM debian:buster-slim COPY -- fron-builder /go/src/app/main /go/bin/nain ENV PATH="/go/bin:$CPATH" CMD ["main")

---

定できます。ここでは、
・アカウント名:DOCKER_USERNAME ・アクセストークン:DOCKER_PASSWORD
をシークレットとして登録します(図6)。
なお、設定したシークレット変数は、ワーク フローから5{ secrets.シークレット変数名 }} としてアクセスできます。
Dockerfile コンテナイメージを作成するためのDocker fileを用意します。ファイルの内容はリスト5の とおりです。
先ほどと同様に、Dockerfileをローカルリボ ジトリにコミットし、リモートリポジトリに反 映させます(図7)。

---

¥97 Dockerfileをリモートリボジトリにpushする
S git add Dockerfile S24git conmit -n "add Dockerfile".
ローカルにコミットされたDocker fileをリモートリポジトリに反映] $ git push-u origin main
|
ワークフロー構築
以上の手順で必要なファイルの用意ができた ので、ローカルリポジトリの.github/workflows 配下に、go-deploy.yml というワークフローファ イルを作成します(リスト6)。
リスト6のワークフローは、VN.N.N(N = 0~ (9)形式のバージョンタグによる push イベントを

---

トリガーに実行されます。
deploy ジョブは、jobs.job_id.needsシンタッ クスでtestを指定しているので、test ジョブの あとに実行されます(needsについての詳細は、 第3章「複数ジョブの実行パターン」で解説しま す)。 test ジョブにて、Go言語アプリケーショ ンのテストが通ったら、deploy ジョブでコンテ ナイメージをビルドし、コンテナレジストリ (Docker Hub)にpushします。
注5)リスト6で使用しているBuildKitはDocker18.09以降に組
み込まれており、有効化することでイメージを高速かつ安 全にビルドできるようになります。BuildKitを有効化したイ メージビルドに関する詳細は「auid images with Buildkit」 が参考になります。 UND https://docs.docker.com/develop/develop-images/
build enhancements/

---

Vu6
.github/workflows/go-deploy.yml
name: Go deploy on: push: tags:
- " *.*.*"
jobs: test:
runs-on: ubuntu-latest steps: - uses: actions/checkoutav2 - name: Set up Go
uses: actions/setup-goav2 with:
go-version: 1.17 - name: Test
run: go test -v ./...
deploy:
runs-on: ubuntu-latest 8 needs TASTE. Sccutesty 70XIT needs: test steps: ロリポジトリをチェックアウト - uses: actions/checkoutav2 # **-ZELKI BuildKits - name: Set up Docker Buildx
uses: docker/setup-buildx-actionav1 # 18-YDELFpush - name: Build and push Docker image run:
TAG=$(echo $GITHUB REF | grep - "[0-9][¥.).*") DOCKER_IMAGE=SCC secrets.DOCKER_USERNAME}}/greeting: STAG
docker login --usernane $CC secrets.DOCKER_USERNAME )) --password $CC secrets. 7 DOCKER_PASSWORD })
docker build -t $DOCKER_IMAGE. docker push $DOCKER_IMAGE

---

Docker Hubへのアクセスに必要なユーザー名 とアクセストークン情報は、ともにGitHubの シークレットとして管理しています。それぞれ ワークフローの中で、{{ secrets.DOCKER _USERNAME }}と { secrets.DOCKER_PASS WORD}}で値を参照しています。
そしてpush されたタグ名(U.N.N.N)からい以外 の部分を抜き出し、コンテナイメージタグとして 設定します。
ワークフロー実行
前述のとおり、ワークフローはvN.N.N(N =3 0~9)形式のバージョンタグによるpush イベン トをトリガーとしています。ここでは、v0.0.1

---

のイメージタグをpushし、ワークフローを実行 します。
$ git tag -a v0.0.1 -m "v0.0.1" $ git push origin v0.0.1
コマンドの実行後に、ワークフローの実行結 果を確認していきます。今回実行されたワーク フローのサマリーは図8上のようになっており、 test ジョブと deploy ジョブが直列に実行された ことがわかります。先ほどと同様に、ジョブ名 (ここでは deploy)をクリックすると図8下のよ うに、ジョブを構成する各ステップの詳細が確 認できます。50

---

ここから始めるの夏開発) 21a GitHub Actions Gi
01高機能な自動化ツールを プ で簡単・快適CI/CD 体験しよう。 030 
# 動化を進めるために 知っておきたいこと
## ローやタスク実行を すべてGitHubで効率化
第3章では、GitHub Actions の本格導入を考えるうえで知っておきたい。 機能や使い方を紹介します。効率的なCI/CDパイプラインの作り方や 構成管理ツールとの組み合わせ、細かな開発作業の自動化に至るまで、 GitHub ベースのさまざまな作業を時短できることがわかるでしょう。

---
# 効率的なCI/CDパイプライン構築に必要な基礎知識
## 複数ジョブの実行パターン
ここでは複数ジョブの実行パターンについて 解説します。
リスト1のように複数ジョブが定義されてい る場合、デフォルトでは、各ジョブは図1のよ うに並行で実行されます。
ところが、並列実行ではなく、たとえばコー ドのビルド・テストを行うジョブのあとにデブ ロイを行うジョブのように、直列で複数ジョブ を実行したいケースもあります。その場合、jobs. job_id.needstシンタックスを使うことで、ぼ
1) URL https://docs.github.com/en/actions/learn-github
actions/workflow-syntax-for-github-actions #jobs job_idneeds
マリスト1 複数のジョブのデフォルト定義の例
on: push jobs: job_a:
runs-on: ubuntu-latest steps:
(....】 job_b:
runs-on: ubuntu-latest steps:
job_c:
runs-on: ubuntu-latest steps:

---

かのジョブに対する依存関係を定義できます。 リスト2では、jobs.job_id.needs シンタックスを 使い、Job A、Job B、JobCを直列実行するよ うに定義しています(図2)。
なお、当然ながら直列実行と並列実行を組み 合わせることで、リスト3のようなFan-out/ Fan-inパターン2によるジョブ実行フローも定 義できます(図3は実行イメージ)。よく利用さ れる例としては、複数OS環境における並列ビ ルドジョブ(Fan-out)が完了したら、その成果 物をリリースジョブでまとめてリリース(Fanin)するケースが挙げられます。

### Build Matrix
複数のOSやプラットフォーム、言語バージョ ンなど、設定オプション別のジョブを実行する
注2) メッセージング処理でよく登場するデザインパターンです。
ある共通の送信元から複数のターゲットに対してメッセー ジが並列で配送、拡散されることをFan-out.それらがすべ て完了したあとに共通の処理が実行されることをFan-inと 呼びます。

---

マリスト2 jobs.job_id.needsによる直列実行の例
on: push jobs: job_a:
runs-on: ubuntu-latest steps:
job_b:
needs: job_a R TDEA runs-on: ubuntu-latest steps:
job_c: needs: job_b S TORA runs-on: ubuntu-latest steps:

---

場合、個々の設定オプションをそれぞれジョブ 定義としてワークフローに追加できます。ただ し、オプション数が多いと、ワークフローが長 く、かつ冗長になります。このような場合、Build Matrixが非常に有効です。Build Matrix は jobs.

---

job_id.strategy.matrix#シンタック スにより設定オプションをリストで 指定できる機能です。
リスト4のサンプルは、第2章の 「CIパイプラインを構築する」で紹介
3) URL https://docs.github.com/en/actions/
learn-github-actions/workflowsyntax-for-github-actionstjobsjob_ idstrategymatrix

---

したGo言語アプリのビルドとテストを行うサン ブルを、Build Matrix によりGoの複数のバー ジョンとOSのパターンで実行するものです。
リスト4を実行した結果が図4です。Build Matrix により、Go言語アプリを、3つのバー ジョンのGo環境、さらに3種類のOSでビルド・ テストした、合計9個のジョブが実行されたこ とがわかります。

---

VUZ 4 Build Matrix Iko Go Xi77UOEK: 721
(go-matrix.yml)
jobs: build: strategy: matrix:
go-version: [1.15, 1.16, 1.17]
os: Cubuntu-latest, macos-latest, windows-latest] runs-on: ${{ matrix.os }} steps: - uses: actions/checkoutav2 - name: Set up Go
uses: actions/setup-goav2 with:
go-version: $CC matrix.go-version) - name: Build
run: go build -v ./... - name: Test
run: go test -v ./...

---

## ワークフロー内のデータ共有
1第1章で説明したとおり、ワークフロー内の各 ジョブは、ランナーの別々のインスタンスで実行 されます。また、ジョプ内の各ステップはラン ナーの別々のプロセスで実行されます。よって、 各ステップで定義する環境変数を変更したとし ても、ステップ間では共有されず、当然ながら ジョブ間でも共有されません。このように、ス テップ、ジョプいずれも、それぞれのレベルで 実行空間が分離されているため、データ共有を する際には工夫が必要です。ここでは、各ステッ プ問、ジョブ問のデータ共有方法を紹介します。

### ステップ間のデータ共有
同一ジョプ内の各ステップは、別々のプロセ スで実行されるものの、同じランナーのインス ・タンス内で実行されるため、共通のワークスペー

---

スとファイルシステムにアクセスできます。つ まり、同一ジョブにおけるすべてのステップは、 共通のファイルシステムを通じてデータを共有 できます。この場合、GITHUB_WORKSPACE やHOME といった既定の環境変数を活用できま す(リスト5)。
ほかにも、set-output コマンドを使う方法 があります。あるステップで、::set-output name=name::valueの形式で変数nameに値 value を設定すると、この変数はステップの Soutput パラメータに設定されます。そしてある ステップで output パラメータに設定された変数 は、同一ジョブの後の任意のステップからお{{ steps.step_id.output.name }}の形式で取 得できます。リスト6では、IDがset-numberのス テップで、set-output コマンドを使い、output パ ラメータに設定された変数 MY_NUMBERを、後 続のステップにて${{ steps.set-number. outputs, MY_NUMBER }}で取得しています。

### ジョブ間のデータ共有
jobs.job_id.outputs5を用いた複数ジョブ間に おけるデータ共有方法を紹介します。
注4) CD https://docs.github.com/ja/actions/hearn-github
actions/workflow-commands-for-github-actions
setting-an-output-parameter #5) URL https://docs.github.com/en/actions/learn-github
actions/workflow-syntax-for-github-actions#jobs job_idoutputs

---

VUZ5 9-
7A77711274
177-*** (data-sharing-steps1.yml 5#*#)
steps: - name: Write Data in a Job
run: echo "Hello" > $CGITHUB_WORKSPACE]/myoutput.txt name: Read Data in a Job run:
value=$(cat SCGITHUB_WORKSPACE/myoutput.txt) echo "Read Data: ${value]"
マリスト6同一ジョブ内でset-outputを用いたデータ共有(data-sharing-steps2.ymlから抜粋)
steps: - name: Set my number
run: echo '::set-output name=MY_NUMBER:: 12345
id: set-number - name: Get my number
run: echo "My number is ${{ steps.set-number.outputs.MY_NUMBER }}"

---

VUN
%70 outputs & CT
7
707-*##(data-sharing-jobs1.yml)
jobs: job_1: runs-on: ubuntu-latest outputs:
output_1: $CC steps.step_1.outputs.my-value }}
output_2: $(< steps.step_2.outputs.my-value }} steps: - id: step_1
run: echo "::set-output name=my-value:: apple" - id: step_2
run: echo "::set-output name=my-value::banana" job_2:
runs-on: ubuntu-latest needs: job_1 steps: -run: echo ${{needs.job_1.outputs.output_13) ${{needs.job_1.outputs.output_2}}

---

任意のジョブの処理結果は、jobs.jobs_id.out putsで設定できます。そして、後続ジョブはそ の出力結果を参照できます。
リスト7では、job_1の各ステップで、setoutputで設定された出力結果をjobs.job_1. outputsに設定しています。そして、jobで設定 された出力結果をjob_2 で SHI needs.job_1. outputs. 変数名 }}として参照しています。
ほかにも、Artifact(成果物)を格納するため のストレージを用いた、複数ジョブ間のデータ 共有方法があります。この場合、Artifactアッ プロード用アクションである upload-artifact 6 と、Artifact ダウンロード用のアクション down load-artifactTを活用します。具体的には、任 意のジョブで生成したファイル(Artifact)を、 upload-artifactを用いてArtifact用のストレー ジにアップロードし、後続のジョブは:downloadartifact を用いて先にアップロードされたファ イルをArtifact用のストレージからダウンロー ドして、その中身を参照します。なお、任意の ワークフローの実行中にアップロードされた Artifact は、そのワークフロー実行中にだけダ ウンロードが可能な点に注意が必要です。
Artifactを用いた複数ジョブ間のデータ共有 方法の詳細は、GitHub 公式ページ「Passing data
6) GAD https//github.com/actions upload-artifact 7) URL https://github.com/actions/download-artifact

---

between jobs in a workflow」をご参照くださ

## キャッシュの活用
GitHub ホスト型ランナーインスタンスで実行 されるジョブは、実行ごとにクリーンな仮想マ シンから実行されるため、ジョブの実行が終わ ると保存されていたデータは破棄されます。よっ て、アプリケーションのビルドなどに必要な依 存ファイルは、都度ダウンロードする必要があ ります。それらの依存ファイルのダウンロード にかかる時間を短縮するために、ワークフロー 内で頻繁に使われる依存データをキャッシュす るしくみをGitHub Actionsは標準でサポートし ています。キャッシュは、リポジトリのすべて のワークフローで共有可能です。たとえば、main ブランチでダウンロードされたパッケージを キャッシュし、ほかのブランチでリストアして 利用することが可能です。ワークフロー内で、 依存データをキャッシュする際には、キャッシュ アクションactions/cacheを用います。
キャッシュアクションには、表1の3つのパ ラメータがあります。 リスト8は、Go言語アプリのビルド処理高速
注8) CD https://docs.github.com/en/actions/advanced.
guides/storing-workflow.data-as-artifacts#
passing-data-between-jobs-in-a-workflow 9) URL https://github.com/actions cache

---

表1 キャッシュアクションのパラメータ一覧 「パラメータの種類
概要・特徴 ・キャッシュするファイル群のパス |path(必須) ・keyパラメータの値がキャッシュのキーと一致すると、ここにキャッシュされたファイル
が復元される
・キャッシュに対応する完全マッチング用キー key(必須)
・この値が完全一致すると、キャッシュが復元される
・keyパラメータの値でキャッシュヒットしなかった場合の救済用あいまい一致用キー restore-keys
・複数キーの追加が可能で、キーを順番に探索して部分一致でキャッシュが復元される

---

化のために、モジュールとビルドのキャッシュ を行うサンプルです。
ここでは、Go言語のモジュールとビルド キャッシュの例を紹介しましたが、ほかにもさ まざまな言語パッケージに活用できます。ほか の言語におけるキャッシュ利用のサンプルは、 actions/cache アクションのサンプル一覧法10が 参考になります。なお、実際に活用する際には、 以下にも留意してください。
・7日間以上アクセスされていないキャッシュ
ファイルは自動的に削除されます ・リポジトリあたりの最大キャッシュサイズは 5GBで、この制限を超えた場合、合計サイズ が5GB以下になるまでキャッシュが退去され ます (参考:Usage limits and eviction policy#1)
10) URL https://github.com/actions/cache/blob/master/
examples.md 11) URL https://docs.github.com/ja/actions/advanced
guides/caching-dependencies-to-speed-upworkflowstusage-limits-and-eviction-policy

---

## Environmentsを活用した複数環境のデプロイメント管理
ここでは、Environments と呼ばれる、環境ご とにシークレットや保護ルールを設定できる機 能を使った、CI/CDパイプラインの設定方法を 紹介します。
CI/CDパイプラインからデプロイする環境は、 本番環境だけではありません。図5のように、開 発・検証環境、ステージング環境、本番環境な ど、複数の環境を対象とすることがほとんどで す。そのような場合、環境ごとに異なるシーク レットやルールの要件が存在するでしょう。 Environmentsは、そのような要件を満たすべく、 2021年12月にリリースされた比較的新しい機 能です。
なお、Environments は、公開リポジトリ、も しくはGitHub Enterprise Cloudでだけ利用可 能な機能です。

---

VUZ
Go E%1-VEELK&#
174%7(go-cache.yml 851)
(.. ..) - uses: actions/cachea v2
id: setup-cache with: path: |
7go/pkg/nod
7.cache/go-build key: ${{ runner.os }}-go-S<hashFiles('**/go.sum') }} restore-keys:
$C runner.os }}-go
- name: Build
run: go build -v ./...
- nane: Test
run: go test -v ./...

---

### Environmentsによる複数環境
の設定 リポジトリ下の「Settings」タブを クリックし、「Environments」を選択 します。そして、[New environment] ボタンをクリックし、名前を入力す ることで新規 Environment を作成 できます。ここでは、図6のように production, staging, development という3つのEnvironment を作成し ます。
そして、図7は各Environment の 設定ページです。大きく3種類の設 定が可能です(表2)。
次に、Environments を活用した複 数環境にデプロイするワークフロー を紹介します。
リスト9のサンプルでは、mainブ ランチへのコミットやマージをトリ ガーとして、build_test ジョブで ビルドとテストを行い、その後、 deploy_stagingジョブでステージン グ環境にデプロイします。そして、

---

▼表2 Environments の設定一覧 設定項目
概要・特徴 ・各環境の保護ルールの設定 Environment
|・保護ルールのRequired reviewersでは、ジョブを進行させるために承認者を設定可能 protection rules
・保護ルールのWait timerでは、ジョブ実行までの待機時間(最大30日)を設定可能 Deployment branches | Environmentにデプロイできるブランチ制限の設定
| Environment ごとのシークレットの設定 Environment secrets
・なお、図7ではすでにMY_SECRETという名前のシークレットが設定されている

---

マリスト9 Environmentを使って複数環境にデプロイするワークフローの例(multi-env-deploy.yml)
name: CICD to multi environments
on: push: branches:
- main
jobs: build_test:
runs-on: ubuntu-latest steps:
- run: echo building and testing!
deploy_staging: needs: [build_test] runs-on: ubuntu-latest environment:
name: staging steps:
- run: echo deploying to staging - run: echo using my secret for staging - St{ secrets.MY_SECRET >>
deploy_production:
needs: [deploy_staging] runs-on: ubuntu-latest environment:
name: production steps:
- run: echo deploying to production! - run: echo using my secret for production - ${{ secrets.MY_SECRET }}

---

deploy_staging ジョブのあとに、deploy_ productionジョブで本番環境にデプロイします。 deploy_staging ジョプと deploy_productionジョ ブには、jobs.job_id.environmentシンタックス で、それぞれstagingとproduction という名前の Environment を関連付けています。ここでは、 stagingとproductionのEnvironment には、別々 のMY_SECRETというシークレットを設定し ています。リスト9を実行すると、deploy_ staging ジョブでは stagingに設定したシー クレットが、deploy_production ジョブでは productionに設定したシークレットが使われま
す。

### ジョブ実行の承認者の設定
HD Environment of Environment protection rules」で、各Environmentの保護ルー ルの1つとして、ジョブを進行させるためのレ

---

ビュアーを設定できます。最大で6人のユーザー もしくはOrganization リポジトリの場合はTeam をレビュー担当者に指定可能です。ここでは、 図8のように筆者1人をレビュアーとして設定 します。
再びワークフローを開始すると、今度は、 deploy_stagingジョブの実行後、図9のように deploy_production ジョブがベンディング状態に なります。これは、レビュー待ちの状態です。
レビュアーには、図9の左のように[Review deployments]ボタンが表示され、図9の右のよ うに承認するかどうかを選択します。そして、 レビュアーが承認([Approve and deploy])を選 択すると、deploy_production ジョブの実行が開 始されます。なお、レビュアーが拒否([Rejeet]) を選択するとワークフローは失敗します。

---

# GitHub ActionsとlaCツールによるインフラ構成管理の自動化
 GitHub Actionsと構成管理ツールを組み合わ せ、CI/CDパイプラインを通じたインフラスト ラクチャの自動デプロイメントを実現させる例 を紹介します。

## lacとCI/CDによるインフラ構成管理の自動化
laCとは、Infrastructure as Codeの略で、イ

---

ンフラ構成をコード化し、その構築を自動化す る手法です。IaCを実践することで、インフラ 運用管理の属人化防止や作業ミスの削減ができ たり、何度でも同じ構成の環境を構築できたり するようになります。
なお、IaCを実現するための構成管理ツール には、表3のようなものがあります。
laCにおいて、コード化されたインフラ構成 ファイルは、GitHubのようなコード管理システ ムでバージョン管理され、CI/CDパイプライン

---

表3 構成管理ツールの例
構成管理ツール AWS CloudFormation
Google Cloud Deployment Manager
Azure Resource Manager
概要・特徴 ・AWSリソースの構成管理を可能にするサービス ・宣言型アプローチで構築を行う ・GCPリソースの構成管理を可能にするサービス ・宣言型アプローチで構築を行う ・Microsoft Azureリソースの構成管理を可能にするサービス ・宣言型アプローチで構築を行う ・HashiCorp社による、特定クラウド、マネージドサービスのリソー
スに限定しないOSS構成管理ツール ・宣言型アプローチで構築を行う ・Red Hat社による、特定クラウド、マネージドサービスのリソース
に限定しないOSS構成管理ツール ・手続き型アプローチで構築を行う
Terraform
Ansible

---

を用いて目的の環境にデプロイするのが一般的 です(図10)。IaCとCI/CDを組み合わせること で、一連のインフラ構築、構成変更が自動化さ れ、迅速かつ安全に実施できます。まさに、IAC とCI/CDはインフラ構成管理の自動化に欠かせ ない2大要素と言えます。

## GitHub ActionsによるlaCツール活用例
参考までに、Terraformを活用し、CI/CD経 由でAWSにEC2を構築するワークフローを紹 介します。
リスト10は、EC2インスタンスを作成する IaCファイル(HCL)、リスト11は、それをもと にTerraform経由でAWS環境にEC2インスタ ンスをデプロイするワークフローです。Terra
マリスト10 TerraformのHCLファイル
terraform { required_providers { aws = {
source = "hashicorp/aws" version="> 3.27"
backend "s3" {
bucket = "gha-terraform" key = "terraform. tfstate" region = "ap-northeast-1"
required_version = ">= 0.14.9"
resource "aws_instance" "app_server" { ani
="ami-0845511340543554c" instance_type = "t2.micro"
tags = {
Name = "ExampleEC2 Instance"

---

A
form e rsla HashiCorp # NTZ
r ahashicorp/setup-terraform 127 利用しています。

## GitHub Actionsによる細かいタスクの自動化
GitHub Actions lt. -FOUNKT
12) URL https://github.com/hashicorp/setup-terraform
マリスト11 Terraformを活用したGitHub Actionsワーク
70
jobs: terraforn:
nane: "Terraform" runs-on: ubuntu-latest steps:
- nane: Setup Terraform
uses: hashicorp/setup-terraformav1 with:
terraforn_version: 0.14.9
- name: Terraform Format
run: terraform fnt -check
- nane: Terraform Init
run: terraform init
- nane: Terraform Validate
run: terraform validate -no-color
- nane: Terraform Plan
if: github.event_name == 'pull_request run: terraform plan -no-color
- nane: Terraform Apply
if: github.ref == 'refs/heads/nain' && 7 github.event_name ='push'
run: terraform apply -auto-approve

---

マリスト12actions/github-script を活用して Pull Request にコメントを投稿する例
- nane: Terraform Validate
id: validate run: terraform validate -no-color
- nane: Terraform Plan
id: plan if: github.event_nane = 'pull_request' run: terraform plan -no-color continue-on-error: true
- uses: actions/github-scriptav3
if: github.event_nane == 'pull_request! eny:
PLAN: "terraforminst steps.plan.outputs.stdout }}" with:
github-token: ${{ secrets.GITHUB_TOKEN }} script:
const output = W Terraform Validation SCC steps.validate.outcome) #### Terraform Plan \"${{ steps.plan.outcome }} <details><summary>Show Plan</summary>
In ${process.env.PLAN)
</details> ; github.issues.createComment
issue_number: context.issue. number, owner: context.repo.owner, repo: context.repo.repo, body: output
)

---

・リリースなどを自動化できますが、CI/CD専用 の自動化ツールではありません。第1章で説明 したとおり、GitHub Actionsはリポジトリで発 生するすべての操作イベントをトリガーとして ワークフローを実行できます。そのため、さま ざまなタスクの自動化が可能です。たとえば、 Issueの作成(issues)やIssueへのコメント (issue_comment)、リポジトリへのラベル作成 (label)などが挙げられます。ここでは、代表的 なタスクの自動化を2つ紹介します。

## CIの処理結果をPull Requestのコメントとして投稿
先ほど紹介した、Terraformを活用したCI/ CD経由による、Amazon EC2を構築するワー クフローを拡張してみます。Terraformの構成 管理を記述するファイルのフォーマットチェッ ク、パリデーションチェック、terraform plan などの処理結果を、各ステップにおける output

---

の出力結果から取得し、Pull RequestのIssue コ メントとして投稿します。この Issue コメント の投稿は、actions/github-script1はアクション を活用します。また、Issue コメントの投稿に は、GitHub APIを利用する必要があります。こ の actions/github-scriptは、リスト12のように、 script 部分に直接JavaScriptをインラインで記 述でき、GitHub API操作のためのJavaScript クライアントライブラリ(octokit/rest.js注1)を API認証済みの状態で利用できます。
図11は、このワークフロー実行で、Pull Request にコメント投稿された結果です。

## 変更ファイルのバスに基づくPull Requestへの自動ラベル付与
) 2つめは、actions/labeler15アクションを
13) URL https://github.com/actions/github-script
14) URL https://octokit.github.io/rest.js/v18 注15) ORD https://github.com/actionstabeler

---

VUZ 13 .github/labeler-config.yml
#kubernetesti. ML (279 ) kubernetes: - kubernetes/**/*
TAL
# cloudformation TO cloudformation: - cloudformation/*
* terrafor ALTFOL terraform: - terraform/*

---

使った、Pull Request への自動ラベル付与の です。actions/labelerは、変更されるファイル のバスに基づき、新しいPull Requestに自動的 にラベルを付与してくれます。
リスト13は、ファイルの変更に対してどのラ ベルを付与するのかを定義するYAMLファイル です。そして、リスト 14は、actions/labeler アク ション利用を定義しているワークフローです。Pull Requestをトリガーに実行されると、actions/ labelerアクションの中で指定する.github/ labeler-config.ymlファイルの内容に基づいてラ ベルが付与されます。

---

VUZ 14 .github/workflows/labeler.yml
name: Labeler on:
pull_request:
jobs: Tabel: runs-on: ubuntu-latest steps: - uses: actions/labelerav3 with:
repo-token: "${{ secrets.GITHUB_TOKEN }}" configuration-path: ".github/labeler-config.yml" sync-labels: true

---

図12は、リスト13、14のワークフローを実 行し、付与されたPull Request のラベルです。

## おわりに
REA
第1章ではGitHub Actionsの概要を、第2章 ではGitHub Actionsを使ったCI/CDパイプラ イン構築をハンズオン形式で解説しました。そ して、第3章では、効率的なワークフローの構 築や、開発フローの自動化のために押さえてお きたい基礎知識を紹介しました。GitHub Actions を使うことで、CI/CDはもちろん、さまざまな

---

GitHubベースの作業が自動 化でき、効率的なソフトウェ ア開発が可能になることをご 理解いただけたのではないで しょうか。本稿がみなさんの GitHub Actions導入の一助 となれば幸いです。50

