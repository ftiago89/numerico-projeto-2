# -*- coding: utf-8 -*-

class HermiteInterpolation:

    def interpolation(self, x, x_j, f_j, diffF_j, n=0):
        """
        Return x avaliado pela interpolacao.
    
        ENTRADA:
          * x: ponto para avaliar
          * x_j: lista das coordenadas x
          * f_j: lista de f(x)
          * diffF_j: derivadas f'(x)
          * n: grau do polinomio (opcional)
    
        SAIDA:
          * y(x): valor de x interpolado
          """
    
        if type(x_j) != type(f_j) or type(x_j) != type([]):
            print ("Erro: Parametros de tipos diferentes")
            return float("NaN")
    
        if len(x_j) != len(f_j) or len(x_j) != len(diffF_j):
            print ("Erro: A quantidade de coordenadas devem ser iguais")
            return float("NaN")
    
        if n <= 0:
            n = len(x_j)
        else:
            n = n + 1
    
        p = 0.0
        for j in range(n):
            # lagrange polinomial
            xj = x_j[j]
            ljn_num = 1.0
            ljn_den = 1.0
            for i in range(n):
                xi = x_j[i]
                if i != j:
                    ljn_num *= (x - xi)
                    ljn_den *= (xj - xi)
            ljn = ljn_num / ljn_den
    
            # hermite interpolation
            diff_ljn = 0
            for i in range(n):
                xi = x_j[i]
                if i != j:
                    diff_ljn += 1.0 / (xj - xi)
    
            hjn = (1.0 - 2 * (x - xj) * diff_ljn) * (ljn * ljn)
            hjn_ = (x - xj) * (ljn * ljn)
            p += hjn * f_j[j] + hjn_ * diffF_j[j]
        return p