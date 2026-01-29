#SHOPPING CART PROGRAM
foods=[]
prices=[]
total=0
while True:
    food=input('enter the food items(q to quit)')
    if food.lower=='q':
        break
    else:
        price=float(input('enter the price'))
        foods.append(food)
        prices.append(price)
print("MYCART")
for food in foods:
    print(food,end= '')
for price in prices:
    total += price
print(f'total price of the food is {total}')
