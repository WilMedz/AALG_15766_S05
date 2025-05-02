def OrdenarInserción(Numeros):
    for actual in range (1,len(Numeros)):
        sig=actual
        while sig>0 and Numeros [sig-1]>Numeros[sig]:
            Numeros[sig],Numeros[sig-1]=Numeros[sig-1],Numeros[sig]


def MetodoBurbuja(Numeros):
    for i in range (len(Numeros)):
        for j in range (len(Numeros)-i-1):
            if Numeros[j]>Numeros [j+1]:
                temp=Numeros[j]
                Numeros[j]=Numeros[j+1]
                Numeros[j+1]=temp
                
Numeros = [7, 2, 9, 1, 3, 6]   
OrdenarInserción(Numeros)
print(Numeros) 

Numeros = [7, 2, 9, 1, 3, 6]   
MetodoBurbuja(Numeros)
print(Numeros) 