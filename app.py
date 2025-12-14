from tkinter import Label, Entry, Tk
from tkinter import ttk
import random

good=False

#fonction pour générer le mot de passe :
def creation_mdp():
    global good
    length=champ_saisi.get()

    #gestion erreur
    if length=="":
        good=False
        return affichage.config(text="Veuillez saisir une longueur !")

    #gestion erreur
    if not length.isdigit():
        good = False
        return affichage.config(text="Veuillez saisir un nombre !")

    char_possible="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-|"
    password=""
    length=int(length)

    #gestion erreur
    if length<=7:
        return affichage.config(text="La longueur minimal est de 8 !")

    for i in range(length):
        password+=random.choice(char_possible)
    good=True
    return affichage.config(text=password)

def copie():
    #gestion erreur
    temp=affichage.cget("text")
    if temp=="":
        mdp.clipboard_clear()
        return affichage.config(text="Générer un mot de passe en premier !")

    #gestion erreur
    if good==False:
        mdp.clipboard_clear()
        return affichage.config(text="Générer un mot de passe en premier !")

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