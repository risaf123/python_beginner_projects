#COMPUND INTEREST CALCULATOR
principle=0
time=0
rate=0
while True:
    principle=float(input('enter the value'))
    if principle<0:
        print('principle cant be zero')
    else:
        break
while True:
    time=int(input('enter the time'))
    if time<0:
        print('time cant be zero')
    else:
        break
while True:
    rate=float(input('enter the rate'))
    if rate<0:
        print('rate cant be zero')
    else:
        break
total=principle * pow((1 + rate / 100),time)
print(f'Total compound interest after{time} is{total}')