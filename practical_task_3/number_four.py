def my_funs(x, y):
    z = x
    for i in range(y - 1):
        x *= z
    print(x)


my_funs(float(input()), int(input()))