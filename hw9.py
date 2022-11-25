# Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах і задекоруйте ним основну функцію гри з попередньої дз. Після закінчення гри декоратор має сповістити, скільки тривала гра.

import time
def decor_timer(function):
    def wrapped(*args, **kwargs):
        start_time = time.time()
        res = function(*args, **kwargs)
        print(f'The game lasted {time.time()-start_time} seconds')
        return res

    return wrapped

# to import random function for using random.randrange
import random

# function to convert number to name
def number_to_name(number):
    '''
    Args:
        number: приймає число від 0 до 4
    Returns: повертає відповідне ім'я 0 - rock; 1 - Spock; 2 - paper; 3 - lizard; 4 - scissors
    Порядок номерів подібран таким чином, щоб залишок від ділення на 5 різниці між числами, що відповідають канкуруючим сутностям,для переможця не перевищував 2.
    Детальнище дивись docstring до функції def rpsls(guess)
    '''

    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Error"


# function to convert name to number
def name_to_number(name):
    '''
    Args:
        name: приймає ім'я (одне з rock; Spock; paper; lizard; scissors
    Returns: повертає число відповідно ім'ю число від 0 до 4
    '''
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print
        name + "is not a character in RPSLS"


# function which selects the winner
@decor_timer
def rpsls(guess):
    '''
    Args:
        guess: приймає вибір гравця (одни з п'яти:
    Returns: результат порівняння вибору гравця та АІ обраного
    Ключова логіка розрахунку. Програма переводить вектор різниць між числами, що відповідають вибору граців (-4,-3, -2, -1, 0, 1, 2, 3, 4) у
    вектор (1, 2, 3, 4, 0, 1, 2, 3, 4). Розташування сутносей зроблено таким чином, що значення (1;2) відповідають переможцю, (3;4) програвшому.
    '''
    try:
        # convert name to player_number using name_to_number
        player_number = name_to_number(guess)

        # compute random guess for comp_number using random.randrange()
        comp_number = random.randrange(0, 5)

        # compute difference of player_number and comp_number modulo five.
        # Створюємо єдиний вектор результатів для їх порівняння в діапозоні [0,4]
        winner = (comp_number - player_number) % 5

        # use if/else to determine winner
        # значення 1,2 відповідають переможцю
        if winner < 3:
            player_win = False
        else:
            player_win = True

        # convert comp_number to name using number_to_name
        comp_name = number_to_name(comp_number)

        # print results
        print("Player chooses " + guess)
        print("AI chooses " + comp_name)
        if player_win:
            print("Player wins!\n")
        elif comp_number == player_number:
            print("Player and AI tie!\n")
        else:
            print("AI wins!\n")

    except Exception as e:
        print('It\'s not a right name of entity. Please, write rock, Spock, paper, lizard or scissors!')

player_guess = input('Enter your choice.. Options: rock, Spock, paper, lizard, scissors\n' )

rpsls(str(player_guess))
