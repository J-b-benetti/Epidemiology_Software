import tkinter as tk
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

     # Affichage des sommes des lignes et des colonnes dans les labels correspondants
    for i, sum_row in enumerate(sum_rows):
        label_row_sums[i]['text'] = f"{sum_row}"
    
    for j, sum_col in enumerate(sum_columns):
        label_col_sums[j]['text'] = f"{sum_col}"

    label_total['text'] = f"{total}"

root = tk.Tk()
root.title("Epidemiology Software")
root.geometry("500x300")

entry_fields = []

# Créer les étiquettes pour les colonnes
column_labels = ['D=0', 'D=1']
for j, col_label in enumerate(column_labels):
    label = tk.Label(root, text=col_label)
    label.grid(row=1, column=j+1)

# Créer les étiquettes pour les lignes et les champs d'entrée pour le tableau 2x2
row_labels = ['E=0', 'E=1']
for i, row_label in enumerate(row_labels):
    label = tk.Label(root, text=row_label)
    label.grid(row=i+2, column=0)

    row = []
    for j in range(2):
        entry = tk.Entry(root)
        entry.grid(row=i+2, column=j+1)
        row.append(entry)
    entry_fields.append(row)

# Bouton pour récupérer les valeurs
submit_button = tk.Button(root, text="Obtenir les valeurs", command=get_values)
submit_button.grid(row=10, columnspan=3)

label_row_sums = [tk.Label(root, text='') for _ in range(2)]
for i, label in enumerate(label_row_sums):
    label.grid(row=i+2, column=3)

label_col_sums = [tk.Label(root, text='') for _ in range(2)]
for j, label in enumerate(label_col_sums):
    label.grid(row=4, column=j+1)

label_total = tk.Label(root, text='')
label_total.grid(row=4, column=3)


root.mainloop()
