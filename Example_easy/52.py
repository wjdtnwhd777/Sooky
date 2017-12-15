import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Myclass():
    def __init__(self):
        self.var="안녕하세요!"
        print("Myclass 인스턴스 객체가 생성되었습니다.")

obj = Myclass()
print(obj.var)
