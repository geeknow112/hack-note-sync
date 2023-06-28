別のGitからGithubにリポジトリを移行する方法
github,git,リポジトリ,python

# 環境
- Centos
- git version 2.27.0

# 1. GitHubで新規リポジトリを作成

# 2. 移行元をミラーリングでクローンする
>git clone --mirror {移行元 リポジトリ URL}

# 3. Push先に移行先(1.で作成したリポジトリ)を設定する
## 移行元へcd
>cd {ミラーリングした移行元 リポジトリ パス}.git

## Push先に移行先を設定する
>git remote set-url --push origin {移行先 リポジトリ URL}

## 確認する
>git remote -v

>git fetch --all

# 4. 移行先へPushする
>git push --mirror

# 5. 認証に応える
