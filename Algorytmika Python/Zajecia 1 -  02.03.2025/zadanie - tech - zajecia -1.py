# Wczytujemy listę L1 od użytkownika
print("Wprowadź elementy listy L1 (oddzielone spacjami):")
L1 = [int(x) for x in input().split()]

# Generujemy listę L2
L2 = [2*x + 1 for x in L1 if x > 0]

# Wypisujemy listę L2
print("Lista L2:")
print(L2)