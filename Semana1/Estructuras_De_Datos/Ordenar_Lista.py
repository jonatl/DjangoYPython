lista=[1,5,3,7,5,23,5]

for i in range(len(lista)):
    mini=i
    for x in range(i,len(lista)):
        if lista[x]<lista[mini]:
            mini=x
        aux=lista[i]
        lista[i]=lista[mini]
        lista[mini]=aux
        print(lista)