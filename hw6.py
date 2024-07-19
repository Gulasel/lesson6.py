# class MagicCalculator:
#     def __init__(self, number_1, number_2):
#         self.number_1 = number_1
#         self.number_2 = number_2
    
#     def __add__(self, other):
#         return MagicCalculator(self.number_1 + other.number_1, self.number_2 + other.number_2)
    
#     def __sub__(self, other):
#         return MagicCalculator(self.number_1 - other.number_1, self.number_2 - other.number_2)
    
#     def __mul__(self, other):
#         return MagicCalculator(self.number_1 * other.number_1, self.number_2 * other.number_2)
    
#     def __truediv__(self, other):
#         if other.number_1 == 0 :
#             raise ValueError("Деление на ноль нельзя.")
#         return MagicCalculator(self.number_1 / other.number_1, self.number_2 / other.number_2)
    
#     def __floordiv__(self, other):
#         if other.number_1 == 0:
#             raise ValueError("Деление на ноль нельзя")
#         return MagicCalculator(self.number_1 // other.number_1, self.number_2 // other.number_2)
    
#     def __str__(self):
#         return f"({self.number_1}, {self.number_2})"


# num1 = MagicCalculator(10,40)
# num2 = MagicCalculator(2,4)


# result_add = num1 + num2
# print("Сложение:", result_add.number_1, result_add.number_2)  

# result_add = num1 - num2
# print("Вычитание:", result_add.number_1, result_add.number_2)

# result_add = num1 + num2
# print("Умножение:", result_add.number_1, result_add.number_2)

# result_add = num1 / num2
# print("деление:", result_add.number_1, result_add.number_2)


