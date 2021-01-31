data = dict()


for line in open('my_file.txt', 'r', encoding='utf-8'):
    line = line.split()
    i = int(line[1][:len(line[1])-3] if line[1][:len(line[1])-3] != '' else 0) + int(line[2][:len(line[2])-4] if line[2][:len(line[2])-4] != '' else 0) + int(line[3][:len(line[3])-5] if line[3][:len(line[3])-5] != '' else 0)
    data.update([(line[0][:len(line[0])-1], i)])

print(data)