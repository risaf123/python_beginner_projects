#THEATRE SHOPPING CART
menu={'pizza':23,'popcorn':15,'Laddu':14,'burger':32,'sandwitch':15,}
total=0
cart=[]
print('_________________')
for key,value in menu.items():
    print(key,value)
print('_________________')
while True:
    food=input('enter you =r item(q to quit): ').lower()
    if food=='q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total+=menu.get(food)
    print(food,end=' ')
print()
print('_________________')
print('total is',total)