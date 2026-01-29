import time
mytime=int(input('enter the time'))
for i in reversed (range(0,mytime)):
    seconds=i%60
    minutes=int(i/60)%60
    hours=int(i/3600)


    print(f'{hours:02}.{minutes:02}.{seconds:02}')
    time.sleep(1)



