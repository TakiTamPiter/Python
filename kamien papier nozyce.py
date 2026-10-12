import random

print(" Witaj w grze Kamień, Papier, Nożyce   ")
print()
print("   Zasady są następujące:   ")
print("- Wygrywa gracz który pierwszy zdobędzie 3 zwycięstwa")
print("- Papier pokonuje kamień")
print("- Kamień pokonuje nożyce")
print("- Nożyce pokonują papier")
print("- Jeżeli zapadnie twoja kolej używaj małych liter i bez polskich znaków")
print()
print("Miłej gry i powodzenia :)")
print()

punkty_gracza = 0
punkty_komputera = 0
opcje = ["kamien", "papier", "nozyce"]

while punkty_komputera < 3 and punkty_gracza < 3:
    print()
    decyzja_gracza = input("Wybierz swój ruch: (kamien, papier, nozyce)")
    decyzja_komputera = random.choice(opcje)
    if decyzja_gracza not in opcje:
        print("Nie ma takiej opcji! Spróbuj ponownie")
        continue
    if decyzja_gracza == decyzja_komputera:
        print(" -> Remis! <-")
        print()
        print(f"Twoja Decyzja -> {decyzja_gracza}, Decyzja komputera -> {decyzja_komputera}")
        print()
        print(f"Aktualna Liczba punktów Gracza: {punkty_gracza}, Aktualna Liczba punktów Komputera: {punkty_komputera}")
    elif (decyzja_gracza == "kamien" and decyzja_komputera == "nozyce") or \
            (decyzja_gracza == "nozyce" and decyzja_komputera == "papier") or \
            (decyzja_gracza == "papier" and decyzja_komputera == "kamien"):
        print("Tą runde wygrywasz ty!")
        print()
        print(f"Twoja Decyzja -> {decyzja_gracza}, Decyzja komputera -> {decyzja_komputera}")
        print()
        punkty_gracza += 1
        print(f"Aktualna Liczba punktów Gracza: {punkty_gracza}, Aktualna Liczba punktów Komputera: {punkty_komputera}")
    else:
        print("Tą runde niestety przegrywasz!")
        print()
        print(f"Twoja Decyzja -> {decyzja_gracza}, Decyzja komputera -> {decyzja_komputera}")
        print()
        punkty_komputera += 1
        print(f"Aktualna Liczba punktów Gracza: {punkty_gracza}, Aktualna Liczba punktów Komputera: {punkty_komputera}")
if punkty_gracza == 3:
    print()
    print("Gratulacje! Wygrałeś grę")
elif punkty_komputera == 3:
    print()
    print("Niestety, przegrałeś grę")
