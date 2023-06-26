Github Actionsを使ってGithubにpushしたらはてなブログに自動投稿する方法
github-actions,hatena blog api,workflow,automation
github-actions-workflow-hatena

こんにちは。今回は、Github Actionsを使って、Githubにpushしたらはてなブログに自動投稿する方法について解説していきます。Github Actionsを使えば、Github上のイベントをトリガーに、様々な処理を自動化することができます。この記事では、Github Actionsを使ってGithubにpushしたらはてなブログに自動投稿する方法を実際の例を交えながら解説します。

## 前提条件

この記事を読む前に、以下の前提条件を満たしていることを確認してください。

- Githubアカウントを持っていること
- はてなブログアカウントを持っていること
- はてなブログAPIのAPIキーを取得していること

## 手順

以下の手順に従って、Githubにpushしたらはてなブログに自動投稿するワークフローを作成しましょう。

### 1. はてなブログAPIのAPIキーを取得する

はてなブログAPIを使うためには、APIキーが必要です。以下の手順に従って、はてなブログAPIのAPIキーを取得してください。

1. [はてなブログ](https://www.hatena.ne.jp/)にログインする。
2. 「設定」→「詳細設定」→「ブログの設定」をクリックする。
3. 「APIキー」欄にある「新しいAPIキーを生成する」をクリックする。
4. APIキーをコピーしてメモしておく。

### 2. Githubにリポジトリを作成する

Githubにリポジトリを作成し、ローカル環境にクローンします。

### 3. はてなブログAPIを使うためのライブラリをインストールする

はてなブログAPIを使うためのライブラリである[hatena-blog-api](https://github.com/miya0001/hatena-blog-api)をインストールします。npmを使ってインストールすることができます。

```bash
npm install hatena-blog-api
```

### 4. はてなブログに投稿するスクリプトを作成する

Github Actionsで実行するスクリプトを作成します。ここでは、以下のようなスクリプトを作成します。

```javascript
const HatenaBlogAPI = require('hatena-blog-api');
const blog = new HatenaBlogAPI({
  type: 'wsse',
  username: 'はてなID',
  blogId: 'ブログID',
  apiKey: process.env.HATENA_API_KEY
});

const title = 'はてなブログに投稿するタイトル';
const body = 'はてなブログに投稿する本文';
const draft = false;

blog.post(title, body, { draft })
  .then(() => {
    console.log('投稿が完了しました！');
  })
  .catch((error) => {
    console.error(error);
  });
```

このスクリプトでは、はてなブログAPIを使用して、タイトル、本文、下書きかどうかを指定して、はてなブログに投稿することができます。

### 5. ワークフローファイルを作成する

Github Actionsで実行するワークフローファイルを作成します。リポジトリのルートに、.github/workflowsディレクトリを作成し、以下のような内容のhatena-blog.ymlという名前のファイルを作成します。

```yaml
name: Post to Hatena Blog on Push

on:
  push:
    branches:
      - main

jobs:
  post-to-hatena-blog:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Setup Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14.x'
      - name: Install Dependencies
        run: npm install
      - name: Post to Hatena Blog
        env:
          HATENA_API_KEY: ${{ secrets.HATENA_API_KEY }}
        run: node post-to-hatena-blog.js
```

このワークフローでは、mainブランチにpushされた場合、post-to-hatena-blog.jsスクリプトが実行され、はてなブログに投稿されるようになっています。また、ワークフロー実行時には、はてなブログAPIのAPIキーをGithubのシークレットに設定しています。

### 6. Githubにpushする

作成したスクリプト、ワークフローファイルをGithubにpushします。pushが完了すると、Github Actionsが自動的に実行され、はてなブログに投稿されます。

## まとめ

以上が、Github Actionsを使ってGithubにpushしたらはてなブログに自動投稿する方法の解説でした。Github Actionsを使えば、Github上のイベントをトリガーに、様々な処理を自動化することができます。是非、自分の開発環境に合わせた自動化を検討してみてください。


　

## Github 関連のまとめ
https://hack-note.com/summary/github-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

