#!/usr/bin/env python3


import sys
from PyQt5.QtWidgets import QApplication, QCheckBox, QComboBox, QDialog, QGridLayout, QHBoxLayout, QLabel, QPushButton, QSpinBox, QVBoxLayout


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.name = 'How Peng'
        self.age = 27


        setButton = QPushButton('Choice')
        showButton = QPushButton('Show')
        layout = QVBoxLayout()
        layout.addWidget(setButton)
        layout.addWidget(showButton)
        self.setLayout(layout)

        setButton.clicked.connect(self.set)
        showButton.clicked.connect(self.display)

    def set(self):
        setName = QComboBox()
        setName.addItems(['How Peng', 'Jixing Xu', 'Jiujian Shi', 'Xiangguo Dang'])
        setAge = QSpinBox()
        setAge.setRange(20, 50)
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout = QVBoxLayout()
        layout.addWidget(setName)
        layout.addWidget(setAge)
        layout.addLayout(buttonLayout)

        form = QDialog()
        form.setLayout(layout)
        okButton.clicked.connect(form.accept)
        cancelButton.clicked.connect(form.reject)

        if form.exec_():
            self.name = setName.currentText()
            self.age = setAge.value()

    def display(self):
        print(self.name + " " + str(self.age))



app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

