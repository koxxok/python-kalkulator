#Zmienne
suma = 0
dziala = True

while dziala:
        liczbaA = float(input("Podaj liczba: "))
        znak = input("Podaj znak: ")
        liczbaB = float(input("Podaj liczba: "))

        if znak == "+":
            suma = liczbaA + liczbaB
            print(suma)
        elif znak == "-":
            suma = liczbaA - liczbaB
            print(suma)
        elif znak == "*":
            suma = liczbaA * liczbaB
            print(suma)
        elif znak == "/" and liczbaB != 0:
            suma = liczbaA / liczbaB
            print(suma)
        elif znak == "/" and liczbaB == 0:
            print("nie dzielimy przez zero")
        else:
            print("Niepoprawne znak")


        print("czy chcesz kontynuwac? (t/n)")
        odpowiedz = input().lower()
        if odpowiedz == "n":
            dziala = False
