import tkinter as tk
from tkinter import font
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
    #print("Valeurs saisies :", values)

    sum_rows = [sum(row) for row in values]
    sum_columns = [sum(col) for col in zip(*values)]  # Utilisation de zip pour obtenir les colonnes

    # Calcul des sommes selon les méthodes définies dans le module backend
    sum_n0 = backend.n0(*values[0])
    sum_n1 = backend.n1(*values[1])
    sum_m0 = backend.m0(values[0][0], values[1][0])
    sum_m1 = backend.m1(values[0][1], values[1][1])
    total = backend.total(sum_n0, sum_n1)

    r0_value = backend.r0(values[0][1], sum_n0)
    r0_entry.delete(0, tk.END)
    r0_entry.insert(0, r0_value)

    r1_value = backend.r1(values[1][1], sum_n1)
    r1_entry.delete(0, tk.END)
    r1_entry.insert(0, r1_value)

    odd_ratio_d_e_value = backend.odd_ratio_d_e(values[0][0], values[1][1], values[1][0], values[0][1])
    odd_ratio_d_e_entry.delete(0, tk.END)
    odd_ratio_d_e_entry.insert(0, odd_ratio_d_e_value)

    r_value = backend.r(sum_m1, total)
    r_entry.delete(0, tk.END)
    r_entry.insert(0, r_value)

    var_r1_r0_value = backend.var_r1_r0(r_value, sum_n0, sum_n1)
    test_hyp_value = backend.test_hypothese_d_e(r0_value, r1_value, var_r1_r0_value)

    hypothese_label['text'] = f"{test_hyp_value}"

    # Affichage des sommes des lignes et des colonnes dans les labels correspondants
    for i, sum_row in enumerate(sum_rows):
        label_row_sums[i]['text'] = f"{sum_row}"
    
    for j, sum_col in enumerate(sum_columns):
        label_col_sums[j]['text'] = f"{sum_col}"

    label_total['text'] = f"{total}"



root = tk.Tk()
root.title("Epidemiology Software")
root.geometry("800x600")
root.resizable(False, True) #Redimensionnement de la fenêtre
#root.eval('tk::PlaceWindow . center')

entry_fields = []

# Créer les étiquettes pour les colonnes
column_labels = ['D=0', 'D=1']
for j, col_label in enumerate(column_labels):
    label = tk.Label(root, text=col_label, font=font.Font(size=12))
    label.grid(row=1, column=j+1)

# Créer les étiquettes pour les lignes et les champs d'entrée pour le tableau 2x2
row_labels = ['E=0', 'E=1']
for i, row_label in enumerate(row_labels):
    label = tk.Label(root, text=row_label, font=font.Font(size=12))
    label.grid(row=i+2, column=0)

    row = []
    for j in range(2):
        entry = tk.Entry(root, font=font.Font(size=12))
        entry.grid(row=i+2, column=j+1)
        row.append(entry)
    entry_fields.append(row)

# Calcul des sommes
label_row_sums = [tk.Label(root, text='', font=font.Font(size=12), fg='blue') for _ in range(2)]
for i, label in enumerate(label_row_sums):
    label.grid(row=i+2, column=3)

label_col_sums = [tk.Label(root, text='', font=font.Font(size=12), fg='blue') for _ in range(2)]
for j, label in enumerate(label_col_sums):
    label.grid(row=4, column=j+1)

label_total = tk.Label(root, text='', fg='red', font=font.Font(size=12))
label_total.grid(row=4, column=3)


# Bouton pour récupérer les valeurs
submit_button = tk.Button(root, text="Obtenir les valeurs", font=font.Font(size=12), bg='grey', border=3, relief=tk.GROOVE, command=get_values)
submit_button.grid(row=10, columnspan=4)

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

odd_ratio_d_e_label = tk.Label(root, text="Odd Ratio D/E", font=font.Font(size=12), fg='black')
odd_ratio_d_e_label.grid(row=16, columnspan=2)
odd_ratio_d_e_entry = tk.Entry(root, font=font.Font(size=12))
odd_ratio_d_e_entry.grid(row=17, columnspan=2)

r_label = tk.Label(root, text='R', font=font.Font(size=12), fg='black')
r_label.grid(row=18, columnspan=2)
r_entry = tk.Entry(root, font=font.Font(size=12))
r_entry.grid(row=19, columnspan=2)

hypothese_label = tk.Label(root, text='', font=font.Font(size=12), fg='black')
hypothese_label.grid(row=20, columnspan=2)


root.mainloop() # On démarre le programme
