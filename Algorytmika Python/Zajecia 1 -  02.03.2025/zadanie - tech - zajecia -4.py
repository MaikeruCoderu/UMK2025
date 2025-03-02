# Wczytujemy listę L od użytkownika
print("Wprowadź elementy listy L (oddzielone spacjami):")
L = input().split()

# Konwertujemy elementy na liczby całkowite
L = [int(x) for x in L]

# Wypisujemy oryginalną listę
print("Oryginalna lista L:", L)

# Wczytujemy indeksy i oraz j
while True:
    try:
        i = int(input("Podaj indeks i: "))
        j = int(input("Podaj indeks j (j > i): "))
        if i < j and i >= 0 and j < len(L):
            break
        else:
            print("Niepoprawne indeksy. Upewnij się, że 0 <= i < j < długość listy.")
    except ValueError:
        print("Proszę podać liczby całkowite.")

# Odwracamy fragment listy od indeksu i do j
L[i:j+1] = L[i:j+1][::-1]

# Wypisujemy zmodyfikowaną listę
print("Lista L po odwróceniu fragmentu:", L)