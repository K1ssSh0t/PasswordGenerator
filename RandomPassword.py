import random



leterrs = ["a","A,","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"]
numbers =["0","1","2","3","4","5","6","7","8","9"]
characters =["!","#","$","%","&","'","(",")","*","+","-",".","/",":",";","<","=",">","?","@","[",",","~"]

i =0
password = "";

while i <4:
    l = int(random.randint(0,51))
    a = str(leterrs[l])
    n = int(random.randint(0,9))
    b = str(numbers[n])
    ca  = int(random.randint(0,22))
    c = str(characters[ca])

    password = password+a + b + c




    i+=1



palabra = ''.join(random.sample(password,len(password)))


print("Random Password of 12 Characters")

print(palabra)