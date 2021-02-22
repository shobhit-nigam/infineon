# lists
# mutable remove data


lista = ['let', 'the', 'force', 'be', 'with', 'you']
listb = [4, 7, 9, 10, 23, 4, 8, 13]

lista.append("and me")
lista.insert(2, "major")
print(lista)


lista.pop()
print(lista)
lista.pop(3)
print(lista)
lista.remove("with")
print(lista)

# clear the list
lista.clear()
print(lista)
