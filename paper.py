import random

ROCK = 'камень'
SCISSORS = 'ножницы'
PAPER = 'бумага'

def get_user_choice():
    while True:
        try:
            user_choice = input('Выбери: камень, ножницы, бумага: ').lower()
            if user_choice in (ROCK, SCISSORS, PAPER):
                return user_choice
            else:
                raise ValueError('Некорректный выбор. Попробуй снова.')
        except ValueError as e:
            print(e)

def compare(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Ничья'
    elif user_choice == ROCK:
        if computer_choice == SCISSORS:
            return name1 + ' победитель'
        else:
            return 'Компьютер победитель'
    elif user_choice == SCISSORS:
        if computer_choice == PAPER:
            return name1 + ' победитель'
        else:
            return 'Компьютер победитель'
    elif user_choice == PAPER:
        if computer_choice == ROCK:
            return name1 + ' победитель'
        else:
            return 'Компьютер победитель'
    else:
        return 'Я тебя не понимаю'

name1 = input('Привет! Это игра "Камень, Ножницы, Бумага с компьютером!". Введи свое имя, чтобы приступить к игре: ')

ans = input("%s, готов уничтожить своего противника?" % name1).lower()
if ans == 'да':
    print('Тогда поехали!')
elif ans == 'нет':
    print('Игра остановлена, до скорой встречи!')
    exit()
else:
    print('Введи "да" или "нет", я тебя не понимаю')
    exit()

round = 1

while True:
    print('РАУНД:', round)
    round += 1

    try:
        user_choice = get_user_choice()
        computer_choice = random.choice([ROCK, PAPER, SCISSORS])

        print('Компьютер выбрал:', computer_choice)

        print(compare(user_choice, computer_choice))
    except KeyboardInterrupt:
        print('Игра прервана пользователем. До скорой встречи!')
        exit()