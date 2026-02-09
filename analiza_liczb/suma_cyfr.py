liczba = int(input("Podaj liczbe calkowita: "))
cyfra = 0
suma = 0

#zliczanie cyfr liczby
while liczba > 0:
    cyfra = liczba % 10
    suma += cyfra
    liczba //= 10

print(f"Suma cyfr w tej liczbie to: {suma}")
