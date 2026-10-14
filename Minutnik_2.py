import time

print("Minutnik")
kategorie = input("W jakiej mierze czasowej mam odliczać? (sekundy, minuty, godziny)")

if kategorie == "sekundy":
    czas_sekudny = int(input("Ile sekund mam odliczyć?"))
    czas_startowy = czas_sekudny
    while czas_sekudny > 0:
        print(f"Pozostało {czas_sekudny} sekund")
        time.sleep(1)
        czas_sekudny -= 1
    else:
        print(f"Koniec! Minęło {czas_startowy} sekund")

if kategorie == "minuty":
    czas_minuty = int(input("Ile minut mam odliczyć?"))
    czas_minuty = czas_minuty * 60
    czas_startowy = czas_minuty
    while czas_minuty > 0:
        print(f"Pozostało {czas_minuty} sekund")
        time.sleep(1)
        czas_minuty -= 1
    else:
        print(f"Koniec! Minęło {czas_startowy} sekund")

if kategorie == "godziny":
    czas_godziny = int(input("Ile godzin mam odliczyć?"))
    czas_godziny = czas_godziny * 3600
    czas_startowy = czas_godziny
    while czas_godziny > 0:
        print(f"Pozostało {czas_godziny} sekund")
        time.sleep(1)
        czas_godziny -= 1
    else:
        print(f"Koniec! Minęło {czas_startowy} sekund")