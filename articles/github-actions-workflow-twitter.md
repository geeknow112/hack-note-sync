Github Actionsを使ってGithubにpushしたらTwitterに自動投稿する方法
github-actions,twitter-api,workflow,automation
github-actions-workflow-twitter

こんにちは。今回は、Github Actionsを使って、GithubにpushしたらTwitterに自動投稿する方法について解説していきます。Github Actionsを使えば、Github上のイベントをトリガーに、様々な処理を自動化することができます。この記事では、Github Actionsを使ってGithubにpushしたらTwitterに自動投稿する方法を実際の例を交えながら解説します。

## 前提条件

この記事を読む前に、以下の前提条件を満たしていることを確認してください。

- Githubアカウントを持っていること
- Twitterアカウントを持っていること
- Twitter Developer Accountを持っていること

## 手順

以下の手順に従って、GithubにpushしたらTwitterに自動投稿するワークフローを作成しましょう。

### 1. Twitter Developer Accountを作成する

Twitter Developer Accountを持っていない場合は、以下の手順に従ってアカウントを作成してください。

1. [Twitter Developer Platform](https://developer.twitter.com/en)にアクセスし、アカウントを作成する。
2. 「Create an App」をクリックし、アプリを作成する。
3. 「Keys and tokens」タブから、Consumer Key、Consumer Secret、Access Token、Access Token Secretを取得する。

### 2. Twitter APIを使うためのライブラリをインストールする

Twitter APIを使うためのライブラリである[twitter-lite](https://github.com/draftbit/twitter-lite)をインストールします。npmを使ってインストールすることができます。

```bash
npm install twitter-lite
```

### 3. Githubにリポジトリを作成する

Githubにリポジトリを作成し、ローカル環境にクローンします。

### 4. ツイートするスクリプトを作成する

Github Actionsで実行するスクリプトを作成します。ここでは、以下のようなスクリプトを作成します。

```javascript
const Twitter = require('twitter-lite');

const client = new Twitter({
  subdomain: "api",
  consumer_key: process.env.TWITTER_CONSUMER_KEY,
  consumer_secret: process.env.TWITTER_CONSUMER_SECRET,
  access_token_key: process.env.TWITTER_ACCESS_TOKEN,
  access_token_secret: process.env.TWITTER_ACCESS_TOKEN_SECRET
});

const tweet = `New commit pushed to ${process.env.GITHUB_REPOSITORY}!`;

client
  .post("statuses/update", {
    status: tweet,
  })
  .then((result) => {
    console.log("Tweeted successfully!");
  })
  .catch((error) => {
    console.error(error);
  });
```

このスクリプトでは、Twitter APIを使用して、指定したテキストをツイートすることができます。

### 5. ワークフローファイルを作成する

Github Actionsで実行するワークフローファイルを作成します。リポジトリのルートに、.github/workflowsディレクトリを作成し、以下のような内容のtweet.ymlという名前のファイルを作成します。

```yaml
name: Tweet on Push

on:
  push:
    branches:
      - main

jobs:
  tweet:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14.x'
      - name: Install dependencies
        run: npm install
      - name: Tweet on Push
        env:
          TWITTER_CONSUMER_KEY: ${{ secrets.TWITTER_CONSUMER_KEY }}
          TWITTER_CONSUMER_SECRET: ${{ secrets.TWITTER_CONSUMER_SECRET }}
          TWITTER_ACCESS_TOKEN: ${{ secrets.TWITTER_ACCESS_TOKEN }}
          TWITTER_ACCESS_TOKEN_SECRET: ${{ secrets.TWITTER_ACCESS_TOKEN_SECRET }}
        run: node tweet.js
```

このワークフローでは、mainブランチにpushされた場合、tweet.jsスクリプトが実行され、指定したテキストがツイートされます。

### 6. シークレット情報を設定する

最後に、Twitter APIのキーとトークンをGithubのシークレットとして設定する必要があります。リポジトリのSettings > Secretsから、以下の4つのシークレットを設定します。

- TWITTER_CONSUMER_KEY
- TWITTER_CONSUMER_SECRET
- TWITTER_ACCESS_TOKEN
- TWITTER_ACCESS_TOKEN_SECRET

それぞれのシークレットには、Twitter Developer Accountで取得したキーとトークンを設定してください。

これで、GithubにpushするとTwitterに自動投稿されるようになりました！

## まとめ

今回は、Github Actionsを使ってGithubにpushしたらTwitterに自動投稿する方法について解説しました。Github Actionsを使えば、簡単に自動化ワークフローを作成することができます。ぜひ、自分にあった自動化ワークフローを作成して、作業効率を上げていきましょう。


　

## Github 関連のまとめ
https://hack-note.com/summary/github-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

