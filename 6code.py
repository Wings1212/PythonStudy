def question():
    print('你吃饭了吗？')
    ans = input()
    if ans == 'y' or ans == 'yes' or ans == '是':
        print('好吧，那我走了吧。')
    else:
        print('我们一起去吃吧！')


if __name__ == '__main__':
    question()
