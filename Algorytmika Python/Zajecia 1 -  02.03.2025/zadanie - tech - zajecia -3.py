# Wczytujemy listę L od użytkownika
print("Wprowadź elementy listy L (oddzielone spacjami):")
L = input().split()

# Wypisujemy oryginalną listę
print("Oryginalna lista L:", L)

# Usuwamy łańcuchy znaków z listy L
L = [x for x in L if not isinstance(x, str) or x.isdigit()]

# Konwertujemy pozostałe elementy na liczby całkowite
L = [int(x) for x in L]

# Wypisujemy zmodyfikowaną listę
print("Lista L po usunięciu łańcuchów znaków:", L)