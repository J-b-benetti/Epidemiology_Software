from math import *

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