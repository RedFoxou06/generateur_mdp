from tkinter import Label, Entry, Tk
from tkinter import ttk
import random

#fonction pour générer le mot de passe :
def creation_mdp():
    length=champ_saisi.get()

    #gestion erreur
    if length=="":
        return affichage.config(text="Veuillez saisir une longueur !")

    #gestion erreur
    if not length.isdigit():
        return affichage.config(text="Veuillez saisir un nombre !")

    char_possible="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-|"
    password=""
    length=int(length)

    #gestion erreur
    if length<=7:
        return affichage.config(text="La longueur minimal est de 8 !")

    for i in range(length):
        password+=random.choice(char_possible)
    return affichage.config(text=password)

def copie():
    mdp.clipboard_clear()
    copy=affichage.cget("text")
    mdp.clipboard_append(copy)

#squelette de base :
mdp=Tk()
mdp.title("Générateur de mot de passe")
mdp.geometry("450x450")
Label(mdp, text="Longueur du mot de passe : ").pack()
champ_saisi=(Entry(mdp))
champ_saisi.pack()
generer=ttk.Button(mdp, text="Générer un mot de passe", command=creation_mdp)
generer.pack()
affichage=Label(mdp, text="")
affichage.pack()
copier=ttk.Button(mdp, text="Copier", command=copie)
copier.pack()
ttk.Button(mdp, text="Quitter", command=mdp.destroy).pack()
mdp.mainloop()