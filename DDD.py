def 斐波那契数列(n):
    a, b = 0, 1
    数列 = []
    while len(数列) < n:
        数列.append(a)
        a, b = b, a + b
    return 数列

# 获取用户想要的数列长度
长度 = int(input("你想要多长的斐波那契数列？请输入数字："))
print(斐波那契数列(长度))
