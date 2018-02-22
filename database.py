#-*- coding:utf-8 -*-
import sys
import sqlite3
from PyQt5.QtWidgets import QWidget,QApplication,QToolButton,QDesktopWidget,QLabel,QLineEdit,QRadioButton,QComboBox,QMessageBox,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QPainter,QPixmap
from PyQt5.QtCore import *
users={'mpy':'512200'}
Ssex=None
#数据库部分
class create_database(object):
        def __init__(self):
            self.stu=sqlite3.connect('student.db')
            self.s=self.stu.cursor()
            #self.s.execute('drop table student')
            self.create_table()
            #self.insert_data()
        def create_table(self):
            self.s.execute('create table if not exists student(sno text,sname text,ssex text,sage text,sdept text);')
            self.stu.commit()

        def insert_data(self,sno,sname,ssex,sage,sdept):
            self.s.execute('insert into student values(?,?,?,?,?)',(sno,sname,ssex,sage,sdept))
            self.stu.commit()
        def show_table(self):
            rows=[]
            for row in self.s.execute('select * from student'):
                rows.append(row)
            return rows

class login_ui(QWidget):
    #界面相关设置
    def __init__(self):
        super().__init__()
        self.center()
        self.init_ui()
        self.show()

        self.udb = update_database()
    def init_ui(self):
        self.setWindowTitle('MySQL Administrator 1.2.17')
        self.resize(560,450)
        self.setStyleSheet('font:bold 18px;background:white')



        Label1=QLabel('连接到MySQL服务实例',self)
        Label1.move(30,190)


        HostLabel=QLabel("   主机名:",self)
        HostLabel.move(95,230)
        HostText=QLineEdit('localhost',self)
        HostText.move(200,225)
        HostText.resize(130,25)
        port=QLabel(' 端口号:',self)
        port.move(350,230)
        portText=QLineEdit('3306',self)
        portText.move(430,225)
        portText.resize(70,25)


        UserLabel=QLabel('   用户名:',self)
        UserLabel.move(95,270)
        self.UserText=QLineEdit(self)
        self.UserText.move(200,270)


        PassLabel=QLabel('     密码:',self)
        PassLabel.move(95,310)
        self.PassText=QLineEdit(self)
        self.PassText.setEchoMode(QLineEdit.Password)
        self.PassText.move(200,310)


        self.LoginButton=QToolButton(self)
        self.LoginButton.move(180,380)
        self.LoginButton.setText('确定')
        #grid.addWidget(LoginButton,5,2)

        self.CancelButton=QToolButton(self)
        self.CancelButton.move(300,380)
        self.CancelButton.setText('取消')



        self.LoginButton.clicked.connect(self.login_firm)
        self.CancelButton.clicked.connect(self.close)
    def paintEvent(self, QPaintEvent):
        p=QPainter(self)
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)
        p.drawPixmap(0,0,560,150,QPixmap("1.png"))
        p.end()

    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    #处理函数
    def login_firm(self):
        if self.UserText.text() in users.keys():
            if self.PassText.text()==users[self.UserText.text()]:
                self.LoginButton.clicked.connect(self.close)
                self.LoginButton.clicked.connect(self.udb.show)
        else:
                self.login_mes = QMessageBox.warning(self, '错误提示', '输入了错误的账号/密码')








class update_database(QWidget):
    #界面设计
    def __init__(self):
        super().__init__()
        self.center()
        self.init_ui()
        self.cdb = create_database()

        #self.show()
    def init_ui(self):
        self.resize(560,450)
        self.setWindowTitle('MySQL Administrator 1.2.17')
        self.setStyleSheet('font:bold 18px')
        self.combox=QComboBox(self)
        self.sd = show_data()

        Label1 = QLabel("请在下面输入要录入的内容:", self)
        Label1.move(30,30)

        SnoLabel=QLabel('学号:',self)
        SnoLabel.move(150,70)
        self.SnoText=QLineEdit(self)
        self.SnoText.setPlaceholderText('学号为11位数字')
        self.SnoText.move(210,70)

        SnameLabel=QLabel('姓名:',self)
        SnameLabel.move(150,120)
        self.SnameText=QLineEdit(self)
        self.SnameText.setFixedWidth(100)
        self.SnameText.move(210,120)

        xbLabel=QLabel('性别:',self)
        xbLabel.move(150,170)
        self.xb_man=QRadioButton('男',self)
        self.xb_man.move(210,170)
        self.xb_feman=QRadioButton('女',self)
        self.xb_feman.move(210,190)

        AgeLabel=QLabel('年龄:',self)
        AgeLabel.move(150,220)
        self.AgeText=QLineEdit(self)
        self.AgeText.setFixedWidth(50)
        self.AgeText.move(210,220)

        SdepartLabel=QLabel('院系:',self)
        SdepartLabel.move(150,270)
        self.combox.move(210,270)
        self.combox.insertItem(1,self.tr('MATH'))
        self.combox.insertItem(2,self.tr('SCIENCE'))

        self.EnterButton=QToolButton(self)
        self.EnterButton.setText('确定')
        self.EnterButton.resize(80,50)
        self.EnterButton.move(310,350)

        self.CancelButton=QToolButton(self)
        self.CancelButton.setText('取消')
        self.CancelButton.resize(80,50)
        self.CancelButton.move(420,350)

        self.FindButton=QToolButton(self)
        self.FindButton.setText('查询')
        self.FindButton.resize(80,50)
        self.FindButton.move(200,350)


        self.EnterButton.clicked.connect(self.get_sex)
        self.EnterButton.clicked.connect(self.Insert)
        self.EnterButton.clicked.connect(self.refresh)
        self.CancelButton.clicked.connect(self.close)
        self.FindButton.clicked.connect(self.sd.show)
        self.FindButton.clicked.connect(self.sd.insert_table)
    def refresh(self):
        self.SnoText.clear()
        self.SnameText.clear()
        self.AgeText.clear()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    #处理函数
    def Insert(self):
        sno=self.SnoText.text()
        sname=self.SnameText.text()
        ssex=Ssex
        sage=self.AgeText.text()
        sdept=self.combox.currentText()
        print(sno,sname,ssex,sage,sdept)
        self.cdb.insert_data(sno,sname,ssex,sage,sdept)
    def get_sex(self):
        global Ssex
        if self.xb_man.isChecked():
            Ssex='男'
        else:
            Ssex='女'




class show_data(QTableWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.cd=create_database()
        #self.show()
    def init_ui(self):
        #self.current_row=0
        self.resize(560,450)
        self.setWindowTitle('MySQL Administrator 1.2.17')
        self.setColumnCount(5)
        self.setRowCount(10)
        column_width=[186,106,66,66,106]
        for column in range(5):
            self.setColumnWidth(column,column_width[column])
        headers=['学号','姓名','性别','年龄','所在系']
        self.setHorizontalHeaderLabels(headers)
    def insert_table(self):
        rows=self.cd.show_table()
        for row in rows:
            #print(rows.index(row))
            for x in range(5):
                #print(row[x])
                self.setItem(rows.index(row),x,QTableWidgetItem(self.tr(row[x])))
                    #self.setItem(y,1,QTableWidgetItem=row[1])
if __name__=='__main__':
    app=QApplication(sys.argv)
    lg=login_ui()
    #udb=update_database()
    #db=create_database()
    #sd=show_data()
    #db.show_table()
    #lu.LoginButton.clicked.connect(lu.close)
    #lu.LoginButton.clicked.connect(db.show)
    app.exit(app.exec_())
