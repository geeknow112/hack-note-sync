# ```python
import json

# JSON形式の文字列
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# JSON形式の文字列をPythonのデータ型に変換する
data = json.loads(json_string)

# データ型を表示する
print(type(data)) # <class 'dict'>
print(data["name"]) # John
# ```


# ```python
import json

# Pythonのデータ型
data = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# Pythonのデータ型をJSON形式の文字列に変換する
json_string = json.dumps(data)

# JSON形式の文字列を表示する
print(json_string) # {"name": "John", "age": 30, "city": "New York"}
# ```
