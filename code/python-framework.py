'''```python'''
# Djangoのインストール
pip install Django

# プロジェクトの作成
django-admin startproject mysite

# アプリケーションの作成
python manage.py startapp myapp
'''```'''


'''```python'''
# myapp/views.pyに下記のコードを記述する
from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello World!")
'''```'''


'''```python'''
# mysite/urls.pyに下記のコードを記述する
from django.urls import path
from myapp.views import hello

urlpatterns = [
	path('hello/', hello),
]
'''```'''


'''```python'''
# サーバーの起動
python manage.py runserver
'''```'''


'''```python'''
# Flaskのインストール
pip install Flask
'''```'''


'''```python'''
# app.pyに下記のコードを記述する
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, World!'
'''```'''


'''```python'''
# アプリケーションの起動
if __name__ == '__main__':
	app.run()
'''```'''
