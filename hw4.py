class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    
    def __make_computations(self, operation):
        if operation == '+':
            result = self.__cpu + self.__memory
        elif operation == '-':
            result = self.__cpu - self.__memory
        elif operation == '*':
            result = self.__cpu * self.__memory
        elif operation == '/':
            result = self.__cpu / self.__memory
        else:
            result = None
        
        if result is not None:
            print(f"Результат {self.__cpu} {operation} {self.__memory} = {result:.2f}")

    def get_cpu(self):
        return self.__cpu
    
    def get_memory(self):
        return self.__memory
    
    def info(self):
        print(f" Процессор - {self.__cpu}, Память - {self.__memory}")


class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card
    
    def get_memory_card(self):
        return self.__memory_card
    
    def info(self):
        super().info()
        print(f"Карта памяти - {self.__memory_card}")


comp1 = Computer(3,8)
comp1.info()
comp1._Computer__make_computations('+')  

laptop1 = Laptop(2,16,'512 GB')
laptop1.info()
laptop1._Computer__make_computations('/')  

