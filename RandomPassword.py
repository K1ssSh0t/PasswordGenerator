import random

array = ["a","A,","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z","0","1","2","3","4","5","6","7","8","9","!","#","$","%","&","'","(",")","*","+","-",".","/",":",";","<","=",">","?","@","[",",","~"]

length=int(input("Password Length: "))

i=0

password="";

while i<length:

    a=int(random.randint(0,82))
    b=str(array[a])

    password = password +b

    i+=1

palabra = ''.join(random.sample(password,len(password)))

print(f"Random Password of {length} Characters")

print(palabra)
