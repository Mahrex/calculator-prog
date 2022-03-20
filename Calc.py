import math

class Calculator():
    
    # Basic functions of a calculator!
    def give_sum(self,a,b):
        return a + b
    
    def give_sub(self,a,b):
        return a - b
    
    def give_product(self,a,b):
        return a * b
    
    def give_div(self,a,b):
        return a / b
    
    def give_fact(self,a):
        return math.factorial(a)
    
    def give_square(self,a):
        return a*a
    
    def give_squareroot(self,a):
        return math.sqrt(a)