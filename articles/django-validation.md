【django】フォームの使い方とバリデーションの実装方法
python,django
django-validation

## djangoのフォームとは？
djangoのフォームは、ユーザーからの入力データを受け取り、処理するための重要な要素です。フォームを使用することで、簡単にデータのバリデーションやデータベースへの保存などを実現することができます。

参考記事：
- [djangoの公式ドキュメント - フォーム](https://docs.djangoproject.com/en/3.0/topics/forms/)
- [django formsの書き方【初心者向け】](https://hibiki-press.tech/django/basic/django_form)

## フォームの基本的な作成方法とは？
フォームを作成するには、まず`forms.py`というファイルを作成します。このファイルには、フォームの定義とバリデーションルールを記述します。

```python
from django import forms

class myform(forms.form):
    name = forms.charfield(max_length=100)
    email = forms.emailfield()
    age = forms.integerfield(min_value=0, max_value=100)
```

この例では、`name`、`email`、`age`という3つのフィールドを持つフォームを定義しています。`charfield`は文字列、`emailfield`はメールアドレス、`integerfield`は整数値を入力するためのフィールドです。

参考記事：
- [djangoの公式ドキュメント - フォームフィールド](https://docs.djangoproject.com/en/3.0/ref/forms/fields/)
- [djangoのformクラスまとめ](https://qiita.com/okoppe8/items/293b17a4a821c94efae4)

## フォームのバリデーションとは？
フォームのバリデーションとは、ユーザーが入力したデータが所定の条件を満たしているかどうかを検証することです。例えば、必須項目の入力漏れやメールアドレスの形式など、入力値に対してルールを設定し、検証することができます。

参考記事：
- [djangoの公式ドキュメント - バリデーション](https://docs.djangoproject.com/en/3.0/ref/forms/validation/)
- [djangoのバリデーションの基本まとめ](https://note.mu/hiroyuki007/n/n35f842dae13e)

## バリデーションの実装方法とは？
バリデーションを実装する方法としては、主に2つの方法があります。一つ目は、`forms.py`内で個別にバリデーションルールを設定する方法であり、もう一つは、`clean_フィールド名`というメソッドを使用してバリデーションを行う方法です。

```python
from django import forms

class myform(forms.form):
    name = forms.charfield(max_length=100)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.validationerror("名前は3文字以上で入力してください。")
        return name
```

上記の例では、`name`フィールドに対して、3文字以上であることを検証しています。

参考記事：
- [djangoの公式ドキュメント - 単一フィールドのバリデーション](https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-a-specific-field-attribute)
- [djangoのバリデーションのルールと正規表現のまとめ](https://qiita.com/silencershop/items/7c43fee782f2a0869b24)

## フォームの表示方法とエラーメッセージの取得方法
フォームをhtml上に表示するには、ビューからテンプレートにフォームを渡し、テンプレート側で表示する必要があります。フォームのエラーメッセージを表示する場合には、`form.errors`を使用してエラーメッセージを取得することができます。

```python
from django.shortcuts import render
from .forms import myform

def my_view(request):
    form = myform()
    if request.method == 'post':
        form = myform(request.post)
        if form.is_valid():
            # フォームのデータを処理する
            pass
    return render(request, 'my_template.html', {'form': form})
```

```html
<!-- my_template.html -->
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">送信</button>
</form>
```

上記の例では、`form.as_p`というテンプレートタグを使用して、フォームを段落(`<p>`)要素として表示しています。また、`form.errors`を使用してエラーメッセージを表示することもできます。

参考記事：
- [djangoの公式ドキュメント - フォームの表示](https://docs.djangoproject.com/en/3.0/topics/forms/#displaying-a-form)
- [djangoのテンプレートタグ - formタグ](https://docs.djangoproject.com/en/3.0/topics/forms/#rendering-fields-manually)

## フォームの送信と処理の方法
フォームの送信と処理の方法は、主に2つあります。一つ目は、`request.method == 'post'`という条件分岐を使用して、フォームがpostメソッドで送信された場合の処理を記述する方法です。もう一つは、`form.is_valid()`メソッドを使用してフォームのバリデーションを行い、バリデーションが成功した場合の処理を記述する方法です。

```python
from django.shortcuts import render
from .forms import myform

def my_view(request):
    form = myform()
    if request.method == 'post':
        form = myform(request.post)
        if form.is_valid():
            # フォームのデータを処理する
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # ここでデータの保存などの処理を行う
            pass
    return render(request, 'my_template.html', {'form': form})
```

上記の例では、`request.method == 'post'`の場合にフォームの送信処理を行っています。また、`form.is_valid()`を使用してバリデーションが成功した場合にのみフォームのデータを取得して処理を行っています。

参考記事：
- [djangoの公式ドキュメント - フォームの処理](https://docs.djangoproject.com/en/3.0/topics/forms/#processing-the-data-from-a-form)
- [djangoでフォームの値を取得する方法まとめ](https://qiita.com/silencershop/items/c255b7ebf9c71be5d99e)

　

## Django 関連のまとめ
https://hack-note.com/summary/django-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

