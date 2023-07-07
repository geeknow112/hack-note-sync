# ```python
import requests

def post_to_hatena_blog(title, body):
	# Hatena BlogのAPIエンドポイントを指定
	endpoint = "https://blog.hatena.ne.jp/{はてなID}/{ブログID}/atom/entry"

	# ユーザー名、ブログID、はてなIDを指定
	username = "ユーザー名"
	blog_id = "ブログID"
	hatena_id = "はてなID"

	# リクエストヘッダーに認証情報を追加
	auth = (hatena_id, "APIキー")

	# リクエストボディに記事のタイトルと本文を指定
	data = {"title": title, "content": body}

	# Hatena Blogに記事を投稿
	response = requests.post(endpoint.format(username, blog_id), auth=auth, data=data)
# ```


# ```python
title = "PythonでHatena Blogに自動投稿する方法"
body = """
PythonコードでHatena Blogに自動投稿する方法を紹介します。
"""
# ```


# ```python
def set_custom_url(username, custom_url):
	base_url = f"https://{username}.hatenablog.com/"
	url = base_url + custom_url
	response = requests.put(url)
# ```
