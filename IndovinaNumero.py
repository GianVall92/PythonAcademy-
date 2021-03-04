import random
NumeroRandom = random.randint(1, 1000)
flag = True 

while flag:
    risposta = int (input("Indovina il numero: "))
    if risposta == NumeroRandom:
        print ("Bravo")
    else:
       if (risposta > NumeroRandom):
           print ("Il numero è più piccolo")
       else:
           print ("Il numero è più grande")