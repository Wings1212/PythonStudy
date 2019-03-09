def question():
    while True:
        print('你吃饭了吗？')
        ans = input()
        if ans == 'y' or ans == 'yes' or ans == '是':
           print('我就是要等你！')
        else:
            print('我们一起去吃吧！')
            break

if __name__ == '__main__':
    question()
