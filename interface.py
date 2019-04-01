# -*- coding: utf-8 -*-
"""
METODOS DE SPLINES PARA INTERPOLACAO POLINOMIAL
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from splines import SplineInterpolation


Ui_MainWindow, QtBaseClass = uic.loadUiType("splinesinterface.ui")

class MyApp(QMainWindow):
    """ Carrega a interface e conecta o botao de calcular ao metodo calcularSplines
    """
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonCalcular.clicked.connect(self.calcularSplines)
    
       
    def calcularSplines(self):
        """ interpola os pontos a partir de um passo (default = 0.1) utilizando
            o metodo de splines. Recebe as entradas da interface, as trata, aplica
            o metodo e retorna para a interface os pontos interpolados. Plota o
            grafico resultante dos pontos interpolados.
        """
        Xfinal = [] 
        Yfinal = []
        X = self.ui.textEditX.toPlainText()#  strings de entrada
        Y = self.ui.textEditY.toPlainText()# Lê os valores de fx
        
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
        
        SaidaDosPontos = ""
        for i in range(0, len(resultado)):  
            SaidaDosPontos += "P(" + (str)(resultadoDeX[i]) + ") = " + (str)(resultado[i]) + "\n"
        
        #calculo de um ponto qualquer dentro do intervalo
        if (self.ui.lineEditPx.text() != "" ):
            pontoEsp = (float)(self.ui.lineEditPx.text())
            self.ui.lineEditPx2.setText((str)(splines.interpolate(pontoEsp)))
        self.ui.textEditResultado.setText(SaidaDosPontos)
        
    
        self.desenhaSplines(resultadoDeX, resultado, Xfinal, Yfinal)
     
        
    def desenhaSplines(self, xinterpolados, yinterpolados, xFinal, fxFinal):
        """ A partir de um conjunto de pontos, plota um grafico e o exibe em um
            objeto MplWidget da interface.
        """
        
        
        self.ui.MplWidgetSplines.canvas.axes.clear()
        self.ui.MplWidgetSplines.canvas.axes.axhline(y=0, color='r')
        self.ui.MplWidgetSplines.canvas.axes.plot(xinterpolados, yinterpolados, label='P(x)') #pontos interpolados
        self.ui.MplWidgetSplines.canvas.axes.plot(xFinal, fxFinal, 'ro', label='(x , f(x))') #pontos de entrada
        self.ui.MplWidgetSplines.canvas.axes.legend()
        self.ui.MplWidgetSplines.canvas.axes.grid()
        self.ui.MplWidgetSplines.canvas.draw()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())