# Home work #3.
# 1) Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові. Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'". Слово та номер символу отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".
# 2) Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). Напишіть код, який визначить кількість слів, в цих даних.
# 3) Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1. Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

# Test#1
string = input("Input the word: ")
number = int(input("Input the number of letter (start from 0, but less than length of the word): "))
if (number < len(string)) and (number >= 0):
    letter = string[number]
    new_str = f"The {number} symbol in '{string}' is '{letter}'"
    print(new_str)
else:
    print("Wrong number, try again!")

# Test#2
sentence = input("Please, input sentence: ")
res = sentence.split()
print(len(res))

# Test#3
lst1 = ['1', 2.0, 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst1_copy = lst1.copy()
lst2 = []
for el in lst1_copy:
    if (type(el) == int) or (type(el) == float):
        lst2.append(el)
print(lst2)


