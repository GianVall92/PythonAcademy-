def isTriangle (a,b,c):

 a = int(input("Inserisci il primo lato"))
 b = int(input("Inserisci il secondo lato"))
 c = int(input("Inserisci il terzo lato"))

 if ((a<b+c)and(b<a+c)and(c<a+b)): #Condizione per essere un triangolo
     print ("È un triangolo")
 elif((a=b+c)or(b=a+c)or(c=a+b)):
     print ("È un triangolo degenere") #caso limite
 else:
     print ("Non è un triangolo")