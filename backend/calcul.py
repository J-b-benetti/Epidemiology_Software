from math import *

x00 = None
x01 = None
x10 = None
x11 = None

while x00 is None or x01 is None or x10 is None or x11 is None:
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


def n0():
    return x00 + x01


def n1():
    return x10 + x11


def m0():
    return x00 + x10


def m1():
    return x01 + x11


def total():
    try:
        first_calc = n0() + n1()
        second_calc = m0() + m1()
        if first_calc != second_calc:
            raise ValueError("Le total n'est pas le bon.")
        else:
            return x00 + x01 + x10 + x11
    except ValueError as e:
        return str(e)


def r0():
    return round(x01 / n0(), 2)


def r1():
    return round(x11 / n1(), 2)


def r():
    return round(m1() / total(), 2)


def odd_ratio():
    return round((x00 * x11) / (x10 * x01), 2)


def var_r1_r0():
    calcul = r() * (1 - r()) * (1 / n0() + 1 / n1())
    return calcul


def test_hypothese():
    calcul = abs((r1() - r0()) / sqrt(var_r1_r0()))
    if calcul > 2.58:
        return "L'hypothèse de départ H0 est rejetée. E et D ne sont pas indépendant sur l'intervalle de confiance de " \
               "98 % ", calcul
    elif calcul > 1.96:
        return "L'hypothèse de départ H0 est rejetée. E et D ne sont pas indépendant sur l'intervalle de confiance de " \
               "95 % ", calcul
    else:
        return "L'hypothèse de départ H0 n'est pas rejetée. E et D sont indépendants", calcul


def nu():
    calcul = log(odd_ratio())
    return round(calcul, 2)


def var_nu():
    return round((1 / x00) + (1 / x01) + (1 / x10) + (1 / x11), 2)


def intervalle_confiance():
    val_min = exp(nu() - 1.96*sqrt(var_nu()))
    val_max = exp(nu() + 1.96*sqrt(var_nu()))
    return [round(val_min, 2), round(val_max, 2)]


print("X0,0: ", x00, "X0,1: ", x01, "X1,0: ", x10, "X1,1: ", x11)
print("n0: ", n0(), "n1: ", n1(), "m0: ", m0(), "m1: ", m1())
print("Total: ", total())

print("R0: ", r0(), "R1: ", r1())
print("R: ", r())

print("Odd Ratio: ", odd_ratio())
print("Hypothèse: ", test_hypothese())
print("Nu: ", nu())
print("Var(nu): ", var_nu())
print("IC(1 - alpha): ", intervalle_confiance())
