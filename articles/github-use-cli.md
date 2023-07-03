Github CLIで簡単にリポジトリを作成する方法
github,cli
github-use-cli

こんにちは。今回は、Github初心者に向けて、Github CLIを使って簡単にリポジトリを作成する方法を解説します。

## Github CLIとは

Github CLIは、Githubのコマンドラインインターフェイスです。Githubの様々な操作をコマンドラインから行うことができます。例えば、リポジトリの作成やクローン、プルリクエストの作成などが簡単に行えます。

## Github CLIのインストール

Github CLIを使用するには、まずはインストールが必要です。以下の手順を参考に、Github CLIをインストールしてください。

1. [Github CLIのダウンロードページ](https://cli.github.com/)にアクセスし、自分のOSに合わせたインストーラーをダウンロードします。
2. ダウンロードしたインストーラーを実行し、指示に従ってインストールを完了します。

## リポジトリの作成

Github CLIを使ってリポジトリを作成するには、以下の手順を実行します。

1. コマンドラインから、リポジトリを作成したいディレクトリに移動します。
2. `gh repo create`コマンドを実行します。
3. コマンドの指示に従い、リポジトリの情報を入力します。

```
$ cd my-project
$ gh repo create
? What do you want to name the repo? my-project
? Which org do you want to put the repo in? my-org
? Is this repo public? Yes
? This will create 'my-org/my-project' in your current directory. Continue?  Yes
✓ Created repository my-org/my-project on GitHub
✓ Cloned to my-project
```

これで、指定したディレクトリにリポジトリが作成され、クローンが完了します。

また、リポジトリの作成と同時にイシューを作成することもできます。以下のコマンドを実行してください。

```
$ gh repo create --enable-issues
```

## コードのプッシュ

リポジトリを作成したら、コードをプッシュしてみましょう。Github CLIを使って、以下の手順でプッシュすることができます。

1. `cd`コマンドでプッシュするディレクトリに移動します。
2. `git add .`コマンドで変更内容をステージングします。
3. `git commit -m "コミットメッセージ"`コマンドでコミットします。
4. `gh repo view`コマンドで、リポジトリのURLを確認します。
5. `git remote add origin リポジトリのURL`コマンドで、リモートリポジトリとしてGithubのリポジトリを追加します。
6. `git push -u origin main`コマンドで、コードをプッシュします。

```
$ cd my-project
$ git add .
$ git commit -m "Initial commit"
$ gh repo view --web
$ git remote add origin https://github.com/my-org/my-project.git
$ git push -u origin main
```

以上で、Github CLIを使ってリポジトリを作成し、コードをプッシュする方法を解説しました。Github CLIは、コマンドラインから簡単にGithubの操作を行うことができるので、ぜひ活用してください。

>注意してほしいのは、Github CLIを使う場合には、Githubのアカウントが必要になることです。アカウントを持っていない場合は、[Githubのサイト](https://github.com/)からアカウントを作成してください。

## まとめ

- Github CLIを使うことで、Githubの様々な操作をコマンドラインから簡単に行うことができます。
- リポジトリの作成やコードのプッシュなどの操作が、より簡単になります。
- Github CLIを使うためには、まずはGithubのアカウントを作成し、Github CLIをインストールする必要があります。

以下が、コードのサンプルです。

```bash
$ gh repo create
```

```bash
$ git push -u origin main
```

　

## Github 関連のまとめ
https://hack-note.com/summary/github-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

