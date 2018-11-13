import random
lista=[]
siedem=0
for i in range(100):
    los=random.randint(0,10)
    lista.append(los)
    while los==7:
        siedem+=1
print(lista)
print(siedem)
