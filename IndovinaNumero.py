import random
NumeroRandom = random.randint(1, 1000)
flag = True 

while flag:
    risposta = int (input("Indovina il numero: "))
    if risposta == NumeroRandom: #Condizione di numero indovinato
        print ("Bravo")
    else: #Nel caso in cui sia sbagliato o è più piccolo o più grande
       if (risposta > NumeroRandom):
           print ("Il numero è più piccolo")
       else:
           print ("Il numero è più grande")