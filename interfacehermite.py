# -*- coding: utf-8 -*-
"""
METODOS DE HERMITE PARA INTERPOLACAO DE POLINOMIOS
"""
import sys
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from hermite import HermiteInterpolation



Ui_MainWindow, QtBaseClass = uic.loadUiType("hermiteinterface.ui")

#classe principal da interface
class MyApp(QMainWindow):
    #load na ui e eventos de botoes
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonCalcular.clicked.connect(self.calcularHermite)
    
    #coleta a funcao da interface e parametros de entrada e usa o metodo de hermite
    #para calcular as raizes da funcao.    
    def calcularHermite(self):
        xFinal = []
        fxFinal = []
        resultadoFinal = ""
        xInterpolados = []
        x = self.ui.textEditX.toPlainText()
        fx = self.ui.textEditFx.toPlainText()
        diff = self.ui.textEditDiff.toPlainText()
        xFinal = x.split('\n')
        for i in range(0, len(xFinal)):
            xFinal[i] = (float)(xFinal[i])
            
        fxFinal = fx.split('\n')
        for i in range(0, len(fxFinal)):
            fxFinal[i] = (float)(fxFinal[i])
            
        diffFinal = diff.split('\n')
        for i in range(0, len(diffFinal)):
            diffFinal[i] = (float)(diffFinal[i])    
            
        S   = 0.1        # passo da interpolacao
        S1 = 1 / S      # Inverso de S
        hermite = HermiteInterpolation()
        resultado = []
        for k in [k / S1 for k in range(int(xFinal[0] / S), int(xFinal[-1] / S) + 1)]:
            resultado.append(hermite.interpolation(k, xFinal, fxFinal, diffFinal))
            xInterpolados.append(k)
        
        for i in range(0, len(resultado)):
            resultadoFinal += "P(" + (str)(xInterpolados[i]) + ") = " + (str)(resultado[i]) + "\n" 
        
        #calculo de um ponto qualquer dentro do intervalo
        if (self.ui.lineEditPx.text() != "" ):
            pontoEsp = (float)(self.ui.lineEditPx.text())
            self.ui.lineEditPx2.setText((str)(hermite.interpolation(pontoEsp, xFinal, fxFinal, diffFinal)))
            
        self.ui.textEditResultado.setText(resultadoFinal)
        self.desenhaGraficoHermite(xFinal, fxFinal, diffFinal)
    
    #funcao para desenhar o grafico na interface    
    def desenhaGraficoHermite(self, xFinal, fxFinal, diffFinal):
        hermite = HermiteInterpolation()
        
        limEsq = (float)(xFinal[0])
        limDir = (float)(xFinal[len(xFinal)-1])
        
        x = np.arange(limEsq, limDir, 0.1)
        
        self.ui.mplWidgetGrafico.canvas.axes.clear()
        self.ui.mplWidgetGrafico.canvas.draw()
        self.ui.mplWidgetGrafico.canvas.axes.set_xlim([limEsq, limDir])
        self.ui.mplWidgetGrafico.canvas.axes.axhline(y=0, color='r')
        self.ui.mplWidgetGrafico.canvas.axes.plot(x, hermite.interpolation(x, xFinal, fxFinal, diffFinal), label='P(x)')
        self.ui.mplWidgetGrafico.canvas.axes.plot(xFinal, fxFinal, 'ro', label='(x , f(x))')
        self.ui.mplWidgetGrafico.canvas.axes.legend()
        self.ui.mplWidgetGrafico.canvas.axes.grid()
        self.ui.mplWidgetGrafico.canvas.draw()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())