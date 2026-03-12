def max_cyfra(x):
    if x == 0: return 0
    max_c = 0
    x = abs(x) # obsługa liczb ujemnych
    while x > 0:
        cyfra = x % 10
        if max_c < cyfra:
            max_c = cyfra
        x //= 10
    return max_c

def suma_cyfr(x):
    suma = 0
    x = abs(x)
    while x > 0:
        suma += x % 10
        x //= 10
    return suma

def ilosc_cyfr(x):
    if x == 0: return 1
    ilosc = 0
    x = abs(x)
    while x > 0:
        ilosc += 1
        x //= 10
    return ilosc

def palindrom(x):
    if x < 0: return "NIE" # liczby ujemne nie są uznawane za palindromy
    oryginalna = x
    odwrocona = 0
    while x > 0:
        odwrocona = odwrocona * 10 + (x % 10)
        x //= 10
    return "TAK" if oryginalna == odwrocona else "NIE"

# Testowanie
liczba = int(input("Podaj liczbe calkowita: "))
print("=====================")
print("Max cyfra: ", max_cyfra(liczba))
print("Suma cyfr: ", suma_cyfr(liczba))
print("Ilosc cyfr: ", ilosc_cyfr(liczba))
print("Palindrom?: ", palindrom(liczba))
