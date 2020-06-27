from scipy.stats import chi2
import scipy.stats as st

releases = {8: 699, 7: 785, 4: 433, 11: 285, 6: 696, 9: 537, 3: 286, 10: 443, 5: 545, 2: 130, 12: 161}
frecuencias = releases.values()
lanzamientos = sum(frecuencias)
cantidadDeClases = len(frecuencias)
gradosDeLibertad = cantidadDeClases - 1
nivelDeSignificacion = 0.01

frecuenciaEsperada = lanzamientos/cantidadDeClases

limiteSuperior = chi2.ppf(1 - nivelDeSignificacion,df=gradosDeLibertad)
(D2,p_value) = st.chisquare(f_obs = frecuencias, f_exp = [frecuenciaEsperada]*cantidadDeClases)

print("D2_2: {}".format(D2))
print("P_value: {}".format(p_value))

print("Limite superior: {}".format(limiteSuperior))


if D2 <= limiteSuperior:
    print("El test acepta la hipotesis nula")
else:
    print("El test rechaza la hipotesis nula")

