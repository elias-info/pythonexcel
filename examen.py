import pandas as pd
import numpy as np
import re
ruta_extrada='Ingresar Ruta' #Ingresar ruta de ingreso del excel
base= pd.read_excel(ruta_extrada)
basef=pd.DataFrame(data=base)
matriz_s=basef.shape
#print(matriz_s)
planilla=[ 
        'username','password','firstname','lastname','email','course1','role1','institution','profile_field_RUT']
archivo_final="exportado.csv"
palabra_filtro="Urgencias"

filas=0
columnas=0
a=0
for i in matriz_s:
    if(a==0):
        filas=int(i)
        a+=1
    else:
        columnas=int(i)


matriz=[]
for i in range(filas):
    matriz.append([0]*9)


arr=np.array(base)
print(arr[0][4])

def verificador(list):
    if len(list) == 0:
        return True
    return False

for i in range(0,filas):
    busqueda=re.findall(palabra_filtro, arr[i][columnas-1])
    if verificador(busqueda)==0:
        if (isinstance(arr[i][4], int )) == 1:
            matriz[i][0]=arr[i][4]
        else:
            matriz[i][0]=str(arr[i][4])

        

    #for j in range(0,columnas):
        #print(arr[i][j])

print (isinstance(arr[0][4], int ))
busqueda=re.findall(palabra_filtro, arr[3][10])

#print(busqueda)
csv=open(archivo_final, "w")

print(matriz)
matriz=pd.DataFrame(data=matriz)
matriz.to_csv('prueba.csv', sep=' ', header=False, float_format='%.2f', index=False)