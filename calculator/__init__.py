from calculator.operations import add, subtract, divide, multiply
from calculator.Calculation import Calculation

class Calculator:
    @staticmethod
    def add(a, b):
        calculation = Calculation(a ,b, add)
        return calculation.get_Output()
    
    @staticmethod
    def subtract(a, b):
        calculation = Calculation(a ,b, subtract)
        return calculation.get_Output()

    @staticmethod
    def multiply(a, b):
        calculation = Calculation(a ,b, multiply)
        return calculation.get_Output()
    
    @staticmethod
    def divide(a, b):
        calculation = Calculation(a, b, divide)
        return calculation.get_Output()