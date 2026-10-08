import random


print("Witaj w grze Odgadnij liczbę.")
print("Liczba jest w przedziale od 1 do 100")
losowa_liczba = random.randint(1,100)
proby = 0


while True:
    liczba_gracza = input("Zaproponuj liczbę: ")
    if liczba_gracza.isdigit():
        proby += 1
        propozycja = int(liczba_gracza)
        if propozycja > losowa_liczba:
            print("Liczba jest za duża. Spróbuj ponownie")
        elif propozycja < losowa_liczba:
            print("Liczba jest za mała. Spróbuj ponownie")
        else:
            print(f"Gratulacje! Odgadłeś liczbę w {proby} próbach")
            print(f"Liczba do odgadnięcia to {losowa_liczba}")
            break
    else:
        print("Błąd: nie wpisałeś liczby")