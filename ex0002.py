#Bank Loan Program

name = str(input('What is your name? ')).strip().lower().capitalize().rstrip()
print(f'Hello and welcome, {name}! I am the Loan Program! I will help you as best I can.')

thing = str(input('What you want loan? '))
price = float(input('What is the price? '))
wage = float(input('What is your wage? '))
print('Ask to the buyer in how much time he want to finance.')
payment = str(input('Do you want to pay in M (months) or Y (years)? ')).strip().lower().rstrip()
payment2 = int(input('How many time? '))
account = wage * 30 / 100

if payment == 'm':
    price1 = price / payment2
    if price1 == account:
        print(f'Your loan was accept. Congratulations, {name}.')
        print(f'Your installment gonna be R$ {price1:.2f}.')
    elif price1 < account:
        print(f'Your loan was accept. Congratulations, {name}.')
        print(f'Your installment gonna be R$ {price1:.2f}.')
    else:
        print('Your loan was not accept. Try later.')
        print(f'Your portion would be R$ {price1:.2f} monthly.')
        print(f'But, with your wage, you was could a portion at most R$ {account:.2f} monthly.')

elif payment == 'y':
    price1 = price / payment2 / 12
    if price1 == account:
        print(f'Your loan was accept. Congratulations, {name}.')
        print(f'Your installment gonna be R$ {price1:.2f}.')
    elif price1 < account:
        print(f'Your loan was accept. Congratulations, {name}.')
        print(f'Your installment gonna be R$ {price1:.2f}.')
    else:
        print('Your loan was not accept. Try later.')
        print(f'Your portion would be R$ {price1:.2f} monthly.')
        print(f'But, with your wage, you was could a portion at most R$ {account:.2f} monthly.')

else:
    print('Type another value.')
