# ООП- принцип Aбстракции
from abc import ABC,abstractmethod
# # Абстрактный класс
# class Payment(ABC):
#     @abstractmethod
#     def process_payment(seldf,amount):
#         pass
# #конкретный класс для обработки платеж       
# class CreditCardPayment(Payment):
#     def process_payment(seldf, amount):
#         return print(f"Оплата произведена по Кредитой карте, на сумму {amount}$")
    
# # Конкретный класс для обработки платеж   
# class PayPALPayment(Payment):
#     def process_payment(seldf, amount):
#         return print(f"Оплата произведена по Paypai, на сумму {amount}$")
    
# # Функция для принятия платеж
# def make_payment(payment_method,amount):
#     payment_method.process_payment(amount)
 
# #Создаем  обьект разных видов платеж
# credit_card_payment=CreditCardPayment()
# paypal=PayPALPayment()

# # Выполняем платежи
# make_payment(credit_card_payment,100)
# make_payment(paypal,200)
    

# class Pet(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog (Pet):
#     def make_sound(self):
#         print("Woof")
    
# class Cat (Pet):
#     def make_sound(self):
#         print("Meow")

# def play_with_pet(pet):
#     pet.make_sound()

# dog=Dog()
# cat=Cat()

# print("Играть с собакой:")
# play_with_pet(dog)

# print("Играть с кошкой:")
# play_with_pet(cat)

# ПОЛИМОРФИЗМ
# class Cat:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def indo(self):
#         print(f"Я кошка. Меня зовут{self.name}.Мне {self.age} лет")
        
#     def make_sound(self):
#         print("Weow")
    
# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def indo(self):
#         print(f"Я собака. Меня зовут{self.name}.Мне {self.age} лет")
        
#     def make_sound(self):
#         print("woof") 
        
# cat1=Cat("Мурка",2)
# dog1=Dog('АК-Тош',4)

# for animal in (cat1,dog1):
#     animal.make_sound()
#     animal.info()
     

# from math import pi



# class Shape:
#     def __init__(self,name):
#         self.name=name
        
#     def area(self):
#             pass
        
#     def fact(self):
#             return"Я двуменная фигура"
        
#     def __str__(self):
#         return self.name
    
# class Square(Shape):
#     def __init__(self,length):
#         super().__init__("Square")
#         self.length=length
        
#     def area(self):
#         pass
    
#     def fact(self):
#         return "У квадрата каждой угол равен на 90 градусам"
        
# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__("Circle")
#         self.radius=radius
        
#     def area(self):
#         return pi*self.radius**2
    
# a=Square(4)
# b=Circle(10)
# print(b)
# print(a.fact())
# print(b.fact())  
# print(b.area())



# Инкапсуляция
# Python 3 предоставляет 3 уровня доступа к данным:


# публичный (public, нет особого синтаксиса, publicBanana);
# защищенный (protected, одно нижнее подчеркивание в начале названия, _protectedBanana);
# приватный (private, два нижних подчеркивания в начала названия, __privateBanana).

# Для краткости и простоты, только два базовых уровня (приватный и публичный) освещены в примере.

# class Phone:
#     username = "Kate"                # public variable
#     __how_many_times_turned_on = 0   # private variable

#     def call(self):                  # public method
#         print( "Ring-ring!" )

#     def __turn_on(self):             # private method
#         self.__how_many_times_turned_on += 1 
#         print( "Times was turned on: ", self.__how_many_times_turned_on )

# my_phone = Phone()

# my_phone.call()
# print( "The username is ", my_phone.username )
# # my_phone.turn_on()
# # my_phone.__turn_on()
# # print( “Turned on: “, my_phone.__how_many_times_turned_on)
# # print( “Turned on: “, my_phone.how_many_times_turned_on)
# # will produce an error
# input( "Press Enter to exit" )     


# class Human:
#     __age=0
#     name="Human"
    
# human= Human()
# human.age=-1
# print(human.age)






