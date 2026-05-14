import random

def gen_segni(seg1):
    if seg1 == 1:
        return "!"
    elif seg1 == 2:
        return "$"
    elif seg1 == 3:
        return "&"
    elif seg1 == 4:
        return "%"
    elif seg1 == 5:
        return "?"

s = random.randint(1, 5)
segno = gen_segni(s)

def generatore_pass(parola1, parola2):
    num = random.randint(100, 900)
    risultato = parola1 + parola2 + segno + str(num)
    return risultato
    
    
print ("Benvenuto nel generatore password")
print ("Scegli due parole")

parola1 = input("Prima parola: ")
parola2 = input("Seconda parola: ")
password = generatore_pass(parola1, parola2)
print (password)

    
