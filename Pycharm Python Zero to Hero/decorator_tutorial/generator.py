def gen_fibon(n):
    a = 1
    b = 1
    for x in range(n):
        yield a
        a,b = b, a+b


for number in gen_fibon(10):
    print(number)

g = gen_fibon(5)
print(next(g))
print(next(g))
print(next(g))
s = 'hello'
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))