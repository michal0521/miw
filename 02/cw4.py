class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def difference(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise Exception('Cannot divide by 0')
        
        result = a / b
        
        return '{:.4f}'.format(result)
    
class ScientificCalculator(Calculator): 
    @staticmethod
    def power(a, power):
        return a**power
    
print(ScientificCalculator.add(5, 2))

    