【初心者必見！】Githubの.gitignoreファイルの使い方
Github,GITIGNORE,使い方
github-gitignore

こんにちは。今回は、Githubについて初心者エンジニアに向けて、.gitignoreファイルの使い方をご紹介します。

## はじめに

Githubを使用する上で、.gitignoreファイルの存在を知っていますか？このファイルは、Commitする際に無視されるファイルを指定するためのものです。例えば、パスワードなどの機密情報や、テスト用のファイルなどを指定することができます。それでは、実際に.gitignoreファイルを作成し、どのように指定するのかを見ていきましょう。

## .gitignoreファイルの作成方法

.gitignoreファイルは、ルートディレクトリに置く必要があります。まずは、下記のコマンドで新規にファイルを作成しましょう。

```
$ touch .gitignore
```

次に、作成した.gitignoreファイルに無視したい拡張子やフォルダ名を指定します。例えば、以下のように記述することができます。

```
# コメントアウトは "#" を使用します

# フォルダの指定
secret_folder/

# ファイルの指定
*.log
```

上記の例では、"secret_folder"というフォルダを無視し、拡張子が".log"で終わるファイルを無視するように指定しています。

## サンプルコード

### 1. .gitignoreファイルによる無視

```
# Node.js
node_modules/

# .envファイル
.env

# ビルドファイル
/dist
/build
/out
```

上記のように、依存関係のあるnode_modulesフォルダや、環境変数を保持する.envファイル、ビルドしたファイルを無視することができます。

### 2. ファイル指定の例

```
# ログファイルの指定
*.log

# バイナリファイルの指定
*.exe
*.dll

# 画像ファイルの指定
*.jpg
*.png
*.gif
```

上記のように、拡張子を指定することで該当するファイルが無視されるようになります。

## 注意点

- .gitignoreでは、フォルダ名の末尾に「/」をつける必要があります。
- 同じファイル名でも、場所によって別々に指定することができます。
- .gitignoreファイルに指定した内容は、既存の変更やファイルの変更をCommit前に行わないと反映されません。

## まとめ

今回は、Githubの.gitignoreファイルの使い方についてご紹介しました。.gitignoreファイルを使うことで、Commitする際に不要なファイルを削除する手間を省くことができます。是非、活用していきましょう。

参考記事：
- [初心者でもわかるGitの使い方――プロジェクト管理を効率化する｜TechAcademyマガジン](https://techacademy.jp/magazine/6235)
- [Gitで管理されているファイルの指定を無視する方法（Gitignore）｜CodeZine](https://codezine.jp/article/detail/7868)

　

## Github 関連のまとめ
https://hack-note.com/summary/github-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

