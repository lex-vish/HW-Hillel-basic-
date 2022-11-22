# Візьміть гру з попереднього ДЗ ('rock scissors paper lizard spock') і модифікуйте наступним чином:
# винесіть всі функції в окремий файл (нехай буде library.py) і імпортуцте їх звідти для роботи в основний файл
# додайте запис статистики в файл (які фігури грали і хто переміг на кожному ході), використовуйте open.

# імпорт гри "rock, Spock, paper, lizard, scissors"
from hw8library import rpsls

# введення вибору гравця серед опцій rock, Spock, paper, lizard, scissors
player_guess = input('Enter your choice.. Options: rock, Spock, paper, lizard, scissors\n' )

# виклик функції для співставлення вібору гравця та АІ, а також визначення переможця
game_rpsls = rpsls(str(player_guess))

print(game_rpsls)

# запис результатів гри в файл hw8stat.txt
with open('hw8stat.txt', 'w') as stat_file:
    for count in range(3):
        stat_file.write(f'{game_rpsls[count]} \n')




