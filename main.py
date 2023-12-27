import tkinter as tk
from tkinter import ttk

# Listes des débits et des crédits
debits = []
credits = []

# Solde initial
solde = 0

# Déclaration de label_solde en tant que variable globale
label_solde = None

# Ajoute une opération à la liste correspondante
def ajouter_operation(operation, date, libelle, montant):
    global solde, label_solde  # Utiliser la variable globale solde et label_solde
    if operation == "débit":
        debits.append((operation, date, libelle, float(montant)))  # Ajouter l'opération à debits
    elif operation == "crédit":
        credits.append((operation, date, libelle, float(montant)))  # Ajouter l'opération à credits
    # Calcule le solde actuel
    solde = solde + sum(item[3] for item in debits) - sum(item[3] for item in credits)

    # Met à jour l'affichage du solde
    label_solde.config(text="Solde : {}".format(solde))

# Affiche l'historique des opérations
def afficher_historique():
    # Crée une fenêtre temporaire
    fenetre_historique = tk.Toplevel()
    fenetre_historique.title("Historique des opérations")

    # Crée un tableau pour afficher les opérations
    table = ttk.Treeview(fenetre_historique, columns=("Type", "Date", "Libellé", "Montant"))
    table.heading("#0", text="Type")
    table.heading("Date", text="Date")
    table.heading("Libellé", text="Libellé")
    table.heading("Montant", text="Montant")

    # Ajoute les opérations au tableau
    for operation in debits + credits:
        table.insert("", "end", values=(operation[0], operation[1], operation[2], operation[3]))

    # Centre le tableau
    table.pack(expand=True, fill="both")

# Lance l'application
def lancer_application():
    global label_solde  # Utiliser la variable globale label_solde

    # Crée la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Suivi de compte bancaire")

    # Crée les widgets
    label_type = ttk.Label(fenetre, text="Type")
    entry_type = ttk.Entry(fenetre)
    label_date = ttk.Label(fenetre, text="Date")
    entry_date = ttk.Entry(fenetre)
    label_libelle = ttk.Label(fenetre, text="Libellé")
    entry_libelle = ttk.Entry(fenetre)
    label_montant = ttk.Label(fenetre, text="Montant")
    entry_montant = ttk.Entry(fenetre)

    # # Définir label_solde en tant que variable globale
    # global label_solde
    label_solde = ttk.Label(fenetre, text="Solde : {}".format(solde))

    button_ajouter = ttk.Button(fenetre, text="Ajouter", command=lambda: ajouter_operation(entry_type.get(), entry_date.get(), entry_libelle.get(), entry_montant.get()))
    button_historique = ttk.Button(fenetre, text="Historique", command=afficher_historique)

    # Positionne les widgets
    label_type.grid(row=0, column=0)
    entry_type.grid(row=0, column=1)
    label_date.grid(row=1, column=0)
    entry_date.grid(row=1, column=1)
    label_libelle.grid(row=2, column=0)
    entry_libelle.grid(row=2, column=1)
    label_montant.grid(row=3, column=0)
    entry_montant.grid(row=3, column=1)
    button_ajouter.grid(row=4, column=0)
    button_historique.grid(row=4, column=1)
    label_solde.grid(row=5, column=0, columnspan=2)

    # Démarre l'application
    fenetre.mainloop()

if __name__ == "__main__":
    lancer_application()
