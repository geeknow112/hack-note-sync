【Python】exe化する方法
Python,exe化
python-generate-exe

こんにちは。今回は、Python初心者に向けて、Pythonプログラムをexeファイルに変換する方法について解説します。

## exe化とは

exe化とは、PythonプログラムをWindowsの実行ファイルであるexeファイルに変換することです。exeファイルに変換することで、Python環境がない他のコンピュータでもPythonプログラムを実行することができます。

## PyInstallerを使用したexe化方法

Pythonプログラムをexeファイルに変換する方法はいくつかありますが、ここでは、PyInstallerを使用する方法を紹介します。PyInstallerは、Pythonのスクリプトを単一のexeファイルにパッケージ化するためのツールです。

### PyInstallerのインストール方法

まず、PyInstallerをインストールする必要があります。以下のコマンドを使用して、PyInstallerをインストールできます。

```python
pip install pyinstaller
```

### exe化手順

PyInstallerを使用して、Pythonプログラムをexeファイルに変換する手順は以下の通りです。

1. exe化したいPythonプログラムを準備する
2. コマンドプロンプトを開き、プログラムがあるディレクトリに移動する
3. 以下のコマンドを実行する

```python
pyinstaller --onefile (プログラム名).py
```

4. 上記のコマンドを実行すると、distという名前のディレクトリが作成され、その中にexeファイルが生成されます。

### 注意点

PyInstallerを使用する際には、以下の点に注意する必要があります。

- プログラムに使用しているライブラリが正しくパッケージ化されていることを確認する
- プログラムが正常に動作するか、exeファイルで実行して確認する
- PyInstallerがアップデートされた場合、パッケージ化する前に再度インストールする必要がある

### サンプルコード

以下は、PyInstallerを使用して、Pythonプログラムをexeファイルに変換するサンプルコードです。

```python
# hello.py
print("Hello, World!")
```

上記のプログラムをexeファイルに変換する場合は、以下のコマンドを実行します。

```python
pyinstaller --onefile hello.py
```

## cx_Freezeを使用したexe化方法

PyInstaller以外にも、Pythonプログラムをexeファイルに変換するためのツールがあります。ここでは、cx_Freezeを使用する方法を紹介します。

### cx_Freezeのインストール方法

cx_Freezeをインストールするには、以下のコマンドを使用します。

```python
pip install cx-Freeze
```

### exe化手順

cx_Freezeを使用して、Pythonプログラムをexeファイルに変換する手順は以下の通りです。

1. exe化したいPythonプログラムを準備する
2. setup.pyという名前のファイルを作成する
3. setup.pyに以下の内容を記述する

```python
from cx_Freeze import setup, Executable

setup(name="(プログラム名)",
      version="(バージョン番号)",
      description="(プログラムの説明)",
      executables=[Executable("(プログラム名).py")])
```

4. コマンドプロンプトを開き、プログラムがあるディレクトリに移動する
5. 以下のコマンドを実行する

```python
python setup.py build
```

6. 上記のコマンドを実行すると、buildという名前のディレクトリが作成され、その中にexeファイルが生成されます。

### 注意点

cx_Freezeを使用する際には、以下の点に注意する必要があります。

- setup.pyの記述が正しいか確認する
- プログラムが正常に動作するか、exeファイルで実行して確認する

### サンプルコード

以下は、cx_Freezeを使用して、Pythonプログラムをexeファイルに変換するサンプルコードです。

```python
# hello.py
print("Hello, World!")
```

以下は、上記のプログラムをexeファイルに変換するためのsetup.pyのサンプルコードです。

```python
# setup.py
from cx_Freeze import setup, Executable

setup(name="hello",
      version="1.0",
      description="Hello, World!",
      executables=[Executable("hello.py")])
```

上記のプログラムをexeファイルに変換する場合は、以下のコマンドを実行します。

```python
python setup.py build
```

## まとめ

本記事では、Pythonプログラムをexeファイルに変換する方法について、PyInstallerとcx_Freezeを使用した方法を紹介しました。どちらの方法も簡単に実行することができますが、プログラムに使用しているライブラリや、setup.pyの記述に注意する必要があります。Pythonプログラムをexeファイルに変換することで、Python環境がない他のコンピュータでもPythonプログラムを実行することができます。

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

