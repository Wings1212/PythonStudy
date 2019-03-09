for i in range(3):
    user = input('请输入你的用户名：')
    password = input('请输入你的密码：')
    if user == 'wings' and password == '12345678901':
        print('欢迎%s' % user)
        break
    else:
        if i < 2:
            print('不好意思，你的用户名或者密码有误！请再次输入！')
            if len(password) < 11:
                print('【提示】你输入的密码长度少于正确密码。')
            elif len(password) > 11:
                print('【提示】你输入的密码长度大于正确密码。')
        else:
            print('你今天的输入错误密码次数已达上限！！！')
