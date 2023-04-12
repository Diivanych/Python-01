
a = int(input('Введите интересуещее Вас число: '))
list = []
for i in range(1, (a//2 + 1)):
    if((a) % i == 0):
        list.append(i)
print(list)

"""
a = int(input('Введите интересуещее Вас число: '))
list1 = []
list2 = []
for i in range(1, (a//8 + 1)):
    if((a) % i == 0):
        list1.append(i)
        list2.append(int(a/i))
list2.reverse()
list1 = list1 + list2
print(list1)
"""
'''
a = int(input('Введите интересуещее Вас число: '))
list = []
n = 1
for i in range(1, (int(a ** (1/2)) + 1)):
    if((a) % i == 0):
        list.append(a/list[0])
print(list)
'''


