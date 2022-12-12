'''1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
 стоящих на нечётной позиции.
*Пример:*
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

# def SumOfIndex(numbers):
#     SumOfElements = 0
#     for elements in range(len(numbers)):
#         if elements % 2 != 0:
#             SumOfElements += numbers[elements]
#     print(f'Сумма элементов на нечетной позиции равна {SumOfElements}')
# numbers = list(map(int, input("Введите числа через пробел: ").split()))
# SumOfIndex(numbers)
numbers = list(map(int, input("Введите числа через пробел: ").split()))
odd_numbers_position = [numbers[elements] for elements in range(len(numbers)) if elements % 2 != 0]
print(f'Сумма элементов на нечетной позиции равна {sum(odd_numbers_position)}')

