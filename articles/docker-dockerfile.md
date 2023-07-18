Dockerfileとdocker-composeを使いこなす
Dcoker,Dockerfile,docker-compose
docker-dockerfile

# Dockerfileとdocker-composeを使いこなす
docker-compose.ymlでDockerfileを指定して起動をコントロールする。
こうすることで修正はDockerfileのみでよくなり、
docker-compose.ymlへの記述が長くなるのを防げる。

# Dockerfileとdocker-composeの分離の手順
1. test用ディレクトリの作成、移動
```
mkdir test_docker
cd ./test_docker
```

2.  test用のファイルの用意
```
touch docker-compose.yml
touch Dockerfile1
touch Dockerfile2
```

# docker-composeのサンプル
``` touch docker-compose.yml
version: '3'

services:
  container1:
    build:
      context: .
      dockerfile: Dockerfile1
  container2:
    build:
      context: .
      dockerfile: Dockerfile2
```
「build: dockerfile」でDockerfileを指定して記述できます。

# Dockerfileのサンプル
``` Dockerfile1
FROM python:3.9
```

``` Dockerfile2
FROM node:latest
```

# コンテナの起動
```
$ docker-compose up --build
Creating network "test_docker_default" with the default driver
Building container1
[+] Building 1.0s (5/5) FINISHED
 => [internal] load build definition from Dockerfile1                      0.0s
 => => transferring dockerfile: 54B                                        0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load metadata for docker.io/library/python:3.9              0.9s
 => CACHED [1/1] FROM docker.io/library/python:3.9@sha256:d88a0a58aeaa7e7  0.0s
 => exporting to image                                                     0.0s
 => => exporting layers                                                    0.0s
 => => writing image sha256:4c6c7fcdd014bb8d4e5ea3ec1452658f118b6cbc39d5f  0.0s
 => => naming to docker.io/library/test_docker_container1                  0.0s

 Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
 Building container2
[+] Building 0.9s (5/5) FINISHED
 => [internal] load build definition from Dockerfile2                      0.0s
 => => transferring dockerfile: 55B                                        0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load metadata for docker.io/library/node:latest             0.8s
 => CACHED [1/1] FROM docker.io/library/node:latest@sha256:52bda4c171f379  0.0s
 => exporting to image                                                     0.0s
 => => exporting layers                                                    0.0s
 => => writing image sha256:b464dde1aefa975c31d071d0ab733f54780cacbc8c6d7  0.0s
 => => naming to docker.io/library/test_docker_container2                  0.0s

 Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
 Creating test_docker_container2_1 ... done
 Creating test_docker_container1_1 ... done
 Attaching to test_docker_container2_1, test_docker_container1_1
 test_docker_container2_1 exited with code 0
 test_docker_container1_1 exited with code 0
```

# コンテナの終了
```
$ docker-compose down
Removing test_docker_container1_1 ... done
Removing test_docker_container2_1 ... done
Removing network test_docker_default
```

正しく動作している。

　

## Docker 関連のまとめ
https://hack-note.com/summary/docker-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

