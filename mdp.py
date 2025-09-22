import random

def generate_password():
    length = 12  #à modifier selons les besoins
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()[]éèàùËêë"  #tous les caractères possibles
    password = ""
    for i in range(length):
        random_index = random.randint(0, len(charset) - 1)
        password += charset[random_index]
    return password

print(generate_password())