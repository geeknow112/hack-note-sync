【twitter】api自動投稿 github actionsがおススメ
twitter,api,github-actions
twitter-github-action

こんにちは。今回は、twitterで月5万、安定収入を稼ぐ方法を知りたい人に向けて、api自動投稿についてお伝えします。

最近では、snsを活用したネットビジネスが注目されています。特に、twitterは手軽に使える上に多くの人が利用するため、自分のビジネス展開に最適です。しかし、毎日の投稿作業は手間がかかることがあります。そこで、今回はgithub actionsを活用したtwitterの自動投稿についてご紹介します。

## github actionsとは

github actionsとは、github上にあるリポジトリを監視し、事前に設定した条件がトリガーになると自動化されたタスクを実行するシステムです。具体的には、開発者たちはastが提供するライブラリを使って、タスクをコードとして定義し、githubにコミットすることで実行されるように設定することができます。

このgithub actionsを利用することで、twitterのapiを使った自動投稿を実現することができます。

## twitter + github actionsがおススメな理由

twitterでビジネスを行う場合、コンスタントに投稿を行うことが重要ですが、その作業には時間と手間がかかることが多いです。

しかし、github actionsを使えば自動投稿ができるため、自分自身が毎日コミットすることと同じように、正確でコンスタントな投稿を行うことができます。さらに、github actionsで自動化されたタスクはコードと同じようにバージョン管理もできるため、運用面でも安心です。

また、github actionsを使ったtwitterの自動投稿は、無料で利用することができます。このため、初めてtwitterでビジネスを始める人や、収益をあげるまでに予算をかけたくない人にもおススメです。

## 実際の導入方法

ここからは、twitter + github actionsの実際の導入方法について紹介します。

### 1. twitter developer accountを作成する

まずは、twitter developer accountを作成する必要があります。developer accountは、twitter apiを利用するために必要なアカウントです。次のurlからアカウント登録を行ってください。

- twitter developer account: https://developer.twitter.com/en/apps

### 2. twitter api keyを取得する

developer accountを作成したら、次はtwitter api keyを取得する必要があります。twitter api keyは、自動投稿に必要な認証情報です。

1. developer accountにログインし、[apps] -> [create app]をクリックして、新しいアプリを作成します。
2. アプリ名・説明・ウェブサイト・利用用途を入力し、[create]ボタンをクリックします。
3. [keys and tokens]タブを選択し、[generate]ボタンをクリックしてconsumer key・consumer secretを入手します。
4. [bearer token]セクションに進み、[generate]ボタンをクリックし、bearer tokenを入手します。

### 3. githubリポジトリを作成する

次に、githubリポジトリを作成する必要があります。githubで新しいリポジトリを作成し、ローカルpcにクローンします。その後、リポジトリ内にconfig.ymlというファイル名で次のようにjson形式の設定ファイルを用意します。

```
name: tweet_my_blog
on:
  schedule:
    - cron: '0 0 * * *'
jobs:
  tweet:
    runs-on: ubuntu-latest
    steps:
      - name: checkout repository
        uses: actions/checkout@v2

      - name: install dependencies
        run: |
          npm install -g twit
      - name: tweet my blog
        env:
          consumer_key: ${{ secrets.consumer_key }}
          consumer_secret: ${{ secrets.consumer_secret }}
          access_token: ${{ secrets.access_token }}
          access_token_secret: ${{ secrets.access_token_secret }}
        run: |
          node tweet.js
```

### 4. twitter自動投稿の実行ファイルを設定する

以下のコードをtweet.jsというファイル名で作成し、githubリポジトリ内のconfig.ymlと同じ階層に保存します。

```
const twit = require('twit')

const t = new twit({
  consumer_key: process.env.consumer_key,
  consumer_secret: process.env.consumer_secret,
  access_token: process.env.access_token,
  access_token_secret: process.env.access_token_secret,
})

const tweet = `今日のブログ記事が投稿されました！ ${new date()}`
t.post('statuses/update', { status: tweet }, (err, data, response) => {
  console.log(data)
})
```

### 5. github secretsに認証情報を記述する

最後に、githubで利用する認証情報を設定します。github secretsにconsumer_key、consumer_secret、access_token、access_token_secretを追加します。

1. githubリポジトリのsettingsタブを選択します。
2. 左のメニューから[secrets]ページを選択して、[new repository secret]ボタンをクリックします。
3. 名前には、それぞれ「consumer_key」「consumer_secret」「access_token」「access_token_secret」と入力して、twitterから取得した値を設定し、[add secret]ボタンをクリックします。

すると、毎日指定した時間にtwitterに自動投稿されるようになります。

## 具体的に活用していく上での日常タスク

twitter + github actionsを利用すると、日常的なブログ記事投稿以外にも、さまざまなタスクを自動化することができます。

例えば、以下のようなタスクが実現できます。

- rssフィードに新しい記事がないか定期的に確認し、あればtwitterに自動投稿する。
- 特定のワードが含まれたツイートをリツイートする。
- 自動返信機能を実装して、特定のワードが送信された場合に自動返信する。

自分自身のビジネスやブログの運用に合わせた業務自動化を実現できるので、ストレスなくコンスタントな投稿ができるようになります。

## まとめ

今回は、twitter + github actionsを使った自動投稿について紹介しました。twitter apiを使った自動投稿には手間がかかることがあるため、github actionsを利用することで自動投稿を実現することができるのが大きなメリットです。ぜひ、twitterでの稼ぎ方に活用してみてください。

参考:
- [github actions documentation](https://docs.github.com/en/actions)
- [twit - npm](https://www.npmjs.com/package/twit)


## twitter関連のまとめ
https://hack-note.com/tools/twitter-summary/


## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

