import time
import random 

print ("Choose language / Scegli lingua")
lingua = input("ENG/ITA: ")

if lingua == "ITA":
    def fallimento(fal):
        if fal == 1:
            return "Attacco iniziato con successo."
        if fal == 2:
            return "Attacco iniziato con successo."
        if fal == 3:
            return "Attacco fallitto."
    r = random.randint(1, 3)
    falli = fallimento(r)        
    print ("Benvenuto su DDoS Launcher.")
    print ("Su quale sito web vuoi lanciare un attacco?")
    sitoweb = input("URL: ")
    time.sleep(1)
    print ("Sicuro di voler lanciare un attacco sul sito " + sitoweb + "?")
    conferma = input("(S/n) " )
    if conferma == "S":
        nBot = input("Numero di bot da utilizzare: ")
        print ("Avvio di " + nBot + " bot")
        print ("..."*3)
        time.sleep(1)
        for i in range(int(nBot)):
            print (f"BOT_{i} -> INVIANDO PACCHETTO 64KB A " + sitoweb + " [STATUS: 200 OK]")
            time.sleep(0.1)
        print ("..."*3)
        time.sleep(3)
        print (falli)
    else:
        print ("Attacco cancellato.")

if lingua == "ENG":
    def failuer(fail):
            if fail == 1:
                return "Attack started succesfully."
            if fail == 2:
                return "Attack started succesfully."
            if fail == 3:
                return "Attack failed."
    ri = random.randint(1, 3)
    falils = failuer(ri)
    print("Welcome to DDoS Launcher.")
    print("Which website do you want to attack?")
    sitoweb = input("URL: ")
    time.sleep(1)
    print("Are you sure you want to launch an attack on " + sitoweb + "?")
    conferma = input("(Y/n) ")
    if conferma == "Y" or conferma == "y":
        nBot = input("Number of bots to use: ")
        print("Launching " + nBot + " bots")
        print("..." * 3)
        time.sleep(1)
        for i in range(int(nBot)):
            print(f"BOT_{i} -> SENDING 64KB PACKET TO " + sitoweb + " [STATUS: 200 OK]")
            time.sleep(0.1)             
        print("..." * 3)
        time.sleep(3)
        print(falils)
    else:
        print("Attack cancelled.")
            
