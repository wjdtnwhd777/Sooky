import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class Myclass:
    def sayHello(self):
        print('안녕하세요')

    def sayBye(self, name):
        print('%s! 잘가!' %name)

obj = Myclass()
obj.sayHello()
obj.sayBye('Sooky!')
