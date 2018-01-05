import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Add:
    def __init__(self):
        print('init! Add!!')
    def __del__(self):
        print('del Add!')
    def add(self, n1, n2):
        return n1+n2

class Multiply:
    def __init__(self):
        print('init! Multiply!!')
    def __del__(self):
        print('del Multiply!')
    def mul(self, n1, n2):
        return n1*n2

class Calculator(Add, Multiply):
    def __init__(self):
        print('init! Calc!!')
    def __del__(self):
        print('del Calc!')
    def sub(self, n1, n2):
        return n1-n2

obj = Calculator()
print(obj.add(1,2))
print(obj.sub(1,2))
print(obj.mul(5,6))
del obj
