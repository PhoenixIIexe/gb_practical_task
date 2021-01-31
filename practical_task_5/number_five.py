with open('task-five.txt', 'x') as file:
    pass

with open('task_five.txt', 'w') as file:
        file.write(input())

summa = 0
with open('task_five.txt', 'r') as file:
    for i in file.read().split():
        summa += int(i)
    print(summa)