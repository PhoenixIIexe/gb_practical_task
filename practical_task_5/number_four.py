data = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Ten': 'Десять'
}

with open('new_my_file.txt', 'w', encoding='utf-8') as new:
    for i in open('my_file.txt', 'r'):
        i = i.split()
        for g in data.keys():
            if i[0] == g:
                i[0] = data[g]
                new.write(' '.join(i) + '\n')