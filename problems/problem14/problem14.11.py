def f(x, a):
    return x ** 2 - a


def fdx(x):
    return 2 * x


a = 6400
xn = a / 2
iterations = 7
for i in range(iterations + 1):
    if f(xn, a) == 0:
        print(i)
        break
    xn = xn - f(xn, a) / fdx(xn)
print(xn)


############################################
# ----------Now for 1/sqrt(x) ##############
def f2(x, a):
    return (1 / x ** 2) - a


def f2dx(x):
    return -2 / x ** 3


a = 7891324
xn = 1 / (a / 2)
iterations = 1000000
for i in range(iterations + 1):
    f_of_xn = f2(xn, a)
    if f_of_xn == 0:
        print(i)
        break
    xn = xn - f_of_xn / f2dx(xn)
print(xn)
