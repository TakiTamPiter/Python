import time

print("Minutnik")

czas = int(input("Ile sekund ma być odliczonych? "))

while czas > 0:
    print(f"Zostało: {czas}")
    time.sleep(1)
    czas -= 1
if czas == 0:
    print(f"Koniec!")

