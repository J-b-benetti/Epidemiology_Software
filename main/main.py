import tkinter as tk
from tkinter import font
from tkinter import messagebox
import calcul as backend

def get_values():
    values = [] # Tableau contenant les valeurs
    for i in range(2):
        row = []
        for j in range(2):
            value = entry_fields[i][j].get()
            # Vérifier si l'entrée est un nombre entier
            if value.isdigit():
                row.append(int(value))
            else:
                # Si l'entrée n'est pas un nombre entier, ajouter 0 par défaut
                row.append(0)
        values.append(row)
        if any(0 in row for row in values):
            messagebox.showerror("Erreur", "Veuillez remplir toutes les cases avant d'exécuter le programme.")
            return

    sum_rows = [sum(row) for row in values]
    sum_columns = [sum(col) for col in zip(*values)]  # Utilisation de zip pour obtenir les colonnes

    # Calcul des sommes selon les méthodes définies dans le module backend
    sum_n0 = backend.n0(*values[0])
    sum_n1 = backend.n1(*values[1])
    sum_m0 = backend.m0(values[0][0], values[1][0])
    sum_m1 = backend.m1(values[0][1], values[1][1])
    total = backend.total(sum_n0, sum_n1)

    # Pour enquête de cohorte et transversale
    update_entry(r0_entry, backend.r0(values[0][1], sum_n0))
    update_entry(r1_entry, backend.r1(values[1][1], sum_n1))
    update_entry(odd_ratio_d_e_entry, backend.odd_ratio_d_e(values[0][0], values[1][1], values[1][0], values[0][1]))
    update_entry(r_entry, backend.r(backend.m1(values[0][1], values[1][1]), total))

    update_label(hypothese_label, backend.test_hypothese_d_e(values[1][1], values[0][1], sum_n0, sum_n1, sum_m1, total))

    update_entry(nu_entry, backend.nu_d_e(values[0][0], values[1][1], values[1][0], values[0][1]))
    update_entry(var_nu_entry, backend.var_nu_d_e(values[0][0], values[0][1], values[1][0], values[1][1]))
    formatter_intervalle_confiance(intervalle_confiance_d_e_entry, backend.intervalle_confiance_d_e(values[0][0], values[1][1], values[1][0], values[0][1]))

    # Pour enquête CAS-Témoins
    update_entry(f0_entry, backend.f0(values[1][0], sum_m0))
    update_entry(f1_entry, backend.f1(values[1][1], sum_m1))
    update_entry(odd_ratio_e_d_entry, backend.odd_ratio_e_d(values[0][0], values[1][1], values[1][0], values[0][1]))
    update_entry(f_entry, backend.f(backend.n1(values[1][0], values[1][1]), total))

    update_label(hypothese_e_d_label, backend.test_hypothese_e_d(values[1][1], values[1][0], sum_m0, sum_m1, sum_n1, total))

    update_entry(nu_e_d_entry, backend.nu_e_d(values[0][0], values[1][1], values[1][0], values[0][1]))
    update_entry(var_nu_e_d_entry, backend.var_nu_e_d(values[0][0], values[0][1], values[1][0], values[1][1]))
    formatter_intervalle_confiance(intervalle_confiance_e_d_entry, backend.intervalle_confiance_e_d(values[0][0], values[1][1], values[1][0], values[0][1]))


    # Affichage des sommes des lignes et des colonnes dans les labels correspondants
    for i, sum_row in enumerate(sum_rows):
        label_row_sums[i]['text'] = f"{sum_row}"
    
    for j, sum_col in enumerate(sum_columns):
        label_col_sums[j]['text'] = f"{sum_col}"

    label_total['text'] = f"{total}"


def update_entry(entry_widget, value):
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, value)

def formatter_intervalle_confiance(entry_widget, value):
    formatted_value = "{:0<3} - {:0>3}".format(*map(lambda x: round(x, 2), value))
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, formatted_value)

def update_label(label_widget, text):
    label_widget.config(text=text)

root = tk.Tk()
root.title("Epidemiology Software")
root.geometry("1000x650")
root.resizable(False, True) # Redimensionnement de la fenêtre

entry_fields = []   # Les entrées du tableau

# Créer les étiquettes pour les colonnes
column_labels = ['D=0', 'D=1']
for j, col_label in enumerate(column_labels):
    label = tk.Label(root, text=col_label, font=font.Font(size=12))
    label.grid(row=1, column=j+2)

# Créer les étiquettes pour les lignes et les champs d'entrée pour le tableau 2x2
row_labels = ['E=0', 'E=1']
for i, row_label in enumerate(row_labels):
    label = tk.Label(root, text=row_label, font=font.Font(size=12))
    label.grid(row=i+2, column=1)

    row = []
    for j in range(2):
        entry = tk.Entry(root, font=font.Font(size=12))
        entry.grid(row=i+2, column=j+2)
        row.append(entry)
    entry_fields.append(row)

# Calcul des sommes
label_row_sums = [tk.Label(root, text='', font=font.Font(size=12), fg='blue') for _ in range(2)]
for i, label in enumerate(label_row_sums):
    label.grid(row=i+2, column=4)

label_col_sums = [tk.Label(root, text='', font=font.Font(size=12), fg='blue') for _ in range(2)]
for j, label in enumerate(label_col_sums):
    label.grid(row=4, column=j+2)

label_total = tk.Label(root, text='', fg='red', font=font.Font(size=12))
label_total.grid(row=4, column=4)

# Pour enquête de cohorte et transversale
# Bouton pour récupérer les valeurs
submit_button = tk.Button(root, text="Obtenir les valeurs", font=font.Font(size=12), bg='grey', border=3, relief=tk.GROOVE, command=get_values)
submit_button.grid(row=10, column=2)

study_label = tk.Label(root, text="Cas d'une étude cohorte ou transversale", font=font.Font(size=12, weight="bold"), fg='black')
study_label.grid(row=11, columnspan=2)

# R0
r0_label = tk.Label(root, text='R0', font=font.Font(size=12), fg='black')
r0_label.grid(row=12, columnspan=2)
r0_entry = tk.Entry(root, font=font.Font(size=12))
r0_entry.grid(row=13, columnspan=2)

# R1
r1_label = tk.Label(root, text='R1', font=font.Font(size=12), fg='black')
r1_label.grid(row=14, columnspan=2)
r1_entry = tk.Entry(root, font=font.Font(size=12))
r1_entry.grid(row=15, columnspan=2)

# OR D/E
odd_ratio_d_e_label = tk.Label(root, text="Odd Ratio D/E", font=font.Font(size=12), fg='black')
odd_ratio_d_e_label.grid(row=16, columnspan=2)
odd_ratio_d_e_entry = tk.Entry(root, font=font.Font(size=12))
odd_ratio_d_e_entry.grid(row=17, columnspan=2)

# R
r_label = tk.Label(root, text='R', font=font.Font(size=12), fg='black')
r_label.grid(row=18, columnspan=2)
r_entry = tk.Entry(root, font=font.Font(size=12))
r_entry.grid(row=19, columnspan=2)

# Vérification de l'indépendance
hypothese_label = tk.Label(root, text='Hypothèse :', font=font.Font(size=12), fg='black')
hypothese_label.grid(row=20, columnspan=2)
hypothese_entry = tk.Label(root, text=" ", font=font.Font(size=12), fg='black')
hypothese_entry.grid(row=21, columnspan=2)

nu_label = tk.Label(root, text='Nu', font=font.Font(size=12), fg='black')
nu_label.grid(row=22, columnspan=2)
nu_entry = tk.Entry(root, font=font.Font(size=12))
nu_entry.grid(row=23, columnspan=2)

var_nu_label = tk.Label(root, text='Var_Nu', font=font.Font(size=12), fg='black')
var_nu_label.grid(row=24, columnspan=2)
var_nu_entry = tk.Entry(root, font=font.Font(size=12))
var_nu_entry.grid(row=25, columnspan=2)

intervalle_confiance_d_e_label = tk.Label(root, text='Intervalle de confiance (IC)', font=font.Font(size=12), fg='black')
intervalle_confiance_d_e_label.grid(row=26, columnspan=2)
intervalle_confiance_d_e_entry = tk.Entry(root, font=font.Font(size=12))
intervalle_confiance_d_e_entry.grid(row=27, columnspan=2)

# Pour enquête CAS-Témoins

study_label_2 = tk.Label(root, text="Cas d'une étude CAS-Témoins", font=font.Font(size=12, weight="bold"), fg='black')
study_label_2.grid(row=11, column=10)

# F0
f0_label = tk.Label(root, text='F0', font=font.Font(size=12), fg='black')
f0_label.grid(row=12, column=10)
f0_entry = tk.Entry(root, font=font.Font(size=12))
f0_entry.grid(row=13, column=10)

# F1
f1_label = tk.Label(root, text='F1', font=font.Font(size=12), fg='black')
f1_label.grid(row=14, column=10)
f1_entry = tk.Entry(root, font=font.Font(size=12))
f1_entry.grid(row=15, column=10)

# OR E/D
odd_ratio_e_d_label = tk.Label(root, text="Odd Ratio E/D", font=font.Font(size=12), fg='black')
odd_ratio_e_d_label.grid(row=16, column=10)
odd_ratio_e_d_entry = tk.Entry(root, font=font.Font(size=12))
odd_ratio_e_d_entry.grid(row=17, column=10)

# F
f_label = tk.Label(root, text='F', font=font.Font(size=12), fg='black')
f_label.grid(row=18, column=10)
f_entry = tk.Entry(root, font=font.Font(size=12))
f_entry.grid(row=19, column=10)

# Vérification de l'indépendance
hypothese_e_d_label = tk.Label(root, text='Hypothèse :', font=font.Font(size=12), fg='black')
hypothese_e_d_label.grid(row=20, column=10)
hypothese_e_d_entry = tk.Label(root, text=" ", font=font.Font(size=12), fg='black')
hypothese_e_d_entry.grid(row=21, column=10)

nu_e_d_label = tk.Label(root, text='Nu', font=font.Font(size=12), fg='black')
nu_e_d_label.grid(row=22, column=10)
nu_e_d_entry = tk.Entry(root, font=font.Font(size=12))
nu_e_d_entry.grid(row=23, column=10)

var_nu_e_d_label = tk.Label(root, text='Var_Nu', font=font.Font(size=12), fg='black')
var_nu_e_d_label.grid(row=24, column=10)
var_nu_e_d_entry = tk.Entry(root, font=font.Font(size=12))
var_nu_e_d_entry.grid(row=25, column=10)

intervalle_confiance_e_d_label = tk.Label(root, text='Intervalle de confiance (IC)', font=font.Font(size=12), fg='black')
intervalle_confiance_e_d_label.grid(row=26, column=10)
intervalle_confiance_e_d_entry = tk.Entry(root, font=font.Font(size=12))
intervalle_confiance_e_d_entry.grid(row=27, column=10)


root.mainloop() # On démarre le programme
