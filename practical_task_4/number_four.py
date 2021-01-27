lists = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
 
new_lists = [i for i in lists if lists.count(i) < 2]
 
print(new_lists)