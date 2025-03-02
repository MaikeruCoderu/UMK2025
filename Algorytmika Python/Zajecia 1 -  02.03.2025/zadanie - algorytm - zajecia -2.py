def czy_pierwsza(n):
    # Liczby mniejsze niż 2 nie są pierwsze
    if n < 2:
        return False
    
    # Sprawdzamy dzielniki do pierwiastka z n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Wczytujemy liczbę od użytkownika
try:
    liczba = int(input("Podaj liczbę całkowitą do sprawdzenia: "))
    
    if czy_pierwsza(liczba):
        print(f"{liczba} jest liczbą pierwszą.")
    else:
        print(f"{liczba} nie jest liczbą pierwszą.")
except ValueError:
    print("To nie jest poprawna liczba całkowita.")