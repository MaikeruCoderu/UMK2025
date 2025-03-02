# Wczytujemy listę L od użytkownika
print("Wprowadź elementy listy L (oddzielone spacjami):")
L = [int(x) for x in input().split()]

# Wypisujemy oryginalną listę
print("Oryginalna lista L:", L)

# Usuwamy liczby parzyste z listy L
L = [x for x in L if x % 2 != 0]

# Wypisujemy zmodyfikowaną listę
print("Lista L po usunięciu liczb parzystych:", L)