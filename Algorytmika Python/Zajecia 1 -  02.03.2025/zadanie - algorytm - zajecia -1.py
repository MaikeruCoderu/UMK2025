def suma_cyfr(liczba):
    # Konwertujemy liczbę na wartość bezwzględną, aby obsłużyć liczby ujemne
    liczba = abs(liczba)
    
    suma = 0
    while liczba > 0:
        cyfra = liczba % 10  # Pobieramy ostatnią cyfrę
        suma += cyfra        # Dodajemy cyfrę do sumy
        liczba //= 10        # Usuwamy ostatnią cyfrę z liczby
    
    return suma

# Wczytujemy liczbę od użytkownika
try:
    liczba = int(input("Podaj liczbę całkowitą: "))
    wynik = suma_cyfr(liczba)
    print(f"Suma cyfr liczby {liczba} wynosi: {wynik}")
except ValueError:
    print("To nie jest poprawna liczba całkowita.")