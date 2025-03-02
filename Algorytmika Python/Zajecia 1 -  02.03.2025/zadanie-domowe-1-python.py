def czy_mozna_przedstawic(L, K):
    lewy = 0
    prawy = len(L) - 1
    
    while lewy <= prawy:
        suma = L[lewy] + L[prawy]
        if suma == K:
            return True
        elif suma < K:
            lewy += 1
        else:
            prawy -= 1
    
    return False

# Wczytanie danych od użytkownika
try:
    L = list(map(int, input("Podaj posortowaną niemalejąco listę liczb oddzielonych spacjami: ").split()))
    K = int(input("Podaj liczbę K: "))
    
    if czy_mozna_przedstawic(L, K):
        print(f"Liczbę {K} można przedstawić jako sumę liczb z listy.")
    else:
        print(f"Liczby {K} nie można przedstawić jako sumy liczb z listy.")
except ValueError:
    print("Błąd: Wprowadź poprawne dane.")