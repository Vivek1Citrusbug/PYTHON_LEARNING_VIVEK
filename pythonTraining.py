# text = "  hello Vivek Soni here  "

# print(text.upper())
# print(text.lower())
# print(text.find('Vivek'))
# print(text.encode())

# class Dog:
#     attr1 = 'mammal'
#     def __init__(self,name):
#         self.name = name

# rodger = Dog("Rodger")
# tommy = Dog("Tommy")

# print(f'Rodger : {rodger.attr1}')
# print(f'Tommy is also a {tommy.attr1}')
# print(f'Rodger : {rodger.name}')
# print(f'Tommy : {tommy.name}')

# class person:
#     def __init__(self,name,idnumber):
#         self.name = name
#         self.idnumber = idnumber
    
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
    
# class employee(person):
#     def __init__(self, name, idnumber,salary, post):
#         super().__init__(name, idnumber)
#         self.salary = salary
#         self.post = post

#     def details(self):
#         print(self.name)
#         print(self.salary)
#         print(self.post)

# obj1 = employee('Vivek Soni',123,50000,'Jr Engineer')
# obj1.details()

# class Bird:
#     def intro(self):
#         print("There are many types of birds.")
#     def flight(self):
#         print("Most of the birds can fly but some cannot.")

# class sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly.")

# class ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly.")

# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()

# class Base:
#     def __init__(self):
#         self.a = "GeeksforGeeks"
#         self.__c = "GeeksforGeeks" 
#     def returnPrivateMember(self):
#         print("Inside function")
#         return self.__c

# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         print("Private member : ",self.returnPrivateMember())

# obj1 = Derived()
# print(obj1.a)


## Dictionary methods revision:

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.get('model')
# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) 

# car["color"] = "white"

# print(x) 

# y = car.values()

# print(y)

# if 'model' in car:
#     print("Yes, model is key in dictionary")

# car.pop('model')

# if 'model' in car:
#     print("Yes, model is key in dictionary")
# else:
#     print("No its not present")

# for i in car:
#     print(i,car[i])

# my_family = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# for i in my_family:
#     print(i,' : ')
#     for j in my_family[i]:
#         print('\t', j,' : ',my_family[i][j])

# from collections import deque

# data: deque = deque()
# data.append('1st')
# data.append('2nd')
# data.append('3rd')
# data.append('4th')
# data.append('5th')

# data.popleft()
# data.popleft()
# data.popleft()

# print(data)

from queue import LifoQueue

# Initializing a stack
stack:LifoQueue = LifoQueue(maxsize=3)
print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')

print(stack.full())
print(stack.empty())
print(stack.qsize())

print(stack.get_nowait())
print(stack.get_nowait())
print(stack.get_nowait())

print(stack.empty())