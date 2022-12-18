'''Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

array = [2, 3, 4, 5, 6]
if len(array)%2==0:
    for i in range(len(array)//2):
        print(array[i]*array[len(array)-1-i])
else:
    for i in range(len(array)//2+1):
        print(array[i]*array[len(array)-1-i])