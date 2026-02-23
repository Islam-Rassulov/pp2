def countdown(n):
    while n >= 0:
        yield n
        n -= 1

a=int(input())
for num in countdown(a):
    print(num) # 5, 4, 3, 2, 1, 0