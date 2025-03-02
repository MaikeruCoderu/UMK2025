def sortowanie_babelkowe(lista):
    n = len(lista)
    
    for i in range(n):
        # Flaga do sprawdzenia, czy była jakaś zamiana
        zamiana = False
        
        for j in range(0, n-i-1):
            # Porównujemy sąsiednie elementy
            if lista[j] > lista[j+1]:
                # Zamieniamy elementy miejscami
                lista[j], lista[j+1] = lista[j+1], lista[j]
                zamiana = True
        
        # Jeśli nie było żadnej zamiany, lista jest już posortowana
        if not zamiana:
            break
    
    return lista

# Wczytywanie listy od użytkownika
try:
    liczby = input("Podaj listę liczb oddzielonych spacjami: ")
    lista_uzytkownika = [int(x) for x in liczby.split()]
    print("Twoja lista przed sortowaniem:", lista_uzytkownika)
    posortowana_lista_uzytkownika = sortowanie_babelkowe(lista_uzytkownika)
    print("Twoja lista po sortowaniu:", posortowana_lista_uzytkownika)
except ValueError:
    print("Błąd: Proszę podać poprawne liczby całkowite.")