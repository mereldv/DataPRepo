# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 14:42:44 2020

@author: merel
"""
import numpy as np
import matplotlib.pyplot as plt
import math


V0 = 0.656 #Volt
t = np.linspace(0,8e-3) #seconde
R = 1.1578e3 #ohm
C = 151.8e-9 #Farad 
Vu = V0*(1-2*(math.e**(-t/(R*C))))  


t_2 = [0.955e-3,1.910e-3,2.865e-3,3.820e-3,4.775e-3,5.730e-3,6.685e-3,7.640e-3] #seconde
Vu_2 = [608e-3,648e-3,656e-3,656e-3,656e-3,656e-3,656e-3,656e-3] #Volt

plt.plot(t,Vu,label = "Berekende lijn")  
plt.plot(t_2,Vu_2, label = "Gemeten lijn")  
plt.xlabel("$t$ (s)", fontsize=15)
plt.ylabel("$Vu$ (V)", fontsize=15)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.legend(loc="lower right", fontsize=11)
plt.title("Berekend en Gemeten", fontsize=15)
plt.grid()
plt.show()


#Hulp berekeningen bij opdrachten
periodekeertien = (R*C)*10
frequentie = 1/periodekeertien #Periode omrekenen naar frequentie om in te stellen op toongenerator 
print(frequentie)
       
amplitude = 780.0
tussenstapjes = 780.0/8
print(tussenstapjes) #Het antwoord is 97.5, dus we nemen stapjes van 100 micros

