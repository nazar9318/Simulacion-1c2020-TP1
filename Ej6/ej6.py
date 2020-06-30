from scipy.stats import chi2
import scipy.stats as st
import numpy as np

def ej6():
    f_obs = [262, 582, 868, 1081, 1353, 1625, 1394, 1078, 850, 585, 322]
    probabilidades_caras = np.array([(1/36), (2/36), (3/36), (4/36), (5/36), (6/36), (5/36), (4/36), (3/36), (2/36), (1/36)])
    cant_observaciones = sum(f_obs)

    alfa = 0.01

    f_esp = cant_observaciones * probabilidades_caras

    (D2,p_valor)=st.chisquare(f_obs,f_esp)

    print ('\nFrecuencias esperadas: ', f_esp)

    print ('\nP-valor: ', p_valor)

    if p_valor < alfa:
        print ('\nResultado del test: se rechaza la H0')
    else:
        print ('\nResultado del test: no hay evidencia suficiente para rechazar H0')

ej6()
