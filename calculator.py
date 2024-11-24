class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(2, 2))
    print("Example: addition: ", calc.add(1, 3))
    print("Example: subtraction: ", calc.subtract(6, 2))
    print("Example: subtraction: ", calc.subtract(8, 3))
    print("Example: multiplication: ", calc.multiply(1, 9))
    print("Example: multiplication: ", calc.multiply(12, 12))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: division: ", calc.divide(12, 13))
    print("Example: modulo: ", calc.modulo(10, 2))
    print("Example: modulo: ", calc.modulo(10, 11))