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

mdp=Tk()
mdp.title("Générateur de mot de passe")
mdp.geometry("450x450")

mdp.mainloop()