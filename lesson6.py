# """ Магические методы - dinner  методы"""

# class Work:
#     def __init__(self,position,graphicks):
#         self.position=position
#         self.graphicks=graphicks
        
#     def info(self):
#         print(f" Позиция-{self.position}, график-{self.graphicks}")

#     def __repr__(self):
#          return (f" Позиция-{self.position}, график-{self.graphicks}")
     
#     # def __str__(self):
#     #      return 2+2
         
        
    
    
# work=Work("Бухгалтер","8/5")
# work.info()
# print(work)


# """Магические методы - dunder методы"""

# from typing import Any


# class Work:
    # def __init__(self, position, graphicks):
    #     self.positon = position
    #     self.graphicks = graphicks
    
    # def info(self):
    #     print(f"Позиция - {self.positon}, график - {self.graphicks}")
        
    # def __repr__(self):
    #      return f"Позиция - {self.positon}, график - {self.graphicks}"
     
    # def __str__(self):
    #     return f"Позиция - {self.positon}, график - {self.graphicks}"
    
    # def __call__(self):
    #     print("Это магический метод __call__")
         
        
# work = Work("Бухгалтер", "8/5")
# print(work)
# work()
# work.info()


# def work():
#     print ("hello")

# print(work())


class Math:
    def __init__(self,number_1,number2):
        self.number_1=number_1
        self.number_2=number2
            
    def __str__(self):
        return f"Первое значение {self.number_1},\nВторое значение{self.number_2}"
    
    def __add__(self,other):
        print(f'Результат сложение{self.number_1} и {self.number_2} ')
        return Math(self.number_1 + other.number_1,self.number_2)


    def __sub__(self,other):
        print(f'Результат вычитание{self.number_1} и {self.number_2} ')
        return Math(self.number_1 - other.number_1,self.number_2)
 
    def __mul__(self,other):
        print(f'Результат умножение{self.number_1} и {self.number_2} ')
        return Math(self.number_1 * other.number_1,self.number_2)


    def __truediv__(self,other):
        print(f'Результат деление{self.number_1} и {self.number_2} ')
        return Math(self.number_1 / other.number_1,self.number_2)
    

math_number_1=int(input("Введите первое число:"))
math_number_2=int(input("Введите второе число:"))























