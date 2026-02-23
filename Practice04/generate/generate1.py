def gensquares(N):
    for i in range(N + 1):
        yield i ** 2

a=int(input())
for x in gensquares(a):
    print(x,end=" ") 
