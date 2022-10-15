# 14.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите число ')
if ',' in num:
    num = num.replace(',',"")
    sum = 0
    for a in num:
        sum = sum + int(a)
    print(sum)
elif '.' in num:
    num = num.replace('.',"")
    sum = 0
    for a in num:
        sum = sum + int(a)
    print(sum)
else:
    sum = 0
    for a in num:
        sum = sum + int(a)
    print(sum)

# 15.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


num = int(input('Введите число '))
print('[', end='')
mult = 1
for i in range(1, num):
    mult = mult * i
    print(mult, end=', ')
print(mult*num, end=']')


# 16.Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число '))
print(f'n = {n}', end=' ')
print('{', end=' ')
sum = 0
for i in range(1, n+1):
    result = round((1+(1/i))**i, 2)
    sum = round(sum + result, 2)
    print(i, ':', result, end=', ')
print()
print(f'Сумма = {sum}')

# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

a = [1, 2, 3, 2, 0]
b = [5, 1, 2, 7, 3, 2]
c = []

for i in range(0, len(a)):
    for j in range(0, len(b)):
        if b[j] == a[i]:
            c.append(b[j])

print(c)
