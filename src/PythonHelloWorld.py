from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 定义函数
def fib(limit):
    "这是文档"
    before, after = 0, 1
    while after < limit:
        print(after, end=',')
        before, after = after, before + after


def fib2(limit):
    result = []
    before, after = 0, 1
    while after < limit:
        result.append(before)
        before, after = after, before + after
    return result


def ask_ok(prompt, retries=4, complaint='Yes or No, please!'):
    """有默认参数的方法.

    这是注释.
    """
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):  # in 用于判断列表中是否包含某一值
            return True
        if ok in ('nope', 'n', 'no', 'nop'):
            return False
        retries -= 1
        if retries < 0:
            raise IOError('refuse nik user')
        print(complaint)


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


def concat(*args, sep=', '):
    return sep.join(args)


if __name__ == '__main__':
    # 字符串切割
    # word = '你猜我在干什么'
    # print(word[10:])
    # print(word[0])
    # print(len(word))

    # print('f你好j'.encode('utf-8'))
    # 数组
    # aList = ['a', "f", 9, 0]
    # aList[0:1] = []
    # aList[1:1] = ['fds','saf']
    # print(len(aList))
    # aList=[]
    # print(aList)

    # 嵌套数组
    # q = [1,2,3]
    # p = ['a','b',q,'d']
    # q.append(32)
    # print(p)

    # 斐波那契数列
    # a, b = 0, 1
    # while b < 100:
    #     print(b, end=',')
    #     a, b = b, a + b

    # print('a','b','c','d')

    # 流程控制
    # if语句
    # x = int(input('please input an integer: '))
    # if x < 0:
    #     x = 0
    #     print('Negative changed to zero')
    # elif x == 0:
    #     print('Zero')
    # elif x == 1:
    #     print('Single')
    # else:
    #     print('More')

    # for循环
    # a = ['1jkfd', '3feyhhnvds', '2fdsafdsa']
    # for x in a:
    #     print(x, len(x))
    # 循环时改变序列的值
    # for x in a[:]:
    #     if len(x) > 9 :
    #         a.insert(0, x)
    # print(a)
    #
    # for i in range(10):
    #     print(i, end=', ')

    # for i in range(len(a)):
    #     print(i, a[i])

    # print(range(0, 10))
    # print(list(range(0, 10)))

    # fib(2000)

    # 函数可以赋值
    # f = fib
    # fib(10)
    # print(fib)
    # print(f)
    # print(f(10))
    #
    # print(fib2(200))

    # ask_ok('Do you want to quit?')

    # print(f(1))
    # print(f(2))
    # print(f(3))

    # cheeseshop("Limburger", "It's very runny, sir.",
    #            "It's really very, VERY runny, sir.",
    #            shopkeeper="Michael Palin",
    #            client="John Cleese",
    #            sketch="Cheese Shop Sketch")
    #
    # print(concat('a','b','c'))
    #
    # args = [3, 6]
    # print(list(range(*args)))

    # square = [(x, x**2) for x in range(1, 9)]
    # print(square)

    # t = 12345, 54321, 'jklklj'
    # print(t)
    #
    # x, y, z = t
    # print(x)
    # print(y)
    # print(z)

    # knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    # for k, v in knights.items():
    #     print(k,v)

    print(dir())



    pass
