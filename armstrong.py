a= int(input("Enter a number: "))
b=a
s=0
c=len(str(a))
while a>0:
    d=a%10
    s=s+(d**c)
    a=a//10
    
if b==s:
    print("The number is Amrstrong")
else:
    print("The number is not Amrstrong")
