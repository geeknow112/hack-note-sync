# ```python
num = int(input("整数を入力してください: "))
if num % 2 == 0:
	print("{0}は偶数です".format(num))
else:
	print("{0}は奇数です".format(num))
# ```


# ```python
string = input("文字列を入力してください: ")
reverse_str = string[::-1]
print(reverse_str)
# ```


# ```python
import random

lst = [random.randint(1, 100) for _ in range(10)]
print("ソート前のリスト: ", lst)

lst.sort()

print("ソート後のリスト: ", lst)
# ```
