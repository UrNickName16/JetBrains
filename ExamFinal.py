from random import randint, choice


def simpleTaskGenerator(): 
    operators = ['+', '-', '*']
    a = randint(2, 9)
    b = randint(2, 9)
    task = str(a) + ' ' + choice(operators) + ' ' + str(b)
    return [task, eval(task)]


def hardTaskGenerator():
    task = randint(11, 29)
    return [task, task**2]


def checkAnswer(bounds=None):
    if not bounds:
        while True:
            try:
                answer = int(input())
            except Exception:
                print('Incorrect format.')
            else:
                return answer
    
    else:
        while True:
            answer = input().lower()
            if answer not in bounds:
                print('Incorrect fromat.')
            else:
                break
        return answer


def exam(difficulty):
    n = 0

    if difficulty == 1:
        for i in range(5):
            task, result = simpleTaskGenerator()
            print(task)
            answer = checkAnswer()
            if answer == result:
                n += 1
                print('Right!')
                continue
            print('Wrong!')
    
    else:
        for i in range(5):
            task, result = hardTaskGenerator()
            print(task)
            answer = checkAnswer()
            if answer == result:
                n += 1
                print('Right!')
                continue
            print('Wrong!')

    return n


def main():
    while True:
        print('Which level do you wand? Enter a number: ')
        print('1 - simple operations with numbers 2-9')
        print('2 - integral squares of 11-29')
        difficulty = input()
        try:
            difficulty = int(difficulty)
            if difficulty not in [1, 2]:
                raise ValueError
        except Exception:
            print('Incorrect format.')
            continue
        break

        print('Incorrect format.')

    n = exam(difficulty)
    print(f'Your mark is {n}/5. Would you like to save the result? Enter yes or no.')
    if checkAnswer(bounds=['no', 'yes']) == 'yes':
        print('What is your name?')
        file = open('result.txt', 'a')
        file.write(f'{input()}: {n}/5 in level {difficulty} ({("simple operations with numbers 2-9" * (difficulty == 1)) + ("integral squares of 11-29" * (difficulty == 2))})\n')
        file.close()
        print('The results are saved in "result.txt"')


if __name__ == '__main__':
    main()