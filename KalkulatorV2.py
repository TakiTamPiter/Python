liczba1 = input("Podaj liczba: ")
operacja = input("Podaj operacja: (+, -, *, /)")
liczba2 = input("Podaj liczba: ")

if liczba1.isdigit() and liczba2.isdigit() == True:
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
      print("Błąd: nie można dzielić przez zero")
  else:
    print("Błąd: Podałeś złą symbol operacji")
else:
  print("Błąd: Nie podałeś liczby")