def factorial(n):
    k = 1
    for i in range(1, n + 1):
        k *= i
        yield i
    print(k)
 
 
n = int(input()) 
for g in factorial(n):
    print(g)