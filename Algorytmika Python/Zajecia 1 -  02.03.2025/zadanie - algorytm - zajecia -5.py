def podziel_liste(lista):
    suma_calkowita = sum(lista)
    cel = suma_calkowita // 2
    n = len(lista)
    
    dp = [[False] * (cel + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, cel + 1):
            if j >= lista[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-lista[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    
    lewa_suma = next(j for j in range(cel, -1, -1) if dp[n][j])
    
    lewa = []
    prawa = []
    i, j = n, lewa_suma
    while i > 0 and j > 0:
        if i > 0 and dp[i-1][j]:
            prawa.append(lista[i-1])
            i -= 1
        else:
            lewa.append(lista[i-1])
            j -= lista[i-1]
            i -= 1
    
    while i > 0:
        prawa.append(lista[i-1])
        i -= 1
    
    return lewa, prawa, abs(sum(lewa) - sum(prawa))

# Wczytywanie listy od użytkownika
try:
    input_lista = input("Podaj listę liczb oddzielonych spacjami: ")
    lista = [int(x) for x in input_lista.split()]
    
    if not lista:
        print("Lista jest pusta.")
    else:
        lewa, prawa, roznica = podziel_liste(lista)
        print(f"Lewa część: {lewa}")
        print(f"Prawa część: {prawa}")
        print(f"Różnica sum: {roznica}")
except ValueError:
    print("Błąd: Proszę podać poprawne liczby całkowite.")