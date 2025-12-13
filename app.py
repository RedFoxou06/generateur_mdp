from tkinter import *
from tkinter import ttk
import random

#fonction pour générer le mot de passe :
length=int(input("Entrer la longueur du mot de passe : "))
def creation_mdp(length):
    char_possible="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-|"
    password=""
    for i in range(length):
        rand_index=random.randint(0, len(char_possible) - 1)
        password+=char_possible[rand_index]
    return password

print(creation_mdp(length))

mdp=Tk()
mdp.title("Générateur de mot de passe")
mdp.geometry("450x450")

mdp.mainloop()