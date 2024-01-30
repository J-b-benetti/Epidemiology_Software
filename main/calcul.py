from math import *

# x00 = None
# x01 = None
# x10 = None
# x11 = None

'''while x00 is None or x01 is None or x10 is None or x11 is None:
    try:
        if x00 is None:
            x00 = int(input("Entrer X0,0: "))
        if x01 is None:
            x01 = int(input("Entrer X0,1: "))
        if x10 is None:
            x10 = int(input("Entrer X1,0: "))
        if x11 is None:
            x11 = int(input("Entrer X1,1: "))
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
'''

def n0(x00, x01):
    return x00 + x01

def n1(x10, x11):
    return x10 + x11

def m0(x00, x10):
    return x00 + x10

def m1(x01, x11):
    return x01 + x11

def total(n0, n1):
    return n0 + n1

def r0(x01, somme_n0):
    return round(x01 / somme_n0, 2)

def r1(x11, somme_n1):
    return round(x11 / somme_n1, 2)

def r(somme_m1, total):
    return round(somme_m1 / total, 2)

def f0(x10, somme_m0):
    return round(x10 / somme_m0, 2)

def f1(x11, somme_m1):
    return round(x11 / somme_m1, 2)

def f(somme_n1, total):
    return round(somme_n1 / total, 2)

def odd_ratio_d_e(x00, x11, x10, x01):
    return round((x00 * x11) / (x10 * x01), 2)

def odd_ratio_e_d(x00, x11, x10, x01):
    return round((x00 * x11) / (x10 * x01), 2)

def var_r1_r0(r, somme_n0, somme_n1):
    calcul = r * (1 - r) * (1 / somme_n0 + 1 / somme_n1)
    return calcul

def var_f1_f0(f, somme_m0, somme_m1):
    calcul = f * (1 - f) * (1 / somme_m0 + 1 / somme_m1)
    return calcul

def test_hypothese_d_e(x11, x01, somme_n0, somme_n1, somme_m1, total):
    calcul = abs((r1(x11, somme_n1) - r0(x01, somme_n0)) / sqrt(var_r1_r0(r(somme_m1, total), somme_n0, somme_n1)))
    if calcul > 2.58:
        return "L'hypothèse de départ H0 est rejetée.\nE et D ne sont pas indépendant\nsur l'intervalle de confiance de " \
               "95 et 98 %\nValeur : ", round(calcul, 2)
    elif calcul > 1.96:
        return "L'hypothèse de départ H0 est rejetée.\nE et D ne sont pas indépendant\nsur l'intervalle de confiance de " \
               "95 %\nValeur : ", round(calcul, 2)
    else:
        return "L'hypothèse de départ H0 n'est pas rejetée.\nE et D sont indépendants\nValeur : ", round(calcul, 2)

def nu_d_e(x00, x11, x10, x01):
    odd_ratio = odd_ratio_d_e(x00, x11, x10, x01)
    calcul = log(odd_ratio)
    return round(calcul, 2)

def var_nu_d_e(x00, x01, x10, x11):
    return round((1 / x00) + (1 / x01) + (1 / x10) + (1 / x11), 2)

def intervalle_confiance_d_e(x00, x11, x10, x01):
    val_min = exp(nu_d_e(x00, x11, x10, x01) - 1.96*sqrt(var_nu_d_e(x00, x11, x10, x01)))
    val_max = exp(nu_d_e(x00, x11, x10, x01) + 1.96*sqrt(var_nu_d_e(x00, x01, x10, x11)))
    return [round(val_min, 2), round(val_max, 2)]

# Pour E/D

def test_hypothese_e_d(x11, x10, somme_m0, somme_m1, somme_n1, total):
    calcul = abs((f1(x11, somme_m1) - f0(x10, somme_m0)) / sqrt(var_f1_f0(r(somme_n1, total), somme_m0, somme_m1)))
    if calcul > 2.58:
        return "L'hypothèse de départ H0 est rejetée.\nE et D ne sont pas indépendant\nsur l'intervalle de confiance de " \
               "95 et 98 %\nValeur : ", round(calcul, 2)
    elif calcul > 1.96:
        return "L'hypothèse de départ H0 est rejetée.\nE et D ne sont pas indépendant\nsur l'intervalle de confiance de " \
               "95 %\nValeur : ", round(calcul, 2)
    else:
        return "L'hypothèse de départ H0 n'est pas rejetée.\nE et D sont indépendants\nValeur : ", round(calcul, 2)

def nu_e_d(x00, x11, x10, x01):
    odd_ratio = odd_ratio_d_e(x00, x11, x10, x01)
    calcul = log(odd_ratio)
    return round(calcul, 2)

def var_nu_e_d(x00, x01, x10, x11):
    return round((1 / x00) + (1 / x01) + (1 / x10) + (1 / x11), 2)

def intervalle_confiance_e_d(x00, x11, x10, x01):
    val_min = exp(nu_d_e(x00, x11, x10, x01) - 1.96*sqrt(var_nu_d_e(x00, x11, x10, x01)))
    val_max = exp(nu_d_e(x00, x11, x10, x01) + 1.96*sqrt(var_nu_d_e(x00, x01, x10, x11)))
    return [round(val_min, 2), round(val_max, 2)]



'''
print("X0,0: ", x00, "\nX0,1: ", x01, "\nX1,0: ", x10, "\nX1,1: ", x11)
print()
print("n0: ", n0(), "\nn1: ", n1(), "\nm0: ", m0(), "\nm1: ", m1())
print("Total: ", total())
print()
print("R0: ", r0(), "R1: ", r1())
print()
print("R: ", r())

print("Odd Ratio D/E: ", odd_ratio_d_e())
print("Hypothèse: ", test_hypothese_d_e())
print("Nu D/E: ", nu_d_e())
print("Var(nu D/E): ", var_nu_d_e())
print("IC(1 - alpha) (D/E): ", intervalle_confiance_d_e())

print("-------------------------------")

print("F0: ", f0(), "F1: ", f1())
print("F: ", f())

print("Odd Ratio E/D: ", odd_ratio_e_d())
print("Hypothèse: ", test_hypothese_e_d())
print("Nu E/D: ", nu_e_d())
print("Var(nu E/D): ", var_nu_e_d())
print("IC(1 - alpha) (E/D): ", intervalle_confiance_e_d())
'''