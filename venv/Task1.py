'''3 Задать список из n чисел последовательности (1+ 1/n)**n и вывести на экран их сумму.'''
'''
n = int(input('Введите число N: '))
result = []
sum1 = 0
for i in range(1, n + 1):
    x = (1 + 1/ i) ** i
    sum1 += x
    result.append(x)
print(result)
print()
print(f'Сумма {n} чисел последовательности равна {sum}')
'''
n = int(input('Введите число N: '))
result = [(1 + 1 / i) ** i for i in range(1, n + 1)]
print(result)
print(f'Сумма {n} чисел последовательности равна {sum(result, 0)}')
