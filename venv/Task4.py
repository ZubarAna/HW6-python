# 1 Подсчитать сумму цифр в вещественном числе.
# n = input("Введите вещественное число: ")
# sum = 0
# for i in n:
#     if i.isdigit():
#         sum += int(i)
# print(f'Cуммa цифр в вещественном числе {n} = {sum}')

n = input("Введите вещественное число: ")
new_sum = sum(map(int, str(n).replace('.', '')))
print(f'Cуммa цифр в вещественном числе {n} = {new_sum}')