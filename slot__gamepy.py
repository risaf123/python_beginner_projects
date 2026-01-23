#***SLOT GAME***

import random
print('hello')
def spin_row():
    symbols=['💕','😘','😎','🤷‍♂️','😍',]
    return[random.choice(symbols) for _ in range(3)]



def print_row(row):
    print(' | '.join(row))


def get_payment(row,bet):

    if row[0]==row[1]==row[2]:
        if row[0]=='💕':
            return bet*3

        if row[0]=='😘':
            return bet*4
        if row[0]=='😎':
            return bet*5
        if row[0]=='🤷‍♂️':
            return bet*10
        if row[0]=='😍':
            return bet*20
    return 0
def main():
    balance=int(input('enter the balance'))
    while balance>0:
        print(f'the current amount in hand{balance}')

        bet=int(input('enter the amount'))

        
        if bet<=0:
            print('Insufficient bet amount')
        if bet> balance:
            print('Insufficient balance')

        balance-=bet
    
    
        row=spin_row()
        print('Spinning')
        print_row(row)
        payout = get_payment(row, bet)
        


        if payout>0:
            print(f'You have won{payout}')
        else:
            print('You lost')
        
        balance+=payout

        play_again=input('You want to play more(y/n)').lower()
        
        if play_again!='y':
            break

 
if __name__ == '__main__':

    main()

