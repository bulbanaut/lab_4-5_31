#! /usr/bin/python3
numbers = []
k = int(input('Введите значение k: '))
print('Введите произвольны целые числа\nИли введите "done" чтобы закончить ввод чисел')
while k < k +1:
    n = input()
    if n == 'done':
        break
    numbers.append(int(n))
print(numbers)
amount_even = 0
for i in numbers:
    if i % k == 0:
        break
    else:
        amount_even = amount_even +1
print('Количество чётных чисел до числа кратного k: ', amount_even)
positive = []
positive_odd = []
for i in numbers:
    if i > 0 and i %2 != 0:
        positive.append(i)
        positive_odd.append(i)
    elif i > 0:
        positive.append(i)
print('Сумма положительных k чисел:',sum(positive[:k]),\
'\nСреднее арифметическое первых k положительных нечётных чисел:', (sum(positive_odd[:k]) / len(positive_odd)))