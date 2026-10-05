plansza = [1, 2, 3, 4, 5, 6, 7, 8, 9] #0-8
aktualny_gracz = "X"
ruchy = 0

def wyswietl_plansze():
    print()
    print(f" {plansza[0]} | {plansza[1]} | {plansza[2]}")
    print()
    print(f" {plansza[3]} | {plansza[4]} | {plansza[5]}")
    print()
    print(f" {plansza[6]} | {plansza[7]} | {plansza[8]}")

def sprawdz_wygrana():
    warunki_wygranej = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for warunek in warunki_wygranej:
        if((plansza[warunek[0]] == plansza[warunek[1]] == plansza[warunek[2]])):
            return True
    return False

while ruchy < 9:
    wyswietl_plansze()
    print(f"Ruch gracza {aktualny_gracz}")
    wybor = input("Podaj numer pola:")
    if wybor.isdigit():
        numer_pola = int(wybor) - 1
        if 0 <= numer_pola <= 8 and plansza[numer_pola] not in ["X", "O"]:
            plansza[numer_pola] = aktualny_gracz
            ruchy += 1
            if sprawdz_wygrana():
                wyswietl_plansze()
                print(f"Wygrywa {aktualny_gracz}")
                break
            if aktualny_gracz == "X":
                aktualny_gracz = "O"
            else:
                aktualny_gracz = "X"
        else:
            print("To pole jest zajęte lub wybrałeś zły numer")
    else:
        print("To nie jest poprawna cyfra")
if ruchy == 9 and not sprawdz_wygrana():
    wyswietl_plansze()
    print("Remis")