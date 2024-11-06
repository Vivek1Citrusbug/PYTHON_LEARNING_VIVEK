#----------------       Open / closed principle   -----------------------

# from abc import ABC, abstractmethod

# class Discount(ABC):
#     @abstractmethod
#     def apply_discount(self, amount):
#         pass

# class PercentageDiscount(Discount):
#     def __init__(self, percent):
#         self.percent = percent

#     def apply_discount(self, amount):
#         return amount * (1 - self.percent / 100)

# class FixedDiscount(Discount):
#     def __init__(self, discount_amount):
#         self.discount_amount = discount_amount

#     def apply_discount(self, amount):
#         return max(0, amount - self.discount_amount)

# discount = PercentageDiscount(10)
# print(discount.apply_discount(100))  

#------------ LSP principle ---------------

# class Bird:
#     def eat(self):
#         print("Eating")

# class FlyingBird(Bird):
#     def fly(self):
#         print("Flying")

# class Sparrow(FlyingBird):
#     pass

# class Penguin(Bird):
#     pass

# sparrow = Sparrow()
# sparrow.fly()     

# penguin = Penguin()
# penguin.eat()

#----------- Interface Segmentation --------------

# from abc import ABC, abstractmethod

# class Worker(ABC):
#     @abstractmethod
#     def work(self):
#         pass

# class Eater(ABC):
#     @abstractmethod
#     def eat(self):
#         pass

# class Programmer(Worker, Eater):
#     def work(self):
#         print("Coding")

#     def eat(self):
#         print("Eating lunch")

# class Robot(Worker):
#     def work(self):
#         print("Assembling parts")

# programmer = Programmer()
# programmer.work()  
# programmer.eat()   

# robot = Robot()
# robot.work()      
 


#------- DIP ( Dependency inversion principle ) ----------

# from abc import ABC, abstractmethod

# class Notifier(ABC):
#     @abstractmethod
#     def send(self, message):
#         pass

# class EmailNotifier(Notifier):
#     def send(self, message):
#         print(f"Sending email with message: {message}")

# class SMSNotifier(Notifier):
#     def send(self, message):
#         print(f"Sending SMS with message: {message}")

# class NotificationService:
#     def __init__(self, notifier: Notifier):
#         self.notifier = notifier

#     def notify(self, message):
#         self.notifier.send(message)

# notifier = EmailNotifier()
# service = NotificationService(notifier)
# service.notify("Welcome to our platform!")  

#-------------------------------->(    Decorators in python    )<----------------------------------------

# class Rectangle:
    
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     @property
#     def area(self):
#         return self.width * self.height
    
#     @classmethod
#     def create_square(cls, side_length):
#         return cls(side_length, side_length)
    
#     @staticmethod
#     def hello_world():
#         print("\nhello world")

# rect = Rectangle(4, 5)
# print(rect.area) 

# square = Rectangle.create_square(5)
# print(square.area) 

# Rectangle.hello_world()




