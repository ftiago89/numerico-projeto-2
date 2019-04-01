#! /usr/local/bin/python3.6
"""
Implementacao do metodo de splines cubicos
"""
class SplineInterpolation:
    def __init__(self, xs, ys):
        """ initicalizacao
        :lista xs: lista dos x de entrada
        :lista ys: lista dos y de entrada
        """
        self.xs, self.ys = xs, ys
        self.n = len(self.xs) - 1
        h = self.__calc_h()
        w = self.__calc_w(h)
        matrix = self.__gen_matrix(h, w)
        v = [0] + self.__gauss_jordan(matrix) + [0]
        self.b = self.__calc_b(v)
        self.a = self.__calc_a(v)
        self.d = self.__calc_d()
        self.c = self.__calc_c(v)

    def interpolate(self, t):
        """ Interpolacao
        :float t: valor pra ser interpolado
        :return resultado  : resultado computado
        """
        try:
            i = self.__search_i(t)
            resultado = self.a[i] * (t - self.xs[i]) ** 3 \
                 + self.b[i] * (t - self.xs[i]) ** 2 \
                 + self.c[i] * (t - self.xs[i]) \
                 + self.d[i]
            return resultado
        except Exception as e:
            raise

    def __calc_h(self):
        """ calculo de H
        :return lista: valores de h
        """
        try:
            return [self.xs[i + 1] - self.xs[i] for i in range(self.n)]
        except Exception as e:
            raise

    def __calc_w(self, h):
        """ calculo de W
        :lista h: valores de h
        :return lista  : valores de w
        """
        try:
            return [
                6 * ((self.ys[i + 1] - self.ys[i]) / h[i]
                   - (self.ys[i] - self.ys[i - 1]) / h[i - 1])
                for i in range(1, self.n)
            ]
        except Exception as e:
            raise

    def __gen_matrix(self, h, w):
        """ geracao da matriz
        :lista   h: valores de h
        :lista   w: valores de w
        :return lista mtx: matriz 2-D gerada
        """
        mtx = [[0 for _ in range(self.n)] for _ in range(self.n - 1)]
        try:
            for i in range(self.n - 1):
                mtx[i][i]     = 2 * (h[i] + h[i + 1])
                mtx[i][-1]    = w[i]
                if i == 0:
                    continue
                mtx[i - 1][i] = h[i]
                mtx[i][i - 1] = h[i]
            return mtx
        except Exception as e:
            raise

    def __gauss_jordan(self, matrix):
        """ Resolve as equacoes lineares
            com o metodo de Gauss Jordan
        :lista mtx: matriz gerada
        :return lista   v: lista de respostas das equacoes lineares
        """
        v = []
        n = self.n - 1
        try:
            for k in range(n):
                p = matrix[k][k]
                for j in range(k, n + 1):
                    matrix[k][j] /= p
                for i in range(n):
                    if i == k:
                        continue
                    d = matrix[i][k]
                    for j in range(k, n + 1):
                        matrix[i][j] -= d * matrix[k][j]
            for row in matrix:
                v.append(row[-1])
            return v
        except Exception as e:
            raise

    def __calc_a(self, v):
        """ calculo de a
        :lista v: valores de v
        :return lista  : valores de a
        """
        try:
            return [
                (v[i + 1] - v[i])
              / (6 * (self.xs[i + 1] - self.xs[i]))
                for i in range(self.n)
            ]
        except Exception as e:
            raise

    def __calc_b(self, v):
        """ calculo de b
        :lista v: valores de v
        :return lista  : valores de b
        """
        try:
            return [v[i] / 2.0 for i in range(self.n)]
        except Exception as e:
            raise

    def __calc_c(self, v):
        """ calculo de c
        :lista v: valores de v
        :return lista  : valores de c
        """
        try:
            return [
                (self.ys[i + 1] - self.ys[i]) / (self.xs[i + 1] - self.xs[i]) \
              - (self.xs[i + 1] - self.xs[i]) * (2 * v[i] + v[i + 1]) / 6
                for i in range(self.n)
            ]
        except Exception as e:
            raise

    def __calc_d(self):
        """ calculo de d
        :return list: valores de d
        """
        try:
            return self.ys
        except Exception as e:
            raise

    def __search_i(self, t):
        """ procura um indice
        :float t: valor para procura
        :return  int i: indice
        """
        i, j = 0, len(self.xs) - 1
        try:
            while i < j:
                k = (i + j) // 2
                if self.xs[k] < t:
                    i = k + 1
                else:
                    j = k
            if i > 0:
                i -= 1
            return i
        except Exception as e:
            raise