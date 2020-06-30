from scipy.stats import chi2
import scipy.stats as st

actual = {2: 262, 3: 582, 4: 868, 5: 1081, 6: 1353, 7: 1625, 8: 1394, 9: 1078, 10: 850, 11: 585, 12: 322}
probabilties = {2:1.0/36,3:2.0/36,4:3.0/36,5:4.0/36,6:5.0/36,7:6.0/36,8:5.0/36,9:4.0/36,10:4.0/36,11:2.0/36,12:1.0/36}
expected = {}

for key in actual:
    expected[key] = probabilties[key]

probabilidades_actuales = list(map(lambda key :key*1.0 / 10000, actual.values()))
print("actual "+str(probabilidades_actuales))
print("expected "+str(expected.values()))
nivelDeSignificacion = 0.01



(D2,p_value) = st.chisquare(f_obs = probabilidades_actuales, f_exp = expected.values())

print("D2_2: {}".format(D2))
print("P_value: {}".format(p_value))

if p_value >= nivelDeSignificacion:
    print("Aceptamos ")
else:
    print("Rechazamos")