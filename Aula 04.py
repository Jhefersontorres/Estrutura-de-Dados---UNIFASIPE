lista = []
lista.append("Jean")
print(lista)
lista.append("Vitor")
print(lista)
lista.append("Diego")
print(lista)
lista.append("jheferson")
print(lista)
lista.append("João")
print(lista)
lista.append("Anderson")
print(lista)
lista.append("Bruno")
print(lista)
lista.append("Dani")
print(lista)
lista.append("lucas")
print(lista)
#lista.pop() limpar lista do ultimo para o inicio utilizado em estrutura de dados pilha
#print(lista)
x = input("Digite o nome procurado: ")
i = 0
while i < len(lista):
    if x == lista[i]:
        print(i)
        break
    i += 1
print(lista)
lista.pop(i)
print(lista)