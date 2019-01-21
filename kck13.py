# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import aseegg as ag

dane=pd.read_csv(r"C:/Users/Moi/Desktop/KCK 13/sub-01_trial-05.csv", delimiter=',', engine='python', names=['wiersz', '01', '02', '03', '04', 'liczby'])

numbers=dane['liczby']
# mojeDane=dane['01']
# prob=200
# czas=len(mojeDane)/200
# t=np.linspace(0,czas,czas*200)
#
# pasmowozaporowy=ag.pasmowozaporowy(mojeDane, prob, 49, 51)
# przefiltrowany=ag.pasmowoprzepustowy(pasmowozaporowy, prob, 1, 50)

# plt.plot(t, mojeDane)
# plt.xlabel("Czas [s]")
# plt.ylabel("Amplituda [-]")
# plt.show()
#
# plt.plot(t, przefiltrowany)
# plt.xlabel("Czas [s]")
# plt.ylabel("Amplituda [-]")
# plt.show()
#
# plt.plot(t, numbers)
# plt.xlabel("Czas [s]")
# plt.ylabel("Liczby")
# plt.show()

for i in range(len(dane['01'])):
    if dane['01'][i]>0.7:
        print("Liczba",[i],":",dane['liczby'][i])
