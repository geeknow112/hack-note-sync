Github Actionsでpushした時に実行するには
Github,Actions,push,開発
github-actions-on-push

こんにちは。今回は、Githubについて初心者エンジニアに向けて、Github Actionsの機能について紹介します。

## はじめに

コードの開発において、リポジトリ管理は非常に重要です。Githubを使用することで、チームでの開発やバージョン管理が容易に行えます。さらに、Github Actionsを活用することで、コードの変更やpushをトリガーとして、自動的にビルド・テスト・デプロイを行うことができます。

この記事では、Github Actionsでpushされたときに実行する方法について説明します。

### Github Actionsとは

Github Actionsは、Githubが提供するCI/CDツールです。コードの変更やpush、PRをトリガーに、自動的にビルドやテスト、デプロイなどのアクションを実行することができます。

Github Actionsの設定は、yaml形式で行います。リポジトリ内に配置するyamlファイルに、ジョブやステップの定義を記述します。Github Actionsを使用することで、開発の効率化や品質の向上が期待できます。

### Github Actionsでpushされたときに実行するには

Github Actionsを使って、pushイベントをトリガーにするには、以下のようなyamlファイルをリポジトリ内の`.github/workflows`フォルダに配置します。この例では、`main`ブランチにpushされた場合に、ステップを実行しています。

```yaml
name: CI

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      
      // ここにビルドやテストのステップを記述する
```

このyamlファイルの解説をします。

- `name` : ワークフローの名前を定義します。
- `on` : ワークフローを実行させるトリガーイベントを設定します。この場合、`push`イベントをトリガーに、`main`ブランチの変更を監視しています。
- `jobs` : ワークフローが実行するジョブを定義します。この場合、`build`というジョブを実行させています。
- `build` : ジョブの名前を定義します。
- `runs-on` : ジョブを実行させる環境を定義します。この場合、`ubuntu-latest`を指定しています。
- `steps` : ジョブが実行するステップを定義します。`actions/checkout`というアクションを行った後、この下にビルドやテストのコマンドを記述してください。


### 注意点

- リポジトリのpushによってアクションが実行されるため、GithubのAPIレートに制限がかかる場合があります。
- アクションの実行順序には注意が必要です。アクション間で依存関係を考慮して、実行順序を設定する必要があります。

## まとめ

今回は、Github Actionsを使用して、pushイベントをトリガーにしたビルドやテストの実行方法について説明しました。Github Actionsを活用すれば、開発チームの作業効率を向上させることができます。ぜひ、利用してみてください。

以下の記事も参考にしてください。

- [Github ActionsでのCI/CDの自動化について](https://www.slideshare.net/SoutaKojima2020/cicd-239271147)
- [Github Actionsの使い方](https://engineering.mercari.com/blog/entry/20200526-github-actions/)


　

## Github 関連のまとめ
https://hack-note.com/summary/github-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)


