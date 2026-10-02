liczba1 = float(input("Podaj liczba: "))
operacja = input("Podaj operacja: +, -, *, /")
liczba2 = float(input("Podaj liczba: "))

if operacja == "+":
    wynik = liczba1 + liczba2
    print(f"Wynik: {wynik}")
elif operacja == "-":
    wynik = liczba1 - liczba2
    print(f"Wynik: {wynik}")
elif operacja == "*":
    wynik = liczba1 * liczba2
    print(f"Wynik: {wynik}")
elif operacja == "/":
    if liczba2 != 0:
        wynik = liczba1 / liczba2
        print(f"Wynik: {wynik}")
    else:
        print("Błąd: Nie można dzielić przez zero")
else:
    print("Błąd: Nie można wykonać operacji")
