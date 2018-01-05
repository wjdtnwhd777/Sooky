import time

count = 1
try:
    while True:
        print(count)
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt: #ctrl + c 가 입력되면 종료됨
    print('종료!')
