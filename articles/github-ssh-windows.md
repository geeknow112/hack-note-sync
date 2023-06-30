【初心者向け】WindowsでのGitHub SSH設定方法
Github,SSH,Windows
github-ssh-windows

こんにちは。今回は、Githubについて初心者エンジニアに向けて、WindowsでのGitHub SSH設定方法を紹介します。

## はじめに

GitHubは、プログラムの開発やコードの共有に利用される、世界中の開発者にとって不可欠なプラットフォームです。GitHubを使用する際に、SSHを使用することで、より安全にリモートリポジトリにアクセスすることができます。本記事では、WindowsでのGitHub SSH設定方法を説明します。

## SSHキーの生成

まず、SSHキーを生成する必要があります。以下の手順に従って、SSHキーを生成してください。

1. Git Bashを開きます。
2. `ssh-keygen`コマンドを実行します。
3. プロンプトが表示されたら、キーの保存場所やパスフレーズを設定します。
4. キーの生成が完了したら、公開鍵と秘密鍵が生成されたことを確認します。

>秘密鍵は絶対に他の人に知られてはいけません。秘密鍵は、SSH接続時に使用されるパスワードのようなものです。

## 公開鍵の登録

次に、生成した公開鍵をGitHubに登録する必要があります。以下の手順に従って、公開鍵を登録してください。

1. GitHubのWebサイトにログインします。
2. 右上のアカウントアイコンをクリックし、「Settings」を選択します。
3. 「SSH and GPG keys」をクリックします。
4. 「New SSH key」をクリックし、公開鍵をタイトルとともに貼り付けます。
5. 「Add SSH key」をクリックして、公開鍵を登録します。

## SSH接続のテスト

最後に、SSH接続をテストする必要があります。以下の手順に従って、SSH接続をテストしてください。

1. Git Bashを開きます。
2. `ssh -T git@github.com`コマンドを実行します。
3. GitHubのユーザー名とパスワードを求められたら、入力します。
4. 「Hi [ユーザー名]! You've successfully authenticated, but GitHub does not provide shell access.」と表示されたら、SSH接続に成功しています。

以上で、WindowsでのGitHub SSH設定が完了しました。

## まとめ

WindowsでのGitHub SSH設定方法を紹介しました。SSHを使用することで、より安全にリモートリポジトリにアクセスすることができます。手順に従って、SSHキーの生成と公開鍵の登録を行い、SSH接続をテストしてください。

## 参考文献

- [Generating a new SSH key and adding it to the ssh-agent - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [Adding a new SSH key to your GitHub account - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

　

## Github 関連のまとめ
https://hack-note.com/summary/github-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

