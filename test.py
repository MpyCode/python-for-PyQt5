from tkinter import *
#import pymsql

root = Tk()
root.title("蓝翔校园一卡通管理系统")
Label(root, text='账号:').grid(row=0, column=0)
Label(root, text='密码;').grid(row=1, column=0)
v1 = StringVar()
v2 = StringVar()
e1 = Entry(root, textvariable=v1)
e2 = Entry(root, textvariable=v2, show='*')
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


def show():
    s1 = e1.get()
    s2 = e2.get()
    conn = pymssql.connect('DESKTOP-QLL2VD2', 'sa', '123456789', 'campuscard')
    c1 = conn.cursor()
    result = c1.execute("select password1 from people,card1 where people.cardnum=card1.cardnum and peoplenum=%s" % (s1))
    result1 = c1.fetchone()

    if result1[0] == s2:
        root1 = Tk()
        root1.title('查询')
        Button(root1, text='卡余额查询', width=10, command=show3).grid(row=0, column=0, sticky=W, padx=10, pady=5)
        Button(root1, text='个人信息查询', width=10, command=show4).grid(row=0, column=1, sticky=E, padx=10, pady=5)
        Button(root1, text='更新密码', width=10, command=show5).grid(row=1, column=0, columnspan=2, padx=10, pady=5)
    else:
        print('登录失败')
    conn.close()


def show1():
    s1 = e1.get()
    s2 = e2.get()
    conn = pymssql.connect('DESKTOP-QLL2VD2', 'sa', '123456789', 'campuscard')
    c1 = conn.cursor()
    result = c1.execute("select pass from peoplead2 where pno=%s" % (s1))
    result1 = c1.fetchone()
    if result1[0].rstrip() == s2:
        print("登录成功")
        root4 = Tk()
        root4.title("管理界面")
    else:
        print("登录失败")


def show3():
    s3 = e1.get()
    conn1 = pymssql.connect('DESKTOP-QLL2VD2', 'sa', '123456789', 'campuscard')
    c2 = conn1.cursor()
    result3 = c2.execute("select balance from card1,people where people.cardnum=card1.cardnum and peoplenum=%s" % (s3))
    result3 = c2.fetchone()
    print(result3[0])


def show4():
    s3 = e1.get()
    conn1 = pymssql.connect('DESKTOP-QLL2VD2', 'sa', '123456789', 'campuscard')
    c1 = conn1.cursor()
    result = c1.execute("select * from people,people1 where people.id=people1.id and peoplenum=%s" % (s3))
    print(c1.fetchall())


def show5():
    s3 = e1.get()
    root3 = Tk()
    root3.title('更新')
    Label(root3, text='更新后的密码').grid(row=0, column=0)
    Label(root3, text='确认密码').grid(row=1, column=0)
    v1 = StringVar()
    v2 = StringVar()
    e3 = Entry(root3, textvariable=v1)
    e4 = Entry(root3, textvariable=v2)
    e3.grid(row=0, column=1)
    e4.grid(row=1, column=1)
    s1 = e3.get()
    s2 = e4.get()
    Button(root3, text='确认', width=10, command=show6(s1, s2)).grid(row=3, column=0)


def show6(s4, s5):
    if s4 == s5:
        print("chenggong")
    else:
        print("shibai")


Button(root, text='学生登录', width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text='管理员登录', width=10, command=show1).grid(row=3, column=1, sticky=E, padx=10, pady=5)

mainloop()
