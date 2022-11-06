# Home work #4. Deadline: 08/11/2022
# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні літери підряд.
# Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною. Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"

# Task#1
vowels = ["a", "e", "i", "y", "o", "u"]
diphthongs = []
for counter_1 in range(len(vowels)-1):
    for counter_2 in range(len(vowels)-1):
        diphthong = vowels[counter_1]+vowels[counter_2]
        diphthongs.append(diphthong)

sentence = "Two tea to room two, please. Air is good."
list_sntc = sentence.lower().split()
count = 0
for word in list_sntc:
    for vv in diphthongs:
        if vv in word:
            count += 1
print(count)

# Task#2
dict = { "cito": 47.999, "BB_studio": 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}
lower_limit = 35.9
upper_limit = 37.339
matches = []
for key, value in dict.items():
    if (value > lower_limit) and (value < upper_limit):
        matches.append(key)
print(f'match: {matches}')
print(dict.values())