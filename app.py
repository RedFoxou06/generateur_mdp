from tkinter import Label, Entry, Tk, BooleanVar
from tkinter import ttk
import random

good=False
MINUSCULES = "abcdefghijklmnopqrstuvwxyz"
MAJUSCULES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHIFFRES = "0123456789"
SYMBOLES = "!@#$%^&*()_+=-|"

#------------------------fonction pour générer le mot de passe------------------------
def creation_mdp():
    global good
    length=champ_saisi.get()

    char_possible=MINUSCULES+MAJUSCULES

    #gestion erreur
    if length=="":
        good=False
        return affichage.config(text="Veuillez saisir une longueur !", fg="black")

    #gestion erreur
    if not length.isdigit():
        good = False
        return affichage.config(text="Veuillez saisir un nombre !", fg="black")

    #ajout des nombres
    if var_nombre.get():
        char_possible+=CHIFFRES

    #ajout des symboles
    if var_symbole.get():
        char_possible+=SYMBOLES
    password=""
    length=int(length)

    #gestion erreur
    if length<=7:
        good=False
        return affichage.config(text="La longueur minimal est de 8 !", fg="black")

    for i in range(length):
        password+=random.choice(char_possible)
    good=True

    if len(password)<=10:
        affichage.config(fg="red")

    if 10 < len(password) <= 14:
        affichage.config(fg="orange")

    if len(password)>14 and var_symbole.get():
        affichage.config(fg="green")
    return affichage.config(text=password)

#------------------------fonction pour copier le mot de passe------------------------
def copie():
    #gestion erreur
    temp=affichage.cget("text")
    if temp=="":
        mdp.clipboard_clear()
        return affichage.config(text="Générer un mot de passe en premier !", fg="black")

    #gestion erreur
    if not good:
        mdp.clipboard_clear()
        return affichage.config(text="Générer un mot de passe en premier !", fg="black")

    mdp.clipboard_clear()
    copy=affichage.cget("text")
    return mdp.clipboard_append(copy)



#------------------------squelette de base------------------------
#fenetre
mdp=Tk()
mdp.title("Générateur de mot de passe")
#taille de la fenêtre
mdp.geometry("450x450")
#texte
Label(mdp, text="Longueur du mot de passe : ").grid(column=0, row=0)
#input
champ_saisi=(Entry(mdp))
champ_saisi.grid(column=1, row=0)
#bouton pour générer
generer=ttk.Button(mdp, text="Générer un mot de passe", command=creation_mdp)
generer.grid(columnspan=2, row=1)
#affichage du mot de passe
affichage=Label(mdp, text="", font="Courier")
affichage.grid(columnspan=2, row=2)
#bouton pour copier
copier=ttk.Button(mdp, text="Copier", command=copie)
copier.grid(columnspan=2, row=3)
#checkbutton pour ajouter des nombres
var_nombre=BooleanVar()
nombre=ttk.Checkbutton(mdp, text="Nombre", variable=var_nombre)
nombre.grid(column=0, row=4)
#checkbutton pour ajouter des caractères spéciaux
var_symbole=BooleanVar()
symbole=ttk.Checkbutton(mdp, text="Symbole", variable=var_symbole)
symbole.grid(column=1, row=4)
#bouton pour quitter
ttk.Button(mdp, text="Quitter", command=mdp.destroy).grid(columnspan=2, row=5)
mdp.mainloop()