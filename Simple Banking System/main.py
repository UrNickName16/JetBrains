from cards import create_card, log_in


def main():
    while True:
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')

        answer = input()
        if answer == '0':
            print('\nBye!')
            return

        elif answer == '1':
            create_card()

        elif answer == '2':
            if log_in() == 1:
                return

        else:
            print('Wrong input!')
            

if __name__ == '__main__':
    main()
