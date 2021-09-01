# El cuarteto de Ascombe
# El cuarteto de Anscombe llamado asi por F. J. Ascombe corresponde a cuatro conjuntos de datos que recurrentemente se utiliza 
# para explicar la ventajas de la visualización como herramienta exploratoria (Coromina, 2009)
# Los datos descritos en cada conjunto son distintos, pero con propiedades estadisticas iguales como: media aritmetica, varianza, 
# correlación, coeficiente de correlación y recta de regresión.


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
  a=np.array([[10.0, 8.04],[8.0, 6.95],[13.0, 7.58],[9.0, 8.81],[11.0, 8.833],[14.0, 9.96],[6.0, 7.24],[4.0, 4.26],[12.0, 10.84],[7.0, 4.82],[5.0, 5.68]])
  b=np.array([[10.0, 9.14],[8.0, 8.14],[13.0, 8.74],[9.0, 8.77],[11.0, 9.26],[14.0, 8.10],[6.0, 6.13],[4.0, 3.10],[12.0, 9.13],[7.0, 7.26],[5.0, 4.74]])
  c=np.array([[10.0, 7.46],[8.0, 6.77],[13.0, 12.74],[9.0, 7.11],[11.0, 7.81],[14.0, 8.84],[6.0, 6.08],[4.0, 5.39],[12.0, 8.15],[7.0, 6.42],[5.0, 5.73]])
  d=np.array([[8.0, 6.58],[8.0, 5.76],[8.0, 7.71],[8.0, 8.84],[8.0, 8.47],[8.0, 7.04],[8.0, 5.25],[19.0, 12.50],[8.0, 5.56],[8.0, 7.91],[8.0, 6.89]])
  #print (a)
dato1=input("Ingrese un numero para X: ")
dato2=input("Ingrese un numero para Y: ")
print (f"El numero para X es: {str(dato1)}")
print (f"El numero para Y es: {str(dato2)}")
bb=float(dato1)
cc=float(dato2)
matrizz=np.array([[bb, cc]])
#cuadrante=pd.DataFrame({"X":[10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0, b], "Y":[8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68, c]})
#print (cuadrante)
matrizc1=np.concatenate((a, matrizz), 0)
matrizc2=np.concatenate((b, matrizz), 0)
matrizc3=np.concatenate((c, matrizz), 0)
matrizc4=np.concatenate((d, matrizz), 0)
matrizb1=pd.DataFrame(matrizc1)
matrizb2=pd.DataFrame(matrizc2)
matrizb3=pd.DataFrame(matrizc3)
matrizb4=pd.DataFrame(matrizc4)
print(matrizb1)
media=matrizb1[0].mean()
media2=matrizb1[1].mean()
media3=matrizb2[0].mean()
media4=matrizb2[1].mean()
media5=matrizb3[0].mean()
media6=matrizb3[1].mean()
media7=matrizb4[0].mean()
media8=matrizb4[1].mean()
print ("La media de  X", media)
print ("La media de  y", media2)
print ("La media de  X", media3)
print ("La media de  y", media4)
print ("La media de  X", media5)
print ("La media de  y", media6)
print ("La media de  X", media7)
print ("La media de  y", media8)

x1=matrizb1[0].corr(matrizb1[1])
x2=matrizb2[0].corr(matrizb2[1])
x3=matrizb3[0].corr(matrizb3[1])
x4=matrizb4[0].corr(matrizb4[1])
print (x1)
print (x2)
print (x3)
print (x4)


# In[ ]:





# In[ ]:




