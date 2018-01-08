import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

a = 111113
b = 23
ret = a%b
print('<%d>를 <%d>로 나누면 <%d>가 남습니다.' %(a,b,ret))
