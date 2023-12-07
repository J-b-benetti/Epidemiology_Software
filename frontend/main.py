import tkinter as tk
from backend import calcul

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
    print("Valeurs saisies :", values)

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
submit_button.grid(row=4, columnspan=3)

root.mainloop()
