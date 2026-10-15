import time

kategorie = input("Podaj w jakiej jednostce czasowej chcesz odliczyć czas? (sekundy, minuty, godziny)")

if kategorie == "sekundy":
    czas = int(input("Ile sekund mam odliczyć?"))
    czas_startowy = czas
    while czas > 0:
        print(f"Pozostało: {czas} sekund")
        time.sleep(1)
        czas -= 1
    else:
        print(f"Koniec czasu! Minęło {czas_startowy} sekund")

elif kategorie == "minuty":
    czas_minuty = int(input("Ile minut mam odliczyć?"))
    czas_sekundy = czas_minuty * 60
    czas_startowy = czas_sekundy
    while czas_sekundy > 0:
        minuty = czas_sekundy // 60
        sekundy = czas_sekundy % 60

        print(f"Pozostało: {minuty:02d}:{sekundy:02d} minut")
        time.sleep(1)
        czas_sekundy -= 1
    else:
        print(f"Koniec czasu! Minęło {czas_startowy // 60} minut")

elif kategorie == "godziny":
    czas_godziny = int(input("Ile godzin mam odliczyć?"))
    czas_sekundy = czas_godziny * 3600
    czas_startowy = czas_sekundy
    while czas_sekundy > 0:
        godziny = czas_sekundy // 3600
        reszta_z_godziny = czas_sekundy % 3600
        minuty = reszta_z_godziny // 60
        sekundy = reszta_z_godziny % 60

        print(f"Pozostało: {godziny:02d}:{minuty:02d}:{sekundy:02d} minut")
        time.sleep(1)
        czas_sekundy -= 1
    else:
        print(f"Koniec czasu! Minęło {czas_startowy // 3600} minut")
else:
    print("Błąd: Została źle wpisana jednostka czasowa! Spróbuj ponownie!")
