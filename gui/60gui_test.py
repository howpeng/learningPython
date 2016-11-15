from PyQt5.QtWidgets import QWidget, QApplication, QComboBox, QDialogButtonBox, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QMenuBar, QMenu, QGridLayout, QComboBox, QFormLayout, QTextBrowser

class Form(QWidget):

    def __init__(self):
        super().__init__()

        self.cm()
        self.createHorizonGroupBox()
        self.createGridGroupBox()

        mainLayout = QVBoxLayout()
        mainLayout.setMenuBar(self.menuBar)
        mainLayout.addWidget(self.horizonGroupBox)
        mainLayout.addWidget(self.gridGroupBox)
        self.setLayout(mainLayout)
        self.setWindowTitle('60YFK仓库管理系统')
        self.show()
        #self.menuBar.setNativeMenuBar(False) # 此语句用来在Mac系统下显示菜单


    def cm(self):
        self.menuBar = QMenuBar()

        self.fileMenu = QMenu("&File", self)
        self.printAction = self.fileMenu.addAction('&Print')
        self.printAction.setShortcut('Ctrl+P')
        self.menuBar.addMenu(self.fileMenu)

        self.printAction.triggered.connect(self.printaa)

    def printaa(self):
        print('helo you are a DA SHA BI')

    def createHorizonGroupBox(self):
        self.horizonGroupBox = QGroupBox('功能')
        layout = QHBoxLayout()

        self.buttonIN = QPushButton('入库')
        self.buttonOUT = QPushButton('出库')
        self.buttonSEEK = QPushButton('查询')
        layout.addWidget(self.buttonIN)
        layout.addWidget(self.buttonOUT)
        layout.addWidget(self.buttonSEEK)

        self.horizonGroupBox.setLayout(layout)

    def show_state(self):
        text = self.in_num.text()
        self.state.setText(text)

    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox('数据录入')
        layout = QFormLayout()

        self.in_time = QLabel('时期：')
        self.in_class = QComboBox(self)
        self.in_name = QComboBox(self)
        self.in_type = QComboBox(self)
        self.in_num = QLineEdit()

        i_class = {'水料', '电料'}
        in_dl = {'lingt', 'kjkj', 'jkjk'}
        in_sl = {'211', '985'}

        self.in_class.addItems(i_class)



        self.state = QTextBrowser()
        layout.addRow(QLabel('时期：'), QLineEdit())
        layout.addRow(QLabel('类别：'), self.in_class)
        layout.addRow(QLabel('品名：'), self.in_name)
        layout.addRow(QLabel('型号：'), self.in_type)
        layout.addRow(QLabel('数量：'), self.in_num)
        layout.addRow(self.state)
        self.in_num.textChanged[str].connect(self.show_state)

        self.gridGroupBox.setLayout(layout)







if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    bbox = Form()
    sys.exit(app.exec_())