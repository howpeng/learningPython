# -*- coding: utf-8 -*-

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
        self.seekCompany = QComboBox()
        self.seekCompany.setEnabled(False)
        self.seekName = QComboBox()
        self.seekName.addItems(initialData.waterList)
        self.seekName.setEnabled(False)
        self.seekDate = QDateEdit()
        self.seekDate.setEnabled(False)
        self.checkCompany = QCheckBox('单位: ')
        self.checkName = QCheckBox('品名: ')


        self.kucunButton = QPushButton('库存量')
        self.inButton = QPushButton('入库记录')
        self.outButton = QPushButton('出库记录')
        self.seekShow = QListWidget()

        inputBox = QGroupBox()
        inputBox.setTitle('查询条件')
        layout = QGridLayout()
        layout.addWidget(self.checkCompany, 0, 0)
        layout.addWidget(self.seekCompany, 0, 1)
        layout.addWidget(self.checkName, 1, 0)
        layout.addWidget(self.seekName, 1, 1)
        layout.addWidget(self.kucunButton, 2, 0)
        layout.addWidget(self.inButton, 2, 1)
        layout.addWidget(self.outButton, 2, 2)

        inputBox.setLayout(layout)
        buttonBox = QHBoxLayout()
        buttonBox.addWidget(self.kucunButton)
        buttonBox.addWidget(self.inButton)
        buttonBox.addWidget(self.outButton)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(inputBox)
        mainLayout.addLayout(buttonBox)
        mainLayout.addWidget(self.seekShow)

        self.seekCompany.addItems(initialData.companyList)
        for i in initialData.kinds.keys():
            self.seekName.addItems(initialData.kinds[i])

        form = QDialog()
        form.setLayout(mainLayout)
        form.setWindowTitle('记录查询')
        form.setGeometry(400, 300, 500, 600)
        self.checkCompany.toggled.connect(self.seekCompany.setEnabled)
        self.checkName.toggled.connect(self.seekName.setEnabled)

        self.kucunButton.clicked.connect(self.howManyLeft)
        self.inButton.clicked.connect(self.inRecord)
        self.outButton.clicked.connect(self.outRecord)
        self.checkCompany.stateChanged.connect(self.howToShow)
        self.checkName.stateChanged.connect(self.howToShow)


        if form.exec_():
            return

    def howToShow(self):
        if not self.checkCompany.isChecked():
            if not self.checkName.isChecked():
                self.kucunButton.clicked.connect(self.howManyLeft)
                self.inButton.clicked.connect(self.inRecord)
                self.outButton.clicked.connect(self.outRecord)
                # if self.checkName.isChecked():
                #  kucunButton.clicked.connect(self.howManyLeft)
                # inButton.clicked.connect(self.inRecord)
                # outButton.clicked.connect(self.outRecord)
        if self.checkCompany.isChecked():
            if not self.checkName.isChecked():
                self.kucunButton.clicked.connect(self.cHowManyLeft)

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
            a = """%s %s 库存量为 %s\n""" % (i[0], i[1], i[2])
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
                a = """%s年%s月%s日 管理员%s从 %s 入库 %s %s %s个, 备注: %s \n""" % (i[0].split('/')[0], i[0].split('/')[1], i[0].split('/')[2], i[6], i[1], i[2], i[3], i[4], i[5])
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
                a = """%s年%s月%s日 管理员%s向 %s 发放 %s %s %s个, 备注: %s \n""" % (
                i[0].split('/')[0], i[0].split('/')[1], i[0].split('/')[2], i[6], i[1], i[2], i[3], i[4], i[5])
                n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()

    def cHowManyLeft(self):
        conn, curs = self.connectDataBase()
        curs.execute("""select COMPANY, NAME, SIZE, SUM(NUM) from records where COMPANY = ? group by COMPANY, NAME""",(self.seekCompany.currentText(),))
        n = []
        for i in curs.fetchall():
            a = """%s 共有 %s %s  [%s]个\n""" % (i[0], i[1], i[2], i[3])
            n.append(a)
        self.whetherHaveRecords(n)
        conn.commit()
        curs.close()
    def nHowManyLeft(self):
        pass
    def cnHowManyLeft(self):
        pass
    def cInRecord(self):
        pass
    def nInRecord(self):
        pass
    def cnInRecord(self):
        pass
    def cOutRecord(self):
        pass
    def nOutRecord(self):
        pass
    def cnOutRecord(self):
        pass

    def whetherHaveRecords(self, n):
        if len(n) == 0:
            QMessageBox.information(self, '无记录', '没有记录!')
            return
        elif len(n) > 0:
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