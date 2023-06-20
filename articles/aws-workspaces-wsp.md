AWS WSP（Workspaces Streaming Protocol）が利用できずあがいた件
AWS,WSP,Workspaces
aws-workspaces-wsp

# 参考
こちらの記事で概ね全て記載ありましたので、これに沿って利用確認してみました。
https://dev.classmethod.jp/articles/general-availability-about-amazon-workspaces-streaming-protocol/

# 事前準備
参考記事の通り、普通にWSP版を利用して動作確認をしました。
手順は下記の通りです。
1. コンソール画面でWorkspacesのバンドルを移行（PCoIP → WSP）
2. Workspacesアプリのデバイス設定で「リモートで利用する」に設定
3. ウェブカメラテストサイト(https://ja.webcamtests.com/)で動作確認

検証には、meetを使うと認証で面倒だったのでテストサイトを使いました。

# 異常
3台ほどWorkspacesを立ち上げて確認しましたが、どれもローカルのカメラを認識してくれず、エラーとなっていました。

# 原因調査
## ネットワークの疎通の問題
まず疑ったのがネットワークの疎通が正しく行えているかどうかです。
下記の点、確認しました。（最終的には、あえて設定することなく疎通することができました。）
- ポート4195が開放されていること
- WSPゲートウェイサーバーへアクセスできること

### ポート4195の開放
特にファイアウォールの設定はしていなかったので、
ポート4195も開放状態でしたが、明示的に開放しました。
結果的に不要な措置でした。

### pingによる疎通確認
WSPゲートウェイサーバー（アジアパシフィック (東京)	3.114.164.0/22）へ、下記の通り疎通できていました。
```
PS C:> test-netconnection 3.114.164.1 -port 4195
ComputerName     : 3.114.164.1
RemoteAddress    : 3.114.164.1
RemotePort       : 4195
InterfaceAlias   : Wi-Fi
SourceAddress    : ***.***.***.***
TcpTestSucceeded : True
```

ヘルスチェックサーバー（アジアパシフィック (東京)	drp-nrt.amazonworkspaces.com 54.64.174.128）へ、下記の通り疎通できていました。
```
PS C:> Test-NetConnection -ComputerName drp-nrt.amazonworkspaces.com -port 4195

ComputerName     : drp-nrt.amazonworkspaces.com
RemoteAddress    : 54.64.174.128
RemotePort       : 4195
InterfaceAlias   : Wi-Fi
SourceAddress    : ***.***.***.***
TcpTestSucceeded : True
```

## Windows上のカメラアプリの許可
下記を参考に設定値を見直しました。
https://paso-kake.com/it/windows10/8735/
https://pc-karuma.net/windows-10-enable-disable-use-camera-app/

### Windowsの設定
カメラの設定をONにしましたが、カメラを認識せずでした。

###  レジストリのカメラ設定
rededitでカメラ用の設定を追加しましたが、カメラを認識せず、結果的に不要な措置でした。

## AD Connectorを利用している点
AD Connectorを利用してActiveDirectoryと連携していることが原因かと思い、
SimpleADでディレクトリを再作成して、Workspacesを起動してみましたが、カメラを認識せずでした。
AD Connectorは特に関係なさそうです。

## リージョンを変えて実施
Workspacesのリージョンを変えて起動してみましたが、カメラを認識せずでした。

## AWSアカウントを変えて実施
AWSアカウントを変えてWorkspacesを起動してみましたが、カメラを認識せずでした。

# 解決方法
ノートPCを変えて、最新のWorkspacesアプリでアクセスするとすんなり利用できました。

# 原因
Workspacesアプリが最新版(バージョン4系)じゃなかったことが原因ぽい。
※メインで使ってるPCがWorkspacesアプリ(バージョン4系)だと正常起動せず、やむなく3系を使っていた。

　

## AWS Workspaces 関連まとめ
https://hack-note.com/summary/aws-workspaces-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)


