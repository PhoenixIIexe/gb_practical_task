k = int(0)
g = int(0)
income = int(0)
with open('my_file.txt', 'r') as my_file:
    for i in my_file:
        income += int(i.split()[1])
        if int(i.split()[1]) < 20000:
            k += 1
        g += 1
        

print(k, income/g)    
    
