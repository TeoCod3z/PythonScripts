import random

fallimenti = 0
limite_fallimenti = random.randint(3,6)

print ("Choose language / Scegli lingua")
lingua = input("ENG/ITA: ")

if lingua == "ITA":
    while True:
        print ("Quante kill hai fatto, pilota?")
        kills = input()
        if int(kills) <= 9:
            fallimenti += 1
            if fallimenti >= limite_fallimenti:
                print (f"Hai fallito per {fallimenti} volte. Sei stanco, stacca pure")
                break
            print ("Continua a giocare finchè hai fatto 10 kills")
            continue
        else:
            break
    if int(kills) >=20:
        print ("Non me lo aspettavo, sono molto fiero di te")
    elif int(kills) >= 10:
        print ("Bravo, ora se vuoi puoi spegnere il gioco")
    
if lingua == "ENG":
    while True:
        print("How many kills did you get, pilot?")
        kills = input()
        if int(kills) <= 9:
            fallimenti += 1
            if fallimenti >= limite_fallimenti:
                print(f"You have failed {fallimenti} times. You're tired, you can stop now")
                break
            print("Keep playing until you get 10 kills")
            continue
        else:
            break
    if int(kills) >= 20:
        print("I didn't expect that, I'm very proud of you")
    elif int(kills) >= 10:
        print("Well done, now you can turn off the game if you want")
