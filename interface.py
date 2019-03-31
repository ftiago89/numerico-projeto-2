# -*- coding: utf-8 -*-
"""
METODOS DE HALLEY E RIDDERS PARA CALCULO DE RAIZES DE FUNCOES
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from splines import SplineInterpolation
import matplotlib.pyplot as plt


Ui_MainWindow, QtBaseClass = uic.loadUiType("splinesinterface.ui")

#classe principal da interface
class MyApp(QMainWindow):
    #load na ui e eventos de botoes
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonCalcular.clicked.connect(self.calcularSplines)
    
    #coleta a funcao da interface e parametros de entrada e usa o metodo halley da classe MetodosHalleyRidders
    #para calcular as raizes da funcao.    
    def calcularSplines(self):
        Xfinal = [] # tratam a string X
        Yfinal = []
        X = self.ui.textEditX.toPlainText()#  strings de entrada
        Y = self.ui.textEditY.toPlainText()# Lê os valores de Y
        
        Xfinal = X.split('\n')
        for i in range(0, len(Xfinal)):
            Xfinal[i] = (float)(Xfinal[i])#converte a entrada X em float
            
        Yfinal = Y.split('\n')
        for i in range(0, len(Yfinal)):
            Yfinal[i] = (float)(Yfinal[i])
            
        S   = 0.1        # passo da interpolacao
        S1 = 1 / S      # Inverso de S
        splines = SplineInterpolation(Xfinal, Yfinal)
        resultado = [] # guarda os valores interpolados de Y
        resultadoDeX = []# guarda os valores interpolados de X
        for x in [x / S1 for x in range(int(Xfinal[0] / S), int(Xfinal[-1] / S) + 1)]:
            resultado.append(splines.interpolate(x))
            resultadoDeX.append(x)
            #self.ui.textEditResultado.setText("Testando na interface")
        
        #resultadoFinal = "" #essa variável quarda os valores computados pra Y interpolados
       # Xinterpolados = "" #converte os pontos X interpolados em string
        SaidaDosPontos = ""
        for i in range(0, len(resultado)):  
            #resultadoFinal += (str)(resultado[i]) + "\n"
            #Xinterpolados += (str)(resultadoDeX[i]) + "\n"
            SaidaDosPontos += "(" + (str)(resultadoDeX[i]) + ",  " + (str)(resultado[i]) + ")\n"
            self.ui.textEditResultado.setText(SaidaDosPontos)
        
    
        #print(SaidaDosPontos)
        self.desenhaSplines(resultadoDeX, resultado)
     
    #funcao para desenhar o grafico na interface
    def desenhaSplines(self, xinterpolados, yinterpolados):
        
        self.ui.MplWidgetSplines.canvas.axes.clear()
        self.ui.MplWidgetSplines.canvas.axes.axhline(y=0, color='r')
        self.ui.MplWidgetSplines.canvas.axes.plot(xinterpolados, yinterpolados, label='f(x)')
        self.ui.MplWidgetSplines.canvas.axes.legend()
        self.ui.MplWidgetSplines.canvas.axes.grid()
        self.ui.MplWidgetSplines.canvas.draw()
        
        #plt.title("3-D Spline Interpolation")
        #plt.plot(xinterpolados, yinterpolados)
        #plt.grid(True)
        #plt.xlabel("X interpolados")
        #plt.ylabel("Y interpolados")
        #plt.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())