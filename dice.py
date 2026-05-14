import random
import time

def dado(d):
	if d == 1:
		return "1"
	if d == 2:
		return "2"
	if d == 3:
		return "3"
	if d == 4:
		return "4"
	if d == 5:
		return "5"
	if d == 6:
		return "6"

def dadov(dv):
	if dv == 1:
		return "1"
	if dv == 2:
		return "2"
	if dv == 3:
		return "3"
	if dv == 4:
		return "4"
	if dv == 5:
		return "5"
	if dv == 6:
		return "6"

r = random.randint(1, 6)
girare = dado(r)

rv = random.randint(1, 6)
girarev = dadov(rv)

print ("Choose language / scegli lingua")
lingua = input ("ENG/ITA: ")

if lingua == "ITA":
    print ("Vuoi girare il dado e cercare di trovare 6?")
    print ("Scrivi gira per tirare il dado o stop per non farlo")
    giro = input("(gira/stop): ")
    if giro == "gira":
        time.sleep(0.5)
        print ("Hai trovato " + girare)
        if int(girare) != 6:
            time.sleep(0.5)
            print ("Vuoi provare un ultima volta?")
            rip = input("(si/no): ")
            if rip == "si":
                time.sleep(0.5)
                print ("Hai trovato " + girarev)
                if int(girarev) != 6:
	                time.sleep(0.5)
	                print ("Si vede che oggi la fortuna non è con te")
                else:
	                time.sleep(0.5)
	                print ("Che fortuna!")
            elif rip == "no":
                time.sleep(0.5)
                print ("Forse oggi non hai i tuoi calzini fortunati, alla prossima volta")
        else:
            time.sleep(0.5)
            print ("Che fortuna!") 
    else:
        time.sleep(0.5)
        print ("Torna quando vuoi!")	
        		    
if lingua == "ENG":
    print("Do you want to roll the die and try to get 6?")
    print("Type roll to roll the die or stop to not do it")
    giro = input("(roll/stop): ")
    if giro == "roll":
        time.sleep(0.5)
        print("You got " + girare)
        if int(girare) != 6:
            time.sleep(0.5)
            print("Do you want to try one last time?")
            rip = input("(yes/no): ")
            if rip == "yes":
                time.sleep(0.5)
                print("You got " + girarev)
                if int(girarev) != 6:
    	            time.sleep(0.5)
    	            print("It looks like luck is not on your side today")
                else:
    	            time.sleep(0.5)
    	            print("How lucky!")
            elif rip == "no":
                time.sleep(0.5)
                print("Maybe today you are not wearing your lucky socks, see you next time")
        else:
            time.sleep(0.5)
            print("How lucky!")
    else:
        time.sleep(0.5)
        print("Come back anytime!")
