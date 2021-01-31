lines = 0
letters = list()
 
for line in open('my_file.txt', 'r'):
    lines += 1
    letters.append(len(line))
 
print("Lines:", lines)
print("Letters:", letters)