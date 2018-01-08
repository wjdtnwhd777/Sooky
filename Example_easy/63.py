import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

a = 111113
b = 23
ret1, ret2 = divmod(a,b)
print('<%d/%d>는 몫이 <%d> 나머지가 <%d>입니다.' %(a,b,ret1,ret2))
