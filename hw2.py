
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    
    def introduce_myself(self):
        print(f"Полное имя: {self.fullname}, Возраст: {self.age}, Married: {self.is_married}")

class Student (Person):
    def __init__(self, fullname, age, is_married):
        super().__init__(fullname, age, is_married)

    def average_grade(self, grades):
       
        total = sum(grades.values())
        average = total / len(grades)
        print(f"Средняя оценка за {self.fullname}: {average}")   

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience
    
    def calculate_salary(self, base_salary):
        bonus = self.experience * 3000
        total_salary = base_salary + bonus
        return total_salary

student = Student("Камалова Гуласел",17, "Не замужем")

student.introduce_myself()

grades = {"Math": 85,
          "Physics": 90,
          "History": 80}

   
student.average_grade(grades)
teacher = Teacher("Токсонбаев Ислам", 20, "Не женатый", 2)
teacher.introduce_myself()
print( teacher.experience)
base_salary =100000
salary = teacher.calculate_salary(base_salary)
print(f"Зарплата: {salary}")

