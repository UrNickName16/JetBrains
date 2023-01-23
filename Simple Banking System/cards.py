from random import sample
from db import create_connection, init_table
from luhn import luhn, check_luhn


connection = create_connection('card')
cursor = connection.cursor()
init_table(connection)


def create_card():
    while True:
        card = luhn('400000' + ''.join(str(i) for i in(sample(range(10), 9))))
        cursor.execute(f'SELECT number FROM card WHERE number = {card};')

        if cursor.fetchone() == None:
            break
    
    pin = ''.join(str(i) for i in sample(range(10), 4))
  
    cursor.execute(f'INSERT INTO card (number, pin) VALUES ({card}, {pin});')

    connection.commit()

    print('\nYour card has been created')
    print('Your card number:')
    print(card)
    print('Your card PIN:')
    print(pin)
    print()


def log_in():
    print('\nEnter your card number: ')
    card = input()

    print('Enter your PIN:')
    pin = input()

    cursor.execute(f'SELECT balance FROM card WHERE (number = {card} AND pin = {pin});')
    balance = cursor.fetchone()

    if balance is None:
        print('\nWrong card number or PIN!\n')
        return

    print('\nYou have successfully logged in!\n')

    while True:
        exit_code = acc_menu(card)
        if exit_code == 1:
            return 1
        if exit_code == 0:
            return 


def acc_menu(card):
    cursor.execute(f'SELECT balance FROM card WHERE number = {card};')
    balance = cursor.fetchone()[0]

    print('1. Balance')
    print('2. Add income')
    print('3. Do transfer')
    print('4. Close account')
    print('5. Log out')
    print('0. Exit')

    answer = input()

    if answer == '1':
        print(f'\nBalnce: {balance}\n')
        return
    
    if answer == '2':
        print('\nEnter income:')
        income = input()

        balance = str(int(balance) + int(income))

        cursor.execute(f'UPDATE card SET balance = {balance} WHERE number = {card}')
        connection.commit()
        print('Income was added!\n')
        return
    
    if answer == '3':
        print('\nTransfer')
        print('Enter card number:')
        destination = input()

        if destination == card:
            print("\nYou can't transfer money to the same account!\n")
            return
        
        if len(destination) == 16 and not check_luhn(destination):
            print('\nProbably you made a mistake in the card number. Please try again!\n')
            return
        
        cursor.execute(f'SELECT balance FROM card WHERE number = {destination}')
        if cursor.fetchone() == None:
            print('\nSuch a card does not exist.\n')
            return

        cursor.execute(f'SELECT balance FROM card WHERE number = {destination}')
        destination_balance = cursor.fetchone()[0]

        print('Enter how much money you want to transfer:')
        amount = int(input())

        if amount <= 0:
            print("\nValue can't be equal or lower then 0!\n")
            return

        if amount > int(balance):
            print('\nNot enough money!\n')
            return

        cursor.execute(f'UPDATE card SET balance = {int(balance) - amount} WHERE number = {card}')
        cursor.execute(f'UPDATE card SET balance = {int(destination_balance) + amount} WHERE number = {destination}')
        connection.commit()

        print('\nSuccess!\n')
        return
    
    if answer == '4':
        cursor.execute(f'DELETE FROM card WHERE number = {card};')
        connection.commit()

        print('\nThe account has been closed!\n')
        return 0

    if answer == '5':
        print('\nYou have successfully logged out!\n')
        return 0
    
    if answer == '0':
        print('\nBye!\n')
        return 1

    print('\nWrong input!\n')
    return
