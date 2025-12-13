from tkinter import *
from tkinter import ttk
import random

#fonction pour générer le mot de passe :
def creation_mdp():
    length=int(champ_saisi.get())
    char_possible="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-|"
    password=""
    for i in range(length):
        rand_index=random.randint(0, len(char_possible) - 1)
        password+=char_possible[rand_index]
    return affichage.config(text=password)

#squelette de base :
mdp=Tk()
mdp.title("Générateur de mot de passe")
mdp.geometry("450x450")
Label(mdp, text="Longueur du mot de passe : ").pack()
champ_saisi=(Entry(mdp))
champ_saisi.pack()
generer=ttk.Button(mdp, text="Générer un mot de passe", command=creation_mdp).pack()
affichage=Label(mdp, text="")
affichage.pack()
ttk.Button(mdp, text="Quitter", command=mdp.destroy).pack()
mdp.mainloop()