'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''


arr = [1.1, 1.2, 3.1, 5, 10.01]
min= 0.1
max= 0.1
for i in range(len(arr)):
    if arr[i]%1 !=0:
        if max<arr[i]%1:
            max=arr[i]%1
        elif min>arr[i]%1:
            min = arr[i]%1
print(round(max-min,5))
