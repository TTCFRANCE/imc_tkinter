from tkinter import *

def open_imc():
    fenetre = Toplevel()
    fenetre.title("Calcul de l'IMC")


    def compute_IMC():
        global photo
        try:
            # Récupération des valeurs saisies par l'utilisateur
            poids = float(poids_entry.get())
            taille = float(taille_entry.get()) / 100  # Convertir la taille en mètres

            # Calcul de l'IMC
            imc = poids / (taille * taille)
            imc_label.config(text=f"IMC = {imc:.2f}")
        except ValueError:
            imc_label.config(text="Veuillez saisir des valeurs numériques.")


    # Libellé et champ de saisie pour le poids
    poids_label = Label(fenetre, text="Poids (kg):")
    poids_label.pack()
    poids_entry = Entry(fenetre)
    poids_entry.pack()

    # Libellé et champ de saisie pour la taille
    taille_label = Label(fenetre, text="Taille (cm):")
    taille_label.pack()
    taille_entry = Entry(fenetre)
    taille_entry.pack()


    calculer_button = Button(fenetre, text="Calculer", command=compute_IMC)
    calculer_button.pack()

    # Libellé pour afficher l'IMC
    imc_label = Label(fenetre, text="")
    imc_label.pack()
    Button(fenetre, image=photo).pack(side=TOP)

home = Tk()
btn_imc = Button(home, text="IMC",command=open_imc)
btn_imc.pack()
home.mainloop()