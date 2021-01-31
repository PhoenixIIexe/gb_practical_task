my_file = open('my_file.txt', 'x')

my_file = open('my_file.txt', 'w')

data = ' '
while data != '':
    data = input()
    my_file.write(data + '\n')

my_file.close()