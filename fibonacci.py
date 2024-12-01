# 斐波那契数列的前100项‌如下：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610


# seq_test = [1, 1]
# for i in range(100 - 2):
#     seq_test.append(seq_test[i] + seq_test[i + 1])

# print(seq_test)


def fib_1(x):
    seq_1 = [1, 1]
    if x == 1:
        return [1]
    elif x == 2:
        return seq_1
    else:
        for _ in range(x - 2):
            seq_1.append(seq_1[_] + seq_1[_ + 1])
        return seq_1


# n = fib_1(5)
# print(n)


def cal_1(n):
    ret = 0
    for _ in range(n + 1):
        ret += _
    print(ret)
    return ret


# cal_1(100)
# cal_1(1000)





def test12_1(name, age, gender):
    print(name)
    print(age)
    print(gender)



# test12_1(name=12, age=22, )

dict_1 = {"gender": "男", "name": "z3", "age": 11}


test12_1(**dict_1)






