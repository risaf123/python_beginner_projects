import time

mytime = int(input('Enter the time in seconds: '))

for i in reversed(range(1, mytime + 1)):
    seconds = i % 60
    minutes = (i // 60) % 60
    hours = i // 3600

    print(f'{hours:02}:{minutes:02}:{seconds:02}', end='\r')
    time.sleep(1)

print("\nTime's up!")
