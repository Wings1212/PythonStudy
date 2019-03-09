print('这是一个趣味问答小测验')
while True:
    name = input('请问你的名字是：')
    if name == 'wings':
        print('嗯嗯，我知道了，你的名字是%s' % name)
        color = input('请问你喜欢什么颜色：')
        if color != 'yello' and color != '黄色':
            print('%s 喜欢 %s' % (name, color))
            print('欢迎下次再来玩耍。')
            break
        else:
            print('你喜欢的颜色是{col}。真独特！重口味大叔。'.format(col = color))
            break
    else:
        print('%s 谢谢参与！！！' % name)
        break
