class Person:
    #생성자 메서드: 객체 생성시 호출
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #인스턴스 메서드
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.age)
print(person1.name)
print(person1.greet())

print(type(person1))