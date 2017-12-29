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


def ask_ok(prompt, retries = 4, complaint = 'Yes or No, please!'):
    '有默认参数的方法'
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):    # in 用于判断列表中是否包含某一值
            return True
        if ok in ('nope','n','no', 'nop'):
            return False
        retries -= 1
        if retries < 0:
            raise IOError('refuse nik user')
        print(complaint)


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

    ask_ok('Do you want to quit?')