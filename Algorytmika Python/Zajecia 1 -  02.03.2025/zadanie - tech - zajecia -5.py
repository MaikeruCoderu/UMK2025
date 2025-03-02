# Wczytaj listę L, a następnie sprawdź, czy jest ona palindromem.
# Wczytujemy listę L od użytkownika
print("Wprowadź elementy listy L (oddzielone spacjami):")
L = input().split()

# Konwertujemy elementy na liczby całkowite
L = [int(x) for x in L]

# Funkcja sprawdzająca, czy lista jest palindromem
def czy_palindrom(lista):
    return lista == lista[::-1]

# Sprawdzamy, czy lista L jest palindromem
if czy_palindrom(L):
    print("Lista L jest palindromem.")
else:
    print("Lista L nie jest palindromem.")

# Wypisujemy listę dla porównania
print("Lista L:", L)