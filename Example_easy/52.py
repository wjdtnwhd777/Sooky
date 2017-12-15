import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Myclass:
    def __init__(self, txt):
        self.var = txt
        print('txt == '+txt)

obj = Myclass('Hi!')
print(obj.var)
