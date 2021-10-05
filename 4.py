while 1==1:
    n=0
    yue=0
    a=[]
    d=[]
    m=input('是否有账号(Y/N)!')
    if m=='N':
        print('注册账号')
        b=input('请输入账号：')
        c=input("请输入密码：")
        a.append(b)
        d.append(c)
        print(a,d)
    else:

        print('登陆账号')
        b=input('请输入账号：')
        c=input("请输入密码：")
        if b in a and c in d:
            while n!='5':
                n=input('''输入需要办理的业务:1,查询余额
                            2,存钱
                            3,取钱
                            4,修改密码
                            5,退出系统
                        ''')
                if n=='1':
                    print('您的余额为:',yue)
                elif n=='2': 
                    x=int(input('请输入存钱金额:'))
                    yue=yue+x
                    print('余额为:',yue)
                elif n=='3':
                    x=int(input('请输入取钱金额:'))
                    if x>yue:
                        print('您的余额不足！')
                    else:
                        yue=yue-x
                        print("余额为",yue)
                elif n=='4':
                    z=input('请输入您要要修改的密码:')
                    d.remove(c)
                    d.append(z)
                elif n=='5':
                    print('退出系统!')

        else:
            print('账号或密码错误!')
