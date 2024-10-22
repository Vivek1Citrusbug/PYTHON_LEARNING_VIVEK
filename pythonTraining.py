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

class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks" 
    def returnPrivateMember(self):
        print("Inside function")
        return self.__c

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class: ")
        print("Private member : ",self.returnPrivateMember())

obj1 = Derived()
print(obj1.a)
