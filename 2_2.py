# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N

N = int(input('Enter number: '))
p = 1 # начальное значение произведения всегда 1
for i in range(1, N+1):
    for i in range (1, N+1):
        p = p * i
        print(p, end=" ")