#PRIME NUMBER CHECK
def prime_check():

    n=int(input('enter thenumber'))
    c=1
    while n>1:
        if n%2==0:
            c=c+1
    if c==2:
        print('prime')
    else:
        print('not prime')
prime_check()

