
class Calculator:
    
        
        
    def add(self, x, y):
        self.__add = x +y
        return self.__add
    def subtract(self, x, y):
        self.__subtract = x - y
        return self.__subtract
    def multiply(self, x, y):
        self.__multiply = x * y
        return self.__multiply
        
    def divide(self, x, y):
        if y == 0:
            print("You can't divide by zero!")
        else:
            self.__divide = x/y
            return self.__divide
        
        
