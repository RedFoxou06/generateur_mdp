from tkinter import Label, Entry, Tk, BooleanVar, Frame
from tkinter import Button
from tkinter import Checkbutton
import random

C_BG_APP = "#121212"
C_BG_CARD = "#1E1E1E"
C_ACCENT = "#BB86FC"
C_TEXT_MAIN = "#E0E0E0"
C_TEXT_SEC = "#A0A0A0"
C_INPUT_BG = "#2C2C2C"
C_ERROR = "#CF6679"
C_SUCCESS = "#03DAC6"

good = False
MINUSCULES = "abcdefghijklmnopqrstuvwxyz"
MAJUSCULES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHIFFRES = "0123456789"
SYMBOLES = "!@#$%^&*()_+=-|"

#------------------------fonction pour générer le mot de passe------------------------
def creation_mdp():
    global good
    length = champ_saisi.get()
    char_possible = MINUSCULES + MAJUSCULES

    #gestion erreur
    if length == "":
        good = False
        return affichage.config(text="Erreur: Longueur vide", fg=C_ERROR)

    #gestion erreur
    if not length.isdigit():
        good = False
        return affichage.config(text="Erreur: Pas un nombre", fg=C_ERROR)

    #ajout des nombres
    if var_nombre.get():
        char_possible += CHIFFRES

    #ajout des symboles
    if var_symbole.get():
        char_possible += SYMBOLES
    password = ""
    length = int(length)

    #gestion erreur
    if length <= 7:
        good = False
        return affichage.config(text="Min: 8 caractères", fg=C_ERROR)

    for i in range(length):
        password += random.choice(char_possible)
    good = True

    if len(password) <= 10:
        affichage.config(fg=C_ERROR)
    elif 10 < len(password) <= 14:
        affichage.config(fg="orange")
    elif len(password) > 14 and var_symbole.get():
        affichage.config(fg=C_SUCCESS)
    else:
        affichage.config(fg=C_SUCCESS)

    return affichage.config(text=password)

#------------------------fonction pour copier le mot de passe------------------------
def copie():
    #gestion erreur
    temp = affichage.cget("text")
    if temp == "" or "Erreur" in temp or "Min:" in temp:
        mdp.clipboard_clear()
        return affichage.config(text="Rien à copier !", fg=C_ERROR)

    #gestion erreur
    if not good:
        mdp.clipboard_clear()
        return affichage.config(text="Générez d'abord !", fg=C_ERROR)

    mdp.clipboard_clear()
    copy = affichage.cget("text")
    mdp.clipboard_append(copy)
    affichage.config(text="COPIÉ !", fg=C_ACCENT)


def on_enter(e):
    generer['bg'] = "#9965f4"


def on_leave(e):
    generer['bg'] = C_ACCENT


#------------------------squelette de base------------------------
#fenetre
mdp = Tk()
mdp.title("Password Generator")
#taille de la fenêtre
mdp.geometry("550x600")
mdp.config(bg=C_BG_APP)

container = Frame(mdp, bg=C_BG_APP)
container.pack(expand=True)

card = Frame(container, bg=C_BG_CARD, padx=40, pady=40)
card.pack()

Label(card, text="SÉCURITÉ", font=("Helvetica", 10, "bold"), fg=C_ACCENT, bg=C_BG_CARD).grid(row=0, column=0, columnspan=2)
Label(card, text="Générateur de mot de passe", font=("Helvetica", 18, "bold"), fg="white", bg=C_BG_CARD).grid(row=1, column=0, columnspan=2, pady=(0, 20))

#texte
Label(card, text="Longueur souhaitée", font=("Helvetica", 10), fg=C_TEXT_SEC, bg=C_BG_CARD).grid(row=2, column=0, sticky="w")

#input
champ_saisi = Entry(card, font=("Helvetica", 12), bg=C_INPUT_BG, fg="white", insertbackground="white", relief="flat", justify='center')
champ_saisi.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(5, 20), ipady=5)

#checkbutton pour ajouter des nombres
var_nombre = BooleanVar()
chk_nb = Checkbutton(card, text="Inclure des Chiffres (0-9)", variable=var_nombre,
                     bg=C_BG_CARD, fg=C_TEXT_MAIN, selectcolor=C_INPUT_BG, activebackground=C_BG_CARD,
                     activeforeground="white", font=("Helvetica", 10))
chk_nb.grid(row=4, column=0, columnspan=2, sticky="w", pady=2)

#checkbutton pour ajouter des caractères spéciaux
var_symbole = BooleanVar()
chk_sym = Checkbutton(card, text="Inclure des Symboles (!@#)", variable=var_symbole,
                      bg=C_BG_CARD, fg=C_TEXT_MAIN, selectcolor=C_INPUT_BG, activebackground=C_BG_CARD,
                      activeforeground="white", font=("Helvetica", 10))
chk_sym.grid(row=5, column=0, columnspan=2, sticky="w", pady=2)

#bouton pour générer
generer = Button(card, text="GÉNÉRER LE CODE", command=creation_mdp,
                 bg=C_ACCENT, fg="#000000", font=("Helvetica", 11, "bold"), relief="flat", cursor="hand2")
generer.grid(row=6, column=0, columnspan=2, sticky="ew", pady=(25, 15), ipady=10)

generer.bind("<Enter>", on_enter)
generer.bind("<Leave>", on_leave)

result_frame = Frame(card, bg=C_INPUT_BG, bd=0)
result_frame.grid(row=7, column=0, columnspan=2, sticky="ew", pady=10)

#affichage du mot de passe
affichage = Label(result_frame, text="...", font=("Courier New", 14, "bold"), fg=C_TEXT_SEC, bg=C_INPUT_BG, pady=15)
affichage.pack(fill="both")

frame_actions = Frame(card, bg=C_BG_CARD)
frame_actions.grid(row=8, column=0, columnspan=2, pady=(10, 0))

#bouton pour copier
btn_copy = Button(frame_actions, text="Copier", command=copie, bg=C_BG_CARD, fg=C_TEXT_MAIN, relief="flat",
                  font=("Helvetica", 10), activebackground=C_BG_CARD, cursor="hand2")
btn_copy.pack(side="left", padx=10)

Label(frame_actions, text="|", bg=C_BG_CARD, fg=C_TEXT_SEC).pack(side="left")

#bouton pour quitter
btn_quit = Button(frame_actions, text="Quitter", command=mdp.destroy, bg=C_BG_CARD, fg=C_ERROR, relief="flat",
                  font=("Helvetica", 10), activebackground=C_BG_CARD, cursor="hand2")
btn_quit.pack(side="left", padx=10)

mdp.mainloop()