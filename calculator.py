class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b # B is swapped with A

    def multiply(self, a, b):
        result = 0
        if b >= 0:
            for i in range(b): # original error had b+1
                result = self.add(result, a)

        else:
            for i in range(abs(b)): # original error had b+1
                result = self.subtract(result, a)

        return result

    def divide(self, a, b):

        if b == 0:
            return "can not divide with 0"
        negacheck = (a < 0) ^ (b < 0)
        a, b = abs(a), abs(b)
        result = 1
        while a > b:
            a = self.subtract(a, b)
            result += 1
        if a != b:
            return result-1
        return -result if negacheck else result
    

    
    def modulo(self, a, b):
        nega = 0
        if b == 0:
            return "can not divide with 0"
        if a < 0:
            a = abs(a)
            nega = 1
        if b < 0:
            b = abs(b)
            nega = 1
            
        while a >= b:
            a = a-b
        return -a if nega == 1 else a 

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(6, 3))
    print("Example: modulo: ", calc.modulo(11, 3))