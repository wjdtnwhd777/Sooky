import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Myclass:
    def __del__(self):
        print('해당 클래스가 할당된 영역이 메모리에서 해제됩니다.')

obj = Myclass()
del obj
