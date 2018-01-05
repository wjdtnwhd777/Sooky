import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


try:
    print('hi!')
    #print(param)
except:
    print('예외가 발생했어요')
else: #예외가 발생하지 않으면 실행
    print('예외가 발생하지 않았어요')
