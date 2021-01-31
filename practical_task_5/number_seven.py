import json
datas = dict()
data = list()
average_firm = list()
average_profit = int(0)
g = int(0)


for i in open('my_file.txt', 'r'):
    i = i.split()
    profit = int(i[2])-int(i[3])
    if profit >= 0:
        datas.update([(i[0], profit)])
        average_firm.append(i[0])
        g += 1
    else:
        datas.update([(i[0], str(-profit) + '(Убыток)')])
        
for i in average_firm:
    average_profit += int(datas[i])


datas.update([('average_profit', average_profit // g)])
data.append(datas)
print(data)
            
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file)