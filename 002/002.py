def Fibi(n):
    a, b = 1, 1
    while a <= n:
        a, b = b, a + b
        if a % 2 == 0:
            yield a

print sum([i for i in Fibi(4000000)])