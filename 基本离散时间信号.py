# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 30, 200, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.button1)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 130, 200, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.button2)

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 230, 200, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.button3)

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 330, 200, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.button4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "基本离散时间信号"))
        self.pushButton.setText(_translate("Form", "冲激序列"))
        self.pushButton_2.setText(_translate("Form", "阶跃序列"))
        self.pushButton_3.setText(_translate("Form", "正弦序列"))
        self.pushButton_4.setText(_translate("Form", "实指数序列"))

class Function(QMainWindow,Ui_Form):
 def __init__(self,parent=None):
  super(Function,self).__init__(parent)
  self.setupUi(self)
 
 def button1(self):
  def t(x):
   y = x == 0 
   return y
  x3=np.linspace(-5, 5,11)
  y3=t(x3)
  plt.stem(x3,y3)
  plt.grid(True)
  plt.title('冲激序列')
  plt.show()

 def button2(self):
  def u(x):
   y = x > 0
   return y
  x4=np.linspace(-5, 5, 10)
  y4=u(x4)
  plt.stem(x4,y4)
  plt.grid(True)
  plt.title('阶跃序列')
  plt.show()
  
 def button3(self):
  x=np.linspace(0,5,20)
  y2=np.sin(0.5*np.pi*x+2)
  plt.title(r'正弦序列$x(n)=sin(π/2*x+2)$')
  plt.grid(True)
  plt.stem(x,y2)
  plt.show()

 def button4(self):
  x1=np.linspace(0,10,10)
  y5=0.6**x1
  plt.grid(True)
  plt.title(r'实指数序列$x(n)=0.6^x$')
  plt.stem(x1,y5)
  plt.show()

if __name__ == "__main__":
 app = QApplication(sys.argv)
 test_demo = Function()
 test_demo.show()
 sys.exit(app.exec_())