【Python】tweepy開発メモ
python,tweepy,twitter
python-tweepy-memo

# tweepy
[root@d613ec220c08 tweepy]# python3 -m pip install tweepy
WARNING: Running pip install with root privileges is generally not a good idea. Try `__main__.py install --user` instead.
Collecting tweepy
  Downloading https://files.pythonhosted.org/packages/67/c3/6bed87f3b1e5ed2f34bd58bf7978e308c86e255193916be76e5a5ce5dfca/tweepy-3.10.0-py2.py3-none-any.whl
Collecting requests-oauthlib>=0.7.0 (from tweepy)
  Downloading https://files.pythonhosted.org/packages/a3/12/b92740d845ab62ea4edf04d2f4164d82532b5a0b03836d4d4e71c6f3d379/requests_oauthlib-1.3.0-py2.py3-none-any.whl
Requirement already satisfied: requests[socks]>=2.11.1 in /usr/local/lib/python3.6/site-packages (from tweepy)
Requirement already satisfied: six>=1.10.0 in /usr/local/lib/python3.6/site-packages (from tweepy)
Collecting oauthlib>=3.0.0 (from requests-oauthlib>=0.7.0->tweepy)
  Downloading https://files.pythonhosted.org/packages/05/57/ce2e7a8fa7c0afb54a0581b14a65b56e62b5759dbc98e80627142b8a3704/oauthlib-3.1.0-py2.py3-none-any.whl (147kB)
    100% |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■| 153kB 7.1MB/s
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.6/site-packages (from requests[socks]>=2.11.1->tweepy)
Requirement already satisfied: chardet<5,>=3.0.2 in /usr/local/lib/python3.6/site-packages (from requests[socks]>=2.11.1->tweepy)
Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.6/site-packages (from requests[socks]>=2.11.1->tweepy)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.6/site-packages (from requests[socks]>=2.11.1->tweepy)
Collecting PySocks!=1.5.7,>=1.5.6; extra == "socks" (from requests[socks]>=2.11.1->tweepy)
  Downloading https://files.pythonhosted.org/packages/8d/59/b4572118e098ac8e46e399a1dd0f2d85403ce8bbaad9ec79373ed6badaf9/PySocks-1.7.1-py3-none-any.whl
Installing collected packages: oauthlib, requests-oauthlib, tweepy, PySocks
Successfully installed PySocks-1.7.1 oauthlib-3.1.0 requests-oauthlib-1.3.0 tweepy-3.10.0

## tweepy 投稿
https://tech-lab.sios.jp/archives/21400

##tweepy いいねなど
https://qiita.com/kitarikes/items/74b58bd28325d7d43a57

## ツイッターに電話番号を登録することについて
https://appllio.com/twitter-register-phone-number

## error
tweepy.error.TweepError: Read-only application cannot POST.
###対処法
https://qiita.com/butsuli_shine/items/78fd5ee6fdb4a0581652

## keyword search
https://qiita.com/ekzemplaro/items/92bf8f680b7667f028d5
## schedule いいね
https://qiita.com/pontyo4/items/7a33b2e1a6f949d76ade
## schedule 投稿
https://note.com/riverriverstream/n/n31adef0f8152


## すでにいいねしている場合のエラー
[root@d613ec220c08 tweepy]# python3 fav_tweet.py
Traceback (most recent call last):
  File "fav_tweet.py", line 24, in <module>
    api.create_favorite(id=user_id)
  File "/usr/local/lib/python3.6/site-packages/tweepy/binder.py", line 253, in _call
    return method.execute()
  File "/usr/local/lib/python3.6/site-packages/tweepy/binder.py", line 234, in execute
    raise TweepError(error_msg, resp, api_code=api_error_code)
tweepy.error.TweepError: [{'code': 139, 'message': 'You have already favorited this status.'}]



http://hack-note.com/monetize/books-sns/
https://stock.hack-note.com/stock-analyze/nikkei225-4183-mitsuikagaku-20210405/

vim ./static_sa/category/stock-analyze/9107-kawasakikisen/index.html

## データサイエンティストスクール 無料部分あります
PythonやRなどのプログラミングを学ぶなら、
さらに統計分野を学習してデータサイエンティストを目指すのがおすすめ！

ディープラーニングやビックデータ分析などの高額システム案件の受注にも有利になります。

システム開発より、分析がやりたい方向けですが、下記載せておきます。

https://hack-note.com/programming-schools/#toc17

　

## Python 関連のまとめ
https://hack-note.com/summary/python-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

