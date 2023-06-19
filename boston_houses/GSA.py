import numpy as np
import random
import math

class GSA:
    def __init__(self,qA=1.5,qT=1.1,qV=1.1,To=1.0):
        self.qA = qA
        self.qT = qT
        self.qV = qV
        self.To = To

    def GSA_ini(self):
        """ This routine initializes the GSA parameters """
        D = 0
        Pi = np.pi

        #Acceptance probability
        qA1 = self.qA - 1.0

        #Temperature
        qT1 = self.qT - 1.0
        Tq = self.To * (2 ** qT1 - 1)

        #Visiting Probability
        qV1 = self.qV - 1.0

        if D == 0:
            A = 1
        else:
            coef1 = (qV1 / Pi) ** 0.5
            gammaUp = math.gamma(1/qV1+(D-1)/2)
            gammaDown = math.gamma(1 / qV1 - 1 / 2)
            A = coef1 * gammaUp/gammaDown

        return Tq, A, qA1, qV1, qT1

    def Temperature(self,t,Tq,qT1):
        """ This routine returns the temperature that will be used to calculate the deltax """
        return Tq / ((1 + t) ** qT1 - 1)

    def Delta_x(self,T,qV1,A,factor):
        """ This routine returns the deltax to be used in each step """
        a = -1/(qV1-2)
        b = 2 * a
        c = 1/qV1
        R = random.random()
        dX = A * T**a /(1+qV1*R*R/(T**b))**c
        dX = dX * random.choice([-1,1]) * factor
        return dX

    def gsa(self,nDimension,func,NStopMax=1000,X_0='none',factor=1):
        """
        - Obrigatórios:
        :param nDimension: A quantidade de parâmetros a serem ajustados.
        :param func: Função Custo criada pelo usuário deve receber um vetor de tamanho nDimension e retornar um número que será minimizado.

        - Opcionais:
        :param NStopMax:  Número total de ciclos do ajuste. Default = 1000
        :param qA: Parâmetro 'q' de Tsallis para probabilidade de aceitação. Default = 1.5
        :param qT: Parâmetro 'q' de Tsallis para temperatura. Default = 1.1
        :param qV: Parâmetro 'q' de Tsallis para visitação. Default = 1.1
        :param To: Temperatura Inicial

        :return: X_Min, func_Min
                 X_Min: O vetor de tamanho = nDimension contendo os parâmetros ajustados.
                 func_Min: O valor minimizado de retorno da Função Custo.
        """

        Tq, A, qA1, qV1, qT1 = self.GSA_ini()
        if X_0 == 'none':
            X_0 = np.array([random.uniform(-1, 1)*factor for n in range(nDimension)])
        X_Min = np.copy(X_0)

        func_0 = func(X_0)
        func_Min = func_0
        conv_func = []
        for t in range(1,NStopMax):
            T = self.Temperature(t, Tq, qT1)
            X_t = X_0 + np.array([self.Delta_x(T,qV1,A,factor) for n in range(nDimension)])
            func_t = func(X_t)
            if func_t <= func_0:
                X_0 = np.copy(X_t)
                func_0 = func_t
                if func_t <= func_Min:
                    func_Min = func_t
                    X_Min = np.copy(X_t)
                    conv_func.append(func_Min)

            elif self.qA != 1.0:
                DeltaE = func_t - func_0
                PqA = 1.0 / ((1.0 + qA1 * DeltaE / T) ** (1.0 / qA1))
                if random.random() < PqA:
                    X_0 = X_t.copy()
                    func_0 = func_t

        self.X_Min, self.func_Min, self.conv_func =  X_Min, func_Min, conv_func


class functions:
    def __init__(self,X, Y,type):
        def polinomio(X_t):
            YFit = 0
            for n in range(len(X_t)-1,-1,-1):
                YFit += X_t[n] * np.power(X,n)
            erro = YFit - Y
            return sum(erro * erro) / len(X)

        self.func =  {'pol': polinomio}[type]

