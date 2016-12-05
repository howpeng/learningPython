# -*- coding: utf-8 -*-


# 问题: 怎么设置一次只能开一个程序,不能同时运行多个程序,否则会乱了数据


from PyQt5.QtWidgets import *
import initialData
import sqlite3
import time
import hashlib
import shelve

class Form(QDialog):
    #最先显示的登录界面
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.initUI()


    def initUI(self):
        self.userName = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        buttonBox = QHBoxLayout()
        loginButton = QPushButton('登录')
        cancelButton = QPushButton('取消')
        mainlayout = QVBoxLayout()
        layout = QGridLayout()
        layout.addWidget(QLabel('用户名: '), 0, 0)
        layout.addWidget(self.userName, 0, 1)
        layout.addWidget(QLabel('密码: '), 1, 0)
        layout.addWidget(self.password, 1, 1)

        buttonBox.addWidget(loginButton)
        buttonBox.addWidget(cancelButton)
        mainlayout.addLayout(layout)
        mainlayout.addLayout(buttonBox)

        loginButton.clicked.connect(self.login)
        cancelButton.clicked.connect(self.reject)
        self.setLayout(mainlayout)
        self.setWindowTitle('欢迎使用60YFK仓库管理系统')
        self.setGeometry(400, 400, 260, 180)

    # gui start
    def registerWindow(self):
        self.registerName = QLineEdit()
        self.registerPassword1 = QLineEdit()
        self.registerPassword1.setEchoMode(QLineEdit.Password)
        self.registerPassword2 = QLineEdit()
        self.registerPassword2.setEchoMode(QLineEdit.Password)
        registerButton = QPushButton('注册')
        cancelButton = QPushButton('取消')
        layout = QFormLayout()
        layout.addRow(QLabel('用户名: '), self.registerName)
        layout.addRow(QLabel('输入密码: '), self.registerPassword1)
        layout.addRow(QLabel('重复密码: '), self.registerPassword2)
        layout.addRow(registerButton, cancelButton)
        form = QDialog()
        form.setLayout(layout)
        registerButton.clicked.connect(self.register)
        cancelButton.clicked.connect(form.reject)
        form.setWindowTitle('新用户注册')
        if form.exec_():
            form.show()

    def featureWindow(self):

        inButton = QPushButton('入库')
        outButton = QPushButton('出库')
        seekButton = QPushButton('查询记录')
        logButton = QPushButton('导出日志')



        inButton.clicked.connect(self.inDataWindow)
        outButton.clicked.connect(self.outDataWindow)
        seekButton.clicked.connect(self.seekDataWindow)

        layout = QVBoxLayout()
        layout.addWidget(inButton)
        layout.addWidget(outButton)
        layout.addWidget(seekButton)
        layout.addWidget(logButton)

        form = QDialog()
        form.setLayout(layout)
        form.setGeometry(400, 400, 200, 400)
        form.setWindowTitle('60YFK仓库管理系统')

        if form.exec_():
            return

    def inDataWindow(self):
        date = time.gmtime()
        inDate = "{}/{}/{}".format(date.tm_year, date.tm_mon, date.tm_mday)
        self.inDate = QLineEdit(inDate)
        self.inCompany = QComboBox()
        self.inKinds = QComboBox()
        self.inName = QComboBox()
        self.inSize = QLineEdit()
        self.inNumber = QLineEdit()
        self.inMemo = QLineEdit()
        self.inShow = QListWidget()
        date = QLabel('日期: ')
        date.setBuddy(self.inDate)
        inCompany = QLabel('来源: ')
        inCompany.setBuddy(self.inCompany)
        kind = QLabel('类别: ')
        kind.setBuddy(self.inKinds)
        name = QLabel('品名: ')
        name.setBuddy(self.inName)
        insize = QLabel('型号: ')
        insize.setBuddy(self.inSize)
        number = QLabel('数量: ')
        number.setBuddy(self.inNumber)
        memo = QLabel('备注: ')
        memo.setBuddy(self.inMemo)
        okButton = QPushButton('提交')
        cancelButton = QPushButton('取消')

        mainLayout = QVBoxLayout()

        inputLayout = QGridLayout()
        inputLayout.addWidget(date, 0, 0)
        inputLayout.addWidget(self.inDate, 0, 1)
        inputLayout.addWidget(inCompany, 1, 0)
        inputLayout.addWidget(self.inCompany, 1, 1)
        inputLayout.addWidget(kind, 2, 0)
        inputLayout.addWidget(self.inKinds, 2, 1)
        inputLayout.addWidget(name, 3, 0)
        inputLayout.addWidget(self.inName, 3, 1)
        inputLayout.addWidget(insize, 4, 0)
        inputLayout.addWidget(self.inSize, 4, 1)
        inputLayout.addWidget(number, 5, 0)
        inputLayout.addWidget(self.inNumber, 5, 1)
        inputLayout.addWidget(memo, 6, 0)
        inputLayout.addWidget(self.inMemo, 6, 1)

        inputBox = QGroupBox()
        inputBox.setTitle('数据录入')
        inputBox.setLayout(inputLayout)
        buttonBox = QHBoxLayout()
        buttonBox.addWidget(okButton)
        buttonBox.addWidget(cancelButton)
        mainLayout.addWidget(inputBox)
        mainLayout.addLayout(buttonBox)
        mainLayout.addWidget(self.inShow)



        form = QDialog()
        form.setLayout(mainLayout)
        form.setWindowTitle('物资入库')
        okButton.clicked.connect(self.updateDataIn)
        cancelButton.clicked.connect(form.reject)

        self.inCompany.addItems(initialData.companyList)
        self.inKinds.addItems(initialData.kinds.keys())
        nowKind = self.inKinds.currentText()
        self.inName.addItems(initialData.kinds[nowKind])
        self.inKinds.currentTextChanged.connect(self.diffName)

        if form.exec_():  # 这种情况下弹出的窗口不会在输入信息后立刻关闭
            return  # 而是可以反复填数据

    def outDataWindow(self):
        date = time.gmtime()
        outDate = "{}/{}/{}".format(date.tm_year, date.tm_mon, date.tm_mday)
        self.outDate = QLineEdit(outDate)
        self.outCompany = QComboBox()
        self.outKinds = QComboBox()
        self.outName = QComboBox()
        self.outSize = QLineEdit()
        self.outNumber = QLineEdit()
        self.outMemo = QLineEdit()
        self.outShow = QListWidget()
        date = QLabel()
        date.setBuddy(self.outDate)
        outCompany = QLabel('去向: ')
        outCompany.setBuddy(self.outCompany)
        kind = QLabel('类别: ')
        kind.setBuddy(self.outKinds)
        name = QLabel('品名: ')
        name.setBuddy(self.outName)
        outsize = QLabel('型号: ')
        outsize.setBuddy(self.outSize)
        number = QLabel('数量: ')
        number.setBuddy(self.outNumber)
        memo = QLabel('备注: ')
        memo.setBuddy(self.outMemo)
        okButton = QPushButton('提交')
        cancelButton = QPushButton('取消')

        mainLayout = QVBoxLayout()

        inputLayout = QGridLayout()
        inputLayout.addWidget(date, 0, 0)
        inputLayout.addWidget(self.outDate, 0, 1)
        inputLayout.addWidget(outCompany, 1, 0)
        inputLayout.addWidget(self.outCompany, 1, 1)
        inputLayout.addWidget(kind, 2, 0)
        inputLayout.addWidget(self.outKinds, 2, 1)
        inputLayout.addWidget(name, 3, 0)
        inputLayout.addWidget(self.outName, 3, 1)
        inputLayout.addWidget(outsize, 4, 0)
        inputLayout.addWidget(self.outSize, 4, 1)
        inputLayout.addWidget(number, 5, 0)
        inputLayout.addWidget(self.outNumber, 5, 1)
        inputLayout.addWidget(memo, 6, 0)
        inputLayout.addWidget(self.outMemo, 6, 1)

        inputBox = QGroupBox()
        inputBox.setTitle('数据录入')
        inputBox.setLayout(inputLayout)
        buttonBox = QHBoxLayout()
        buttonBox.addWidget(okButton)
        buttonBox.addWidget(cancelButton)
        mainLayout.addWidget(inputBox)
        mainLayout.addLayout(buttonBox)
        mainLayout.addWidget(self.outShow)

        form = QDialog()
        form.setLayout(mainLayout)
        form.setWindowTitle('物资出库')
        okButton.clicked.connect(self.updateDataOut)
        cancelButton.clicked.connect(form.reject)

        self.outCompany.addItems(initialData.companyList)
        self.outKinds.addItems(initialData.kinds.keys())
        nowKind = self.outKinds.currentText()
        self.outName.addItems(initialData.kinds[nowKind])
        self.outKinds.currentTextChanged.connect(self.diffNameOut)

        if form.exec_():  # 这种情况下弹出的窗口不会在输入信息后立刻关闭
            return  # 而是可以反复填数据

    def seekDataWindow(self):
        companyLabel = QLabel('单位: ')
        self.seekCompany = QComboBox()
        companyLabel.setBuddy(self.seekCompany)
        self.seekCompany.addItems(initialData.companyList)
        self.seekCompany.setCurrentText(initialData.companyList[0])
        nameLabel = QLabel('品名: ')
        self.seekName = QComboBox()
        nameLabel.setBuddy(self.seekName)
        self.seekName.addItems(initialData.allList)
        self.seekName.setCurrentText(initialData.allList[0])


        self.kucunButton = QPushButton('库存量')
        self.inButton = QPushButton('入库记录')
        self.outButton = QPushButton('出库记录')
        self.seekShow = QListWidget()

        inputBox = QGroupBox()
        inputBox.setTitle('查询条件')
        inputLayout = QFormLayout()
        inputLayout.addRow(companyLabel, self.seekCompany)
        inputLayout.addRow(nameLabel, self.seekName)
        inputBox.setLayout(inputLayout)

        buttonBox = QGroupBox()
        buttonBox.setTitle('功能')
        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.kucunButton)
        buttonLayout.addWidget(self.inButton)
        buttonLayout.addWidget(self.outButton)
        buttonBox.setLayout(buttonLayout)

        userLayout = QHBoxLayout()
        userLayout.addWidget(inputBox)
        userLayout.addWidget(buttonBox)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(userLayout)
        mainLayout.addWidget(self.seekShow)

        form = QDialog()
        form.setLayout(mainLayout)
        form.setWindowTitle('记录查询')
        form.setGeometry(400, 300, 620, 600)

        self.kucunButton.clicked.connect(self.howManyLeft)
        self.inButton.clicked.connect(self.inRecord)
        self.outButton.clicked.connect(self.outRecord)

        self.seekCompany.currentTextChanged.connect(self.howToShow)
        self.seekName.currentTextChanged.connect(self.howToShow)

        if form.exec_():
            return

    def howToShow(self):
        company = self.seekCompany.currentText()
        name = self.seekName.currentText()
        if company == '营房仓库':
            if name == '全部':
                self.kucunButton.clicked.connect(self.howManyLeft)
                self.inButton.clicked.connect(self.inRecord)
                self.outButton.clicked.connect(self.outRecord)
            elif name != '全部':
                self.kucunButton.clicked.connect(self.nHowManyLeft)
                self.inButton.clicked.connect(self.nInRecord)
                self.outButton.clicked.connect(self.nOutRecord)
        elif company != '营房仓库':
            if name == '全部':
                self.kucunButton.clicked.connect(self.caHowManyLeft)
                self.inButton.clicked.connect(self.caInRecord)
                self.outButton.clicked.connect(self.caOutRecord)
            elif name != '全部':
                self.kucunButton.clicked.connect(self.cnHowManyLeft)
                self.inButton.clicked.connect(self.cnInRecord)
                self.outButton.clicked.connect(self.cnOutRecord)



    def diffName(self):
        '''当各类变化时,下面可选的品名也跟着变化'''
        i = self.inKinds.currentText()
        if self.inKinds.currentText() == i:
            self.inName.clear()
            self.inName.addItems(initialData.kinds[i])

    def diffNameOut(self):
        '''当各类变化时,下面可选的品名也跟着变化'''
        i = self.outKinds.currentText()
        if self.outKinds.currentText() == i:
            self.outName.clear()
            self.outName.addItems(initialData.kinds[i])



    def howManyLeft(self):
        conn, curs = self.connectDataBase()
        curs.execute("""select NAME, SIZE, SUM(NUM) from records group by NAME, SIZE""")
        n = []
        for i in curs.fetchall():
            a = """营房仓库  %s %s 库存量为 [ %s ]\n""" % (i[0], i[1], i[2])
            n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()

    def inRecord(self):
        conn, curs = self.connectDataBase()
        curs.execute("""select TIME, COMPANY, NAME, SIZE, NUM, MEMO, USER from records order by TIME""")
        n = []
        for i in curs.fetchall():
            if i[4] > 0:
                a = """%s年%s月%s日  |  %s ===> 营房仓库  %s %s [ %s ]个, 备注: %s 管理员: %s\n""" % (i[0].split('/')[0], i[0].split('/')[1], i[0].split('/')[2], i[1], i[2], i[3], i[4], i[5], i[6])
                n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()

    def outRecord(self):
        conn, curs = self.connectDataBase()
        curs.execute("""select TIME, COMPANY, NAME, SIZE, NUM, MEMO, USER from records order by TIME""")
        n = []
        for i in curs.fetchall():
            if i[4] < 0:
                a = """%s年%s月%s日  |  营房仓库 ===> %s  %s %s [ %s ]个, 备注: %s 管理员: %s\n""" % (i[0].split('/')[0], i[0].split('/')[1], i[0].split('/')[2], i[1], i[2], i[3], -i[4], i[5], i[6])
                n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()

    def nHowManyLeft(self):
        """仓库中某一物品的库存数量"""
        conn, curs = self.connectDataBase()
        curs.execute("""select NAME, SIZE, SUM(NUM) from records where NAME = ? group by SIZE order by SIZE""", (self.seekName.currentText(),))
        n = []
        for i in curs.fetchall():
            a = """营房仓库 共有 %s %s  [ %s ]个\n""" % (i[0], i[1], i[2])
            n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()

    def nInRecord(self):
        """仓库某一物品的入库记录"""
        conn, curs = self.connectDataBase()
        curs.execute("""select TIME, COMPANY, NAME, SIZE, NUM, MEMO, USER from records where NAME = ? order by TIME""", (self.seekName.currentText(),))
        n = []
        for i in curs.fetchall():
            if i[4] > 0:
                a = """%s年%s月%s日  |  %s ===> 营房仓库  %s %s [ %s ]个, 备注: %s 管理员: %s\n""" % (i[0].split('/')[0], i[0].split('/')[1], i[0].split('/')[2], i[1], i[2], i[3], i[4], i[5], i[6])
                n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()

    def nOutRecord(self):
        """仓库某一物品的出库记录"""
        conn, curs = self.connectDataBase()
        curs.execute("""select TIME, COMPANY, NAME, SIZE, NUM, MEMO, USER from records where NAME = ? order by TIME""", (self.seekName.currentText(),))
        n = []
        for i in curs.fetchall():
            if i[4] < 0:
                a = """%s年%s月%s日  |  营房仓库 ===> %s  %s %s [ %s ]个, 备注: %s 管理员: %s\n""" % (i[0].split('/')[0], i[0].split('/')[1], i[0].split('/')[2], i[1], i[2], i[3], -i[4], i[5], i[6])
                n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()

    def caHowManyLeft(self):
        """某一单位所有物品库存量"""
        conn, curs = self.connectDataBase()
        curs.execute("""select COMPANY, NAME, SIZE, SUM(NUM) from records where COMPANY = ? group by NAME, SIZE order by NAME""", (self.seekCompany.currentText(),))
        n = []
        for i in curs.fetchall():
            a = """%s 共领取 %s %s  [ %s ]个\n""" % (i[0], i[1], i[2], -i[3])
            n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()

    def caInRecord(self):
        """某一单位所有物品的入库记录"""
        conn, curs = self.connectDataBase()
        curs.execute("""select TIME, COMPANY, NAME, SIZE, NUM, MEMO, USER from records where COMPANY = ? order by TIME""", (self.seekCompany.currentText(),))
        n = []
        for i in curs.fetchall():
            if i[4] < 0:
                a = """%s年%s月%s日  |  营房仓库 ===> %s  %s %s [ %s ]个, 备注: %s 管理员: %s\n""" % (i[0].split('/')[0], i[0].split('/')[1], i[0].split('/')[2], i[1], i[2], i[3], -i[4], i[5], i[6])
                n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()

    def caOutRecord(self):
        """某一单位所有物品的出库记录"""
        conn, curs = self.connectDataBase()
        curs.execute("""select TIME, COMPANY, NAME, SIZE, NUM, MEMO, USER from records where COMPANY = ? order by TIME""", (self.seekCompany.currentText(),))
        n = []
        for i in curs.fetchall():
            if i[4] > 0:
                a = """%s年%s月%s日  |  %s ===> 营房仓库  %s %s [ %s ]个, 备注: %s 管理员: %s\n""" % (i[0].split('/')[0], i[0].split('/')[1], i[0].split('/')[2], i[1], i[2], i[3], i[4], i[5], i[6])
                n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()

    def cnHowManyLeft(self):
        """某一单位某一物品的库存量"""
        conn, curs = self.connectDataBase()
        curs.execute(
            """select COMPANY, NAME, SIZE, SUM(NUM) from records where COMPANY = ? and NAME = ? group by NAME, SIZE order by NAME""",
            (self.seekCompany.currentText(), self.seekName.currentText()))
        n = []
        for i in curs.fetchall():
            a = """%s 共领取 %s %s  [ %s ]个\n""" % (i[0], i[1], i[2], -i[3])
            n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()

    def cnInRecord(self):
        """某一单位某一物品的入库记录"""
        conn, curs = self.connectDataBase()
        curs.execute(
            """select TIME, COMPANY, NAME, SIZE, NUM, MEMO, USER from records where COMPANY = ? and NAME = ? order by TIME""", (self.seekCompany.currentText(), self.seekName.currentText()))
        n = []
        for i in curs.fetchall():
            if i[4] < 0:
                a = """%s年%s月%s日  |  %s ===> %s  %s %s [ %s ]个  备注: %s  管理员: %s\n""" % (i[0].split('/')[0], i[0].split('/')[1], i[0].split('/')[2], '营房仓库', i[1], i[2], i[3], -i[4], i[5], i[6])
                n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()

    def cnOutRecord(self):
        """某一单位某一物品的出库记录"""
        conn, curs = self.connectDataBase()
        curs.execute(
            """select TIME, COMPANY, NAME, SIZE, NUM, MEMO, USER from records where COMPANY = ? and NAME = ? order by TIME""", (self.seekCompany.currentText(), self.seekName.currentText()))
        n = []
        for i in curs.fetchall():
            if i[4] > 0:
                a = """%s年%s月%s日  |  %s ===> %s  %s %s [ %s ]个  备注: %s  管理员: %s\n""" % (
                i[0].split('/')[0], i[0].split('/')[1], i[0].split('/')[2], i[1], '营房仓库', i[2], i[3], i[4], i[5], i[6])
                n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()

    def whetherHaveRecords(self, n):
        if self.seekShow.count() == 0:
            self.seekShow.addItems(n)
        elif self.seekShow.count() != 0:
            self.seekShow.clear()
            self.seekShow.addItems(n)



    # logic start
    def save_info(self, username, password):
        """保存用户账号信息,用shelve存储"""
        with shelve.open('users_db') as users_db:
            users_db[username] = password
            for i in users_db.keys():
                print(i + ':' + users_db[i])


    def get_md5(self, password):
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        pass_md5 = md5.hexdigest()
        return pass_md5


    def register(self):
        username = self.registerName.text()
        with shelve.open('users_db') as users_info:
            if username not in users_info.keys():
                while True:
                    password_1 = self.registerPassword1.text()
                    password_2 = self.registerPassword2.text()
                    if password_1 == password_2:
                        password = self.get_md5(password_2)
                        self.save_info(username, password)
                        QMessageBox.information(self, '注册成功', "OK! 新用户[%s]注册成功" % username)
                        self.registerName.clear()
                        self.registerPassword1.clear()
                        self.registerPassword2.clear()
                        self.registerName.setFocus()
                        return
                    elif password_1 != password_2:
                        QMessageBox.information(self, '输入错误', "ERROR! 两次密码不一致,请重新输入!")
                        self.registerPassword1.setFocus()
                        self.registerPassword1.selectAll()
                        return
            elif username in users_info.keys():
                QMessageBox.information(self, '输入错误', "ERROR! 用户已存在,请重新输入!")


    def login(self):
        username = self.userName.text()
        users_info = shelve.open('users_db')
        if username == 'register':
            self.registerWindow()
        elif username in users_info.keys():
            password = self.password.text()
            if users_info[username] == self.get_md5(password):
                conn, curs = self.connectDataBase()
                self.createDataBase(conn, curs)
                self.featureWindow()
            elif users_info[username] != self.get_md5(password):
                QMessageBox.information(self, '密码错误', '密码错误,请重新输入!')
        elif username not in users_info:
            QMessageBox.information(self, '用户不存在', "用户不存在,请重新输入!")
        users_info.close()


    def connectDataBase(self):
        conn = sqlite3.connect('yfk.db')
        curs = conn.cursor()
        return conn, curs


    def createDataBase(self, conn, curs):
        curs.execute("""create table if not exists records (
                                              TIME char,
                                              COMPANY char,
                                              NAME char,
                                              SIZE char,
                                              NUM int,
                                              MEMO char,
                                              USER char)""")
        conn.commit()
        curs.close()

    def updateDataIn(self):
        conn, curs = self.connectDataBase()
        inDate = self.inDate.text()
        inCompany = self.inCompany.currentText()
        inName = self.inName.currentText()
        inSize = self.inSize.text()
        inNumber = self.inNumber.text()
        inMemo = self.inMemo.text()
        inUser = self.userName.text()
        if inName != '' and inNumber != '':
            reply = QMessageBox.question(self, '请确认', '是否入库{}{} [{}]个?'.format(inName, inSize, inNumber), QMessageBox.Yes|QMessageBox.No)
            if reply == QMessageBox.Yes:
                curs.execute("""insert into records values (?,?,?,?,?,?,?)""", (inDate, inCompany, inName, inSize, int(inNumber),  inMemo, inUser))
                conn.commit()
                curs.close()
                string = "[OK!] 管理员{0} 入库{1} {2} [{3}]个".format(inUser, inName, inSize, inNumber)
                self.inShow.addItem(string)
            else:
                return
        elif inName == '' or inNumber == '':
            QMessageBox.information(self, 'error', '输入信息不全!')
            return

    def updateDataOut(self):
        conn, curs = self.connectDataBase()
        outDate = self.outDate.text()
        outCompany = self.outCompany.currentText()
        outName = self.outName.currentText()
        outSize = self.outSize.text()
        outNumber = self.outNumber.text()
        outMemo = self.outMemo.text()
        outUser = self.userName.text()
        if outName != '' and outNumber != '':
            reply = QMessageBox.question(self, '请确认', '是否入库{}{} [{}]个?'.format(outName, outSize, outNumber),
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                curs.execute("""insert into records values (?,?,?,?,?,?,?)""",
                             (outDate, outCompany, outName, outSize, -int(outNumber), outMemo, outUser))
                conn.commit()
                curs.close()
                string = "[OK!] 管理员{0} 出库{1} {2} [{3}]个".format(outUser, outName, outSize, outNumber)
                self.outShow.addItem(string)
            else:
                return
        elif outName == '' or outNumber == '':
            QMessageBox.information(self, 'error', '输入信息不全!')
            return


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    x = Form()
    x.show()
    sys.exit(app.exec_())