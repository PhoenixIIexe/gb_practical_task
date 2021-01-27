lists = [4, 5, 124, 4, 13, 1, 0]
new_lists = list()

for i in range(len(lists)-1):
    if lists[i] < lists[i+1]:
        new_lists.append(lists[i+1])

print(new_lists)
