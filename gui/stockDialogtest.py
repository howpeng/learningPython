# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys

class StockDialog(QDialog):
    def __init__(self, parent=None):
        super(StockDialog, self).__init__(parent)
        self.setWindowTitle(self.tr("堆栈窗口"))

        listWidget = QListWidget()
        listWidget.insertItem(0, self.tr("窗口1"))
        listWidget.insertItem(1, self.tr("窗口2"))
        listWidget.insertItem(2, self.tr("窗口3"))
        label1 = QLabel(self.tr("这是窗口1!"))
        label2 = QLabel(self.tr("这是窗口2!"))
        label3 = QLabel(self.tr("这是窗口3!"))

        stack = QStackedWidget()
        stack.addWidget(label1)
        stack.addWidget(label2)
        stack.addWidget(label3)

        mainLayout = QHBoxLayout(self)
        mainLayout.setSpacing(5)
        mainLayout.addWidget(listWidget)
        mainLayout.addWidget(stack)
        mainLayout.setStretchFactor(listWidget, 1)
        mainLayout.setStretchFactor(stack, 3)

        listWidget.currentRowChanged.connect(stack.setCurrentIndex)


app = QApplication(sys.argv)
main = StockDialog()
main.show()
app.exec_()