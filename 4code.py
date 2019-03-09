def hello(name):
    print('{0}，你好呀。。。'.format(name))


def bye():
    print('再见了。。。')


if __name__ == '__main__':
    name = input('请输入你要打招呼的人的名字：')
    hello(name)
    print('*' * 50)
    bye()
