# ==============================================================================
# Задача 2: Найдите сумму цифр трехзначного числа. 
# ------------------------------------------------------------------------------
'''
a = int(input('Введите любое натуральное число: '))
sum = 0
while a > 0 :
    sum = sum + a%10
    a = a // 10
print(f'Сумма цифр в числе равна:  {sum}')
'''
# ==============================================================================
# //////////////////////////////////////////////////////////////////////////////
# ==============================================================================
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# ------------------------------------------------------------------------------
'''
a = int(input('Введите количество журавликов, представленных комиссии: '))
if a % 6 > 0 :
    print('Делать журавликов ребятам помогала девочка из Хиросмы')
else:
    print(f'Серёжа сделал {int(a / 6)} журавликов')
    print(f'Петя сделал   {int(a / 6)} журавликов')
    print(f'Катя сделала  {int((a / 6) * 4)} журавликов')
'''
# ==============================================================================
# //////////////////////////////////////////////////////////////////////////////
# ==============================================================================
# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# ------------------------------------------------------------------------------
# Чсловое решение
'''
a = int(input(f'\n Введте номер своей кредитной карты: '))
# Вычисляем разрядность введённого числа
n = a
d = 0
while n > 0 :
    n = n // 10
    d += 1
n = a
sum1 = 0
sum2 = 0
r = range(d // 2)
# Сумма для правой части числа
for i in r:
    sum1 = sum1 + n % 10
    n = n // 10
# Сумма для левой части числа
p = 0 # Признак чётности
if d % 2 > 0 :
    p = 1
n = a // (10 ** ((d // 2) + p))
for i in r:
    sum2 = sum2 + n % 10
    n = n // 10
print(f'\n Сумма левой части номера Вашей кредитки: {sum2}')
print(f'\n Сумма правой части номера Вашей кредитки: {sum1}')
if sum1 == sum2 :
    print('\n Редкая удача! У Вас счастливая карта! \n ')
else:
    print('\n Сообщите ещё и CVV код. Тогда точно повезёт :) \n')
'''
# //////////////////////////////////////////////////////////////////////////////
# Решене через обработку строки
'''
a = input('\n Введте номер своей кредитной карты: ')
d = len(a)
sum1 = 0
sum2 = 0
r = range(d // 2)
for i in r:
    sum1 = sum1 + int(a[i])
    sum2 = sum2 + int(a[- (d // 2) + i])
print(f'\n Сумма левой части номера Вашей кредитки: {sum1}')
print(f'\n Сумма правой части номера Вашей кредитки: {sum2}')
if sum1 == sum2 :
    print('\n Редкая удача! У Вас счастливая карта! \n ')
else:
    print('\n Сообщите ещё и CVV код. Тогда точно повезёт :) \n ')
'''
# ==============================================================================
# //////////////////////////////////////////////////////////////////////////////
# ==============================================================================
# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# ------------------------------------------------------------------------------
'''
print()
m = int(input('Введите высоту шоколадки: '))
n = int(input('Введите ширину шоколадки: '))
k = int(input('Сколько  Вам долек нужно? '))
if k % m == 0 or k % n == 0:
    print('\nДа запросто! Берите. \n ')
else:
    print('\nНе парься. Бери всю! \n ')
'''
# ==============================================================================