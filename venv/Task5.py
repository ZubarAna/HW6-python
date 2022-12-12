'''5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
*Пример:*
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
[Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8)
https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
'''
# #{F_{1}=1, F_{2}=-1, Fn = F(n+2)−F(n+1)} - числа негафибоначчи
# #{F_{0}=1, F_{2}=1,F_{n}=F_{n-1}+F_{n-2}} - числа фибоначчи
# n = int(input("Задайте число: "))
# def negafibonachi(n):
#     fib1 = 1
#     fib2 = -1
#     for i in range(n):
#         yield -fib2
#         fib_sum = fib2 - fib1
#         fib2 = fib1
#         fib1 = fib_sum
# def fibonacci(n):
#     fib1 = 0
#     fib2 = 1
#     for i in range(n + 1):
#         yield fib1
#         fib_sum = fib1 + fib2
#         fib1 = fib2
#         fib2 = fib_sum
#
# data1 = list(fibonacci(n))
# data2 = list(negafibonachi(n))
# data2.reverse()
# result = data2 + data1
# print(result)


# улучшенный код


n = int(input("Задайте число: "))
fib = lambda n, x=0, y=1: x if not n else fib(n-1, y, x+y)
fib1 = [fib(i) for i in range(n+1)]
negafib = lambda n, x=0, y=1: x if not n else fib(n-1, y, x+y) * (-1) ** (n + 1)
negafib1 = [negafib(i) for i in range(1, n+1)[::-1]]
print(negafib1+fib1)
