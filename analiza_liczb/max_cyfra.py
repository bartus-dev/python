liczba = int(input("Podaj liczbę: "))
liczba = abs(liczba) # obsługa liczb ujemnych

max_cyfra = 0

# wyszukiwanie największej cyfry w liczbie
while liczba > 0:
    cyfra = liczba % 10
    if cyfra > max_cyfra:
        max_cyfra = cyfra

    liczba //= 10

print(f"Najwieksza cyfra: {max_cyfra} ")
