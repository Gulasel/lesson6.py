# ООП - обьектно ориентированние программирование

# class Person:
#     def __init__(self,name,age,surname):
#         self.name=name
#         self.age=age
#         self.surname=surname
        
#     def info(self):
#         print(f"Имя:{self.name},Возраст:{self.age},Фамилия:{self.surname}")
    
# gulasel=Person("Gulasel",17,"Kamalova")
# gulasel.info()
    

# class Car:
#     def __init__(self,model,year,color,volume):
#         self.model=model
#         self.year=year
#         self.color=color
#         self.volume=volume
        
#     def info(self):
#         print(f"Модель машины:{self.model},Год выпуска:{self.year},Цвет:{self.color},Обьем:{self.volume}")
        
# bmw=Car ('BMW','2016','black','2.5')
# lexus=Car ('Lexus','2023','white','4')
# bmw.info()        
# lexus.info()
        

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def plus(self):
        print(F"Ответ:{self.num1+self.num2}")
        
    def minus(self):
        print(F"Ответ:{self.num1-self.num2}")
calc=Calculator(2,2)
calc.plus()
calc.minus()
        
        