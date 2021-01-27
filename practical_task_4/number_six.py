from itertools import count, cycle

if input("Выберите программу a или б: ") == 'a':
    start = int(input("Напишите начальное значение: "))
    stop = int(input("Напишите конечное значение: "))

    for i in count(start):
        if stop < i:
            break
        print(i)
else:
    start = input("Напишите элемент повторение: ")
    stop = int(input("Напишите количество повторений: "))
    k = int(1)

    for i in cycle(start):
        if stop < k:
            break
        print(i)
        k += 1