```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")
```


```python
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.greeting()  # Hello, my name is Alice and I am 25 years old.
person2.greeting()  # Hello, my name is Bob and I am 30 years old.
```


```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greeting(self):
        print("Hello, my name is", self.name, "and my student ID is", self.student_id)
```


```python
student1 = Student("Carol", 20, "12345")
student1.greeting()  # Hello, my name is Carol and my student ID is 12345.
```
