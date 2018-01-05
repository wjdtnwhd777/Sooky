import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

numdata = 1
strdata = '파이썬'
listdata = [1,2,3]
dictdata = {'a':1,'b':2}

def func():
    print('hihihi!!')

func()
print(type(numdata))
print(type(strdata))
print(type(listdata))
print(type(dictdata))
print(type(func))
