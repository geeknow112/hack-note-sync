# ```python
text = "apple"
new_text = text.replace("a", "b")
print(new_text)
# ```


# ```python
text = "I love apple"
new_text = text.replace("apple", "orange")
print(new_text)
# ```


# ```python
import re

text = "I love apples and bananas"
new_text = re.sub(r"app\w+", "orange", text)
print(new_text)
# ```


# ```python
text = "I love apples and bananas"
new_text = text[:7] + "oranges" + text[13:]
print(new_text)
# ```

