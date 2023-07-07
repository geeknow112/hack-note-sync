# ```python
my_dict = {"apple": 100, "banana": 200, "orange": 300}
print(my_dict["apple"]) # 100
# ```


# ```python
my_dict = {"apple": 100, "banana": 200, "orange": 300}
print(my_dict.get("apple")) # 100
# ```


# ```python
my_dict = {"apple": 100, "banana": 200, "orange": 300}
print("apple" in my_dict) # True
print("grape" in my_dict) # False
# ```


# ```python
my_dict = {"apple": 100, "banana": 200, "orange": 300}
my_dict["grape"] = 400
print(my_dict) # {"apple": 100, "banana": 200, "orange": 300, "grape": 400}
# ```


# ```python
my_dict = {"apple": 100, "banana": 200, "orange": 300}
my_dict["apple"] = 150
print(my_dict) # {"apple": 150, "banana": 200, "orange": 300}
# ```


# ```python
my_dict = {"apple": 100, "banana": 200, "orange": 300}
del my_dict["apple"]
print(my_dict) # {"banana": 200, "orange": 300}
# ```
