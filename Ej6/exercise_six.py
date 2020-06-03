from scipy.stats import chi2
from exercise_two import exercise_two

releases = exercise_two()
frecuencias = releases.values()
lanzamientos = sum(frecuencias)
cantidadDeClases = len(frecuencias)
gradosDeLibertad = cantidadDeClases - 1
nivelDeSignificacion = 0.01

frecuenciaEsperada = lanzamientos/cantidadDeClases

D2 = sum([(fO - frecuenciaEsperada)**2 for fO in frecuencias])/(frecuenciaEsperada)

limiteSuperior = chi2.ppf(1 - nivelDeSignificacion,df=gradosDeLibertad)

print("D2: {}".format(D2))
print("Limite superior: {}".format(limiteSuperior))


if D2 <= limiteSuperior:
    print("El test acepta la hipotesis nula")
else:
    print("El test rechaza la hipotesis nula")

