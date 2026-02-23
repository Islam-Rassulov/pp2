def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a=int(input())
b=int(input())
for val in squares(a, b):
    print(f"Sqrt: {val}")