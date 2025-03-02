def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Wczytujemy liczby od użytkownika
try:
    liczba1 = int(input("Podaj pierwszą liczbę naturalną: "))
    liczba2 = int(input("Podaj drugą liczbę naturalną: "))
    
    if liczba1 < 0 or liczba2 < 0:
        print("Liczby muszą być naturalne (nieujemne).")
    else:
        wynik = nwd(liczba1, liczba2)
        print(f"NWD({liczba1}, {liczba2}) = {wynik}")
except ValueError:
    print("To nie są poprawne liczby całkowite.")
