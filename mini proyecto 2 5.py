import sys
import random
from miniproyecto2 import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.ronda=0
        self.vidas = {}        
        self.bar= []
        self.sub=[]
        self.por=[]
        for i in range(2):
            n1 = random.randint(1, 5)
            n2 = random.randint(1, 5)
            p = "ola"+str(n1) + str(n2)
            print(p)
            p= self.verificador(p)
            self.bar.append(p)
            self.vidas[p]=2
            barco = self.findChild(QtWidgets.QLabel,p)
            barco.setPixmap(QtGui.QPixmap("barco.jpg"))
        for i in range(4):
            n1 = random.randint(1, 5)
            n2 = random.randint(1, 5)
            p = "ola"+str(n1) + str(n2)
            print(p)
            p= self.verificador(p)
            self.sub.append(p)
            self.vidas[p]=1
            submarino = self.findChild(QtWidgets.QLabel,p)
            submarino.setPixmap(QtGui.QPixmap("submarino.jpg"))
        for i in range(1):
            n1 = random.randint(1, 5)
            n2 = random.randint(1, 5)
            p = "ola"+str(n1) + str(n2)
            print(p)
            p= self.verificador(p)
            self.por.append(p)
            self.vidas[p]=3
            portaavion = self.findChild(QtWidgets.QLabel,p)
            portaavion.setPixmap(QtGui.QPixmap("porta avion.jpg"))
        for i in range(1,6):
            a = "a"+str(i)+"j1"
            boton = self.findChild(QtWidgets.QPushButton,a)
            boton.clicked.connect(self.misil)
        for i in range(1,6):
            b = "b"+str(i)+"j1"
            boton = self.findChild(QtWidgets.QPushButton,b)
            boton.clicked.connect(self.misil)
        for i in range(1,6):
            c = "c"+str(i)+"j1"
            boton = self.findChild(QtWidgets.QPushButton,c)
            boton.clicked.connect(self.misil)
        for i in range(1,6):
            d = "d"+str(i)+"j1"
            boton = self.findChild(QtWidgets.QPushButton,d)
            boton.clicked.connect(self.misil)
        for i in range(1,6):
            e = "e"+str(i)+"j1"
            boton = self.findChild(QtWidgets.QPushButton,e)
            boton.clicked.connect(self.misil)
        boton = self.findChild(QtWidgets.QPushButton,"bomba")
        boton.clicked.connect(self.atom)
    def atom(self):
        if self.ronda >= 6:
            self.ronda= self.ronda+1
            n1 = random.randint(1, 5)
            n2 = random.randint(1, 5)
            p0 = "ola"+str(n1) + str(n2)
            if n1+1 <= 5:
                p1 = "ola"+str(n1+1) + str(n2)
            else:
                p1 = "ola00"
            if n1-1>=1:
                p2 = "ola"+str(n1-1) + str(n2)
            else:
                p2 = "ola00"
            if n2+1 <= 5:
                p3 = "ola"+str(n1) + str(n2+1)
            else:
                p3 = "ola00"
            if n2-1>=1:
                p4 = "ola"+str(n1) + str(n2-1)
            else:
                p4 = "ola00"
            print(p0)
            if (p0 in self.bar) or (p0 in self.sub) or (p0 in self.por):
                barco = self.findChild(QtWidgets.QLabel,p0)
                barco.setPixmap(QtGui.QPixmap("barco roto.jpg"))
                self.vidas[p0]=0
            if (p1 in self.bar) or (p1 in self.sub) or (p1 in self.por):
                barco = self.findChild(QtWidgets.QLabel,p1)
                barco.setPixmap(QtGui.QPixmap("barco roto.jpg"))
                self.vidas[p1]=0
            if (p2 in self.bar) or (p2 in self.sub) or (p2 in self.por):
                barco = self.findChild(QtWidgets.QLabel,p2)
                barco.setPixmap(QtGui.QPixmap("barco roto.jpg"))
                self.vidas[p2]=0
            if (p3 in self.bar) or (p3 in self.sub) or (p3 in self.por):
                barco = self.findChild(QtWidgets.QLabel,p3)
                barco.setPixmap(QtGui.QPixmap("barco roto.jpg"))
                self.vidas[p3]=0
            if (p4 in self.bar) or (p4 in self.sub) or (p4 in self.por):
                barco = self.findChild(QtWidgets.QLabel,p4)
                barco.setPixmap(QtGui.QPixmap("barco roto.jpg"))
                self.vidas[p4]=0
    def misil(self):
         button=self.sender()
         button_name=button.objectName()
         l="abcde"
         for k,i in enumerate(l):
            for j in range(1,6):
                n= i + str(j)+ "j1"
                m = "ola" + str(j) + str(k+1)
                if (n == button_name) and (m in self.sub):
                    self.ronda=self.ronda+1
                    print(self.ronda)
                    self.vidas[m] = self.vidas[m]-1
                    if self.vidas[m] == 0:
                        submarino = self.findChild(QtWidgets.QLabel,m)
                        submarino.setPixmap(QtGui.QPixmap("barco roto.jpg"))
                elif (n==button_name) and (m in self.bar):
                    self.ronda=self.ronda+1
                    print(self.ronda)
                    self.vidas[m] = self.vidas[m]-1
                    if self.vidas[m] == 0:
                        barco = self.findChild(QtWidgets.QLabel,m)
                        barco.setPixmap(QtGui.QPixmap("barco roto.jpg"))
                    else:
                        n1 = random.randint(1, 5)
                        n2 = random.randint(1, 5)
                        p = "ola"+str(n1) + str(n2)
                        print(p)
                        p= self.verificador(p)
                        barco = self.findChild(QtWidgets.QLabel,m)
                        barco.setPixmap(QtGui.QPixmap("ola.jpg"))
                        self.bar.remove(m)
                        self.bar.append(p)
                        self.vidas[p] = self.vidas[m]
                        barco = self.findChild(QtWidgets.QLabel,p)
                        barco.setPixmap(QtGui.QPixmap("barco.jpg"))
                elif (n == button_name) and (m in self.por):
                    self.ronda=self.ronda+1
                    print(self.ronda)
                    self.vidas[m] = self.vidas[m]-1
                    if self.vidas[m] == 0:
                        portaavion = self.findChild(QtWidgets.QLabel,m)
                        portaavion.setPixmap(QtGui.QPixmap("barco roto.jpg"))
                    else:
                        n1 = random.randint(1, 5)
                        n2 = random.randint(1, 5)
                        p = "ola"+str(n1) + str(n2)
                        print(p)
                        p= self.verificador(p)
                        portaavion = self.findChild(QtWidgets.QLabel,m)
                        portaavion.setPixmap(QtGui.QPixmap("ola.jpg"))
                        self.por.remove(m)
                        self.por.append(p)
                        self.vidas[p] = self.vidas[m]
                        barco = self.findChild(QtWidgets.QLabel,p)
                        barco.setPixmap(QtGui.QPixmap("porta avion.jpg"))
                elif n== button_name and (not(m in self.sub) or not(m in self.bar) or not(m in self.por)):
                    self.ronda=self.ronda+1
                    print(self.ronda)
    def verificador(self,p):
         while True:
             if (p in self.bar) or (p in self.sub) or (p in self.por):
                 n1 = random.randint(1, 5)
                 n2 = random.randint(1, 5)
                 p = "ola"+str(n1) + str(n2)
                 print(p)
             else:
                 break
         return p
         

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()