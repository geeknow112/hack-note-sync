# ```python
pip install pyinstaller
# ```


# ```python
pyinstaller --onefile (プログラム名).py
# ```


# ```python
# hello.py
print("Hello, World!")
# ```


# ```python
pyinstaller --onefile hello.py
# ```


# ```python
pip install cx-Freeze
# ```


# ```python
from cx_Freeze import setup, Executable

setup(name="(プログラム名)",
	version="(バージョン番号)",
	description="(プログラムの説明)",
	executables=[Executable("(プログラム名).py")])
# ```


# ```python
python setup.py build
# ```


# ```python
# hello.py
print("Hello, World!")
# ```


# ```python
# setup.py
from cx_Freeze import setup, Executable

setup(name="hello",
	version="1.0",
	description="Hello, World!",
	executables=[Executable("hello.py")])
# ```


# ```python
python setup.py build
# ```
