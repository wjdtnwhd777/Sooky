import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

k = input('<값>을 입력해주세요.')
print('당신이 입력한 값은 <' + k + '> 입니다.')
