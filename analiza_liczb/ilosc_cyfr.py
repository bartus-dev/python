liczba = abs(int(input("Podaj liczbe calkowita: "))) # obsługa liczb ujemnych
licznik = 0

# zlicza ilość cyfr
while liczba > 0:
    cyfra = liczba % 10
    licznik += 1
    liczba //= 10

print(f"Podana liczba ma cyfr: {licznik}")
