GitHub Actionsによる自動化入門
GitHub,GitHub Actions,自動化
github-about-actions

こんにちは。今回は、GitHub初心者に向けて、GitHub Actionsによる自動化の基本について解説します。

## はじめに

GitHub Actionsは、GitHubが提供する自動化ツールです。GitHub上で行われるイベントやタスクをトリガーに、様々なプロセスを自動実行できます。例えば、コードをプッシュすると自動的にテストを実行したり、リリースを行うと自動的にデプロイを行うことができます。

## GitHub Actionsの基本

### ワークフローファイルの作成

GitHub Actionsは、ワークフローファイル(yaml形式)によって定義されます。ワークフローファイルは、`.github/workflows`ディレクトリに配置する必要があります。以下は、Node.jsで書かれたアプリケーションを自動テストするワークフローファイルの例です。

```yaml
name: CI

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Use Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14.x'
    - run: npm ci
    - run: npm run test
```

このワークフローファイルでは、GitHub上でのpushイベントをトリガーに、`ubuntu-latest`環境でNode.jsのテストを実行しています。

### アクションの利用

ワークフローファイルの中で、アクションを指定することで、特定のタスクを実行できます。アクションには、GitHubが提供する公式のアクションや、コミュニティが作成したアクションを利用できます。

以下の例では、公式のアクションである`actions/checkout`を利用して、リポジトリをクローンしています。

```yaml
steps:
- uses: actions/checkout@v2
```

また、以下の例では、アクションとして`actions/upload-artifact`を指定して、ビルド成果物をアップロードしています。

```yaml
steps:
- uses: actions/upload-artifact@v2
  with:
    name: binary
    path: path/to/binary
```

### 環境変数の設定

ワークフローの中で、環境変数を設定することができます。以下の例では、環境変数`API_KEY`を設定しています。

```yaml
env:
  API_KEY: ${{ secrets.API_KEY }}
```

環境変数には、GitHubのシークレット機能を利用して、APIキーやパスワードなどの機密情報を安全に設定することができます。

### ジョブの並列実行

複数のジョブを同時に実行することができます。以下の例では、`job1`と`job2`を並列で実行しています。

```yaml
jobs:
  job1:
    runs-on: ubuntu-latest
    steps:
    - run: echo Hello from Job 1

  job2:
    runs-on: ubuntu-latest
    steps:
    - run: echo Hello from Job 2
```

### ワークフローのトリガーの設定

ワークフローをトリガーするイベントを指定することができます。以下の例では、`push`イベントと`pull_request`イベントをトリガーに設定しています。

```yaml
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
```

### ワークフローの実行状況の確認

GitHub Actionsの実行状況は、GitHubのUIから確認することができます。また、以下のコマンドを利用することで、CLIからも確認することができます。

```
$ gh run list
```

## サンプルコード

以下は、Pythonで書かれたアプリケーションを自動テストするワークフローファイルの例です。

```yaml
name: CI

on: [pull_request]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings.
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

    - name: Test with pytest
      run: |
        pytest --cov=./ tests/
```

## 注意点

- GitHub Actionsは、無料で利用できますが、一定の制限があります。詳細は、[公式ドキュメント](https://docs.github.com/ja/actions/reference/usage-limits-billing-and-administration)を参照してください。
- ワークフローファイルは、yaml形式であるため、インデントが正しく設定されているかを確認する必要があります。
- アクションを利用する際には、そのアクションがどのような権限を必要とするかを確認し、必要な権限を付与する必要があります。

>GitHub Actionsは、様々なタスクを自動化できる非常に便利なツールですが、誤った設定によってセキュリティ上の問題を引き起こす可能性があります。注意深く設定を行い、セキュリティを確保するようにしましょう。

## まとめ

今回は、GitHub Actionsによる自動化の基本について解説しました。GitHub Actionsを利用することで、開発プロセスの自動化が容易になります。ぜひ、自身のプロジェクトに導入してみてください。

　

## Github 関連のまとめ
https://hack-note.com/summary/github-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)


