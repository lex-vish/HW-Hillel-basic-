# 1. Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float. Якщо перетворити не вдається функція має повернути 0.

def turn_to_float():
    while True:
        try:
            return print(float(input('Enter the number to transform it ih the float: ')))
        except Exception as e:
            print('It\'s not a transformed to the float ')

get_float = turn_to_float()

# 2. Напишіть функцію, що приймає два аргументи. Функція повинна
# якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# у будь-якому іншому випадку повернути кортеж з цих аргументів

def act_type(arg1, arg2):
    if (type(arg1) == (int or float)) and (type(arg2) == (int or float)):
        return arg1 * arg2
    elif (type(arg1) == str) and (type(arg2) == str):
        return arg1 + arg2
    else:
        return (arg1, arg2)

get_action_1 = act_type(5, 7)
print(get_action_1, type(get_action_1))
get_action_2 = act_type("str1", "str2")
print(get_action_2, type(get_action_2))
get_action_3 = act_type("str", [1,2])
print(get_action_3, type(get_action_3))

# 3. Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
# Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік. Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...). Наприклад :

def end_years(number):
    try:
        if int(number) == 1 or (int(str(number)[-1]) == 1 and int(number) != 11):
            return "pik"
        elif (2 <= int(number) <= 4) or ((int(str(number)) > 15) and (2 <= int(str(number)[-1]) <= 4)):
            return "роки"
        else:
            return "років"
    except Exception as e:
         print("Спробуй ще! Я очікую число!")

def cashier_in_cinema(age):
    try:
        if int(str(age)[-1]) == 7:
            return print(f'Вам {age} {end_years(age)}, вам пощастить!')
        if 0 < int(age) < 7:
            return print(f'Вам {age} {end_years(age)}! Де твої батьки?')
        elif 7 <= int(age) < 16:
            return print(f'Тобі лише {age} {end_years(age)}, а це е фільм для дорослих!')
        elif 199 > int(age) > 65: # We think, that age can't be more than 1xx years
            return print(f'Вам {age} {end_years(age)}? Покажіть пенсійне посвідчення!')
        elif 16 <= int(age) <= 65:
            return print(f'Незважаючи на те, що вам {age} {end_years(age)}, білетів всеодно нема!')
        else:
            return print("Вам незрозуміло скільки років! Спробуй ще!")
    except Exception as e:
        print("Спробуй ще! Твоя інформація не коректна!")

my_ticket = cashier_in_cinema(input("Cкільки Вам років? "))

