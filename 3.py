# Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3

a = int(input("Введите число: "))
n = list(map(int,input().split()))
print(n)

for i in n:
    if i%3 == 0:
        print(i,end= '')