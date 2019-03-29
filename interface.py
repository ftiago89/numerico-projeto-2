# -*- coding: utf-8 -*-
"""
METODOS DE HALLEY E RIDDERS PARA CALCULO DE RAIZES DE FUNCOES
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from splines import SplineInterpolation



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
        Xfinal = []
        Yfinal = []
        X = self.ui.textEditX.toPlainText()
        Y = self.ui.textEditY.toPlainText()
        Xfinal = X.split('\n')
        for i in range(0, len(Xfinal)):
            Xfinal[i] = (float)(Xfinal[i])
            
        Yfinal = Y.split('\n')
        for i in range(0, len(Yfinal)):
            Yfinal[i] = (float)(Yfinal[i])
            
        S   = 0.1        # passo da interpolacao
        S1 = 1 / S      # Inverso de S
        splines = SplineInterpolation(Xfinal, Yfinal)
        resultado = []
        for x in [x / S1 for x in range(int(Xfinal[0] / S), int(Xfinal[-1] / S) + 1)]:
            resultado.append(splines.interpolate(x))
        self.ui.textEditResultado.setText(resultado)

                
        
     
    #funcao para desenhar o grafico na interface
#    def desenhaSplines(self):
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())