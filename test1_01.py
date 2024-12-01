money_left = 1000
if money_left > 10000:
    print("立刻买")
elif 1000 < money_left < 10000:
    print("等等买")
else:
    print("不买了")


def foo1(x):
    if x % 2 == 0:
        return x
    else:
        return x * 2


def foo2(x):
    return x if x % 2 == 0 else x * 2


s = foo1(4)
s1 = foo2(4)
print(s)
print(s1)
