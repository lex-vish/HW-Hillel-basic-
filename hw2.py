# Home work 2. Deadline is 01/11/2022.
# Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік (можно використати константу або input()).
# - якщо користувачу менше 7 - вивести повідомлення "Де твої батьки?"
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# - якщо користувачу більше 65 - вивести повідомлення "Покажіть пенсійне посвідчення!"
# - якщо вік користувача з двох однакових цифр - вивести повідомлення "Як цікаво!"
# - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
# P.S. На екран має бути виведено лише одне повідомлення, якщо вік користувача з двох однакових цифр то має бути виведено тільки відповідне повідомлення! Також подумайте над варіантами, коли введені невірні або неадекватні дані.
try:
    age = int(input("What is your age? "))
    if (age > 10) and (str(age)[0] == str(age)[1]):
        print("Як цікаво!")
    elif age < 7:
        print("Де твої батьки?")
    elif age < 16:
        print("Це фільм для дорослих!")
    elif age > 65:
        print("Покажіть пенсійне посвідчення!")
    else:
        print("А білетів вже немає!")
except:
    print ("Try again! Be careful, your information is incorrect!")