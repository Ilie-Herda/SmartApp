def aantal_dagen(inputFile):
    file = open(inputFile, "r")
    regels = file.readlines()
    file.close()

    aantalDagen = len(regels) - 1
    return aantalDagen

def auto_bereken(inputFile, outputFile):
    file = open(inputFile, "r")
    file.readline()
    regels = file.readlines()
    file.close()

    file = open(outputFile, "w")

    for regel in regels:
        gegevens = regel.strip().split()

        datum = gegevens[0]
        aantalPersonen = int(gegevens[1])
        tempSetpoint = float(gegevens[2])
        tempBuiten = float(gegevens[3])
        neerslag = float(gegevens[4])

        temperatuurVerschil = tempSetpoint - tempBuiten

        if temperatuurVerschil >= 20:
            cvKetel = 100
        elif temperatuurVerschil >= 10:
            cvKetel = 50
        else:
            cvKetel = 0

        ventilatie = aantalPersonen + 1

        if ventilatie > 4:
            ventilatie = 4

        if neerslag < 3:
            bewatering = True
        else:
            bewatering = False

        file.write(f"{datum};{cvKetel};{ventilatie};{bewatering}\n")

    file.close()

def overwrite_settings(outputFile):
    file = open(outputFile, "r")
    regels = file.readlines()
    file.close()

    datum = input("Voer de datum in (DD-MM-JJJJ): ")
    regelNummer = -1

    for i in range(len(regels)):
        gegevens = regels[i].strip().split(";")

        if gegevens[0] == datum:
            regelNummer = i
            break

    if regelNummer == -1:
        return -1

    print("1: CV ketel")
    print("2: Ventilatie")
    print("3: Bewatering")

    systeem = input("Kies een systeem: ")

    if systeem != "1" and systeem != "2" and systeem != "3":
        return -3

    waardeInput = input("Voer de nieuwe waarde in: ")

    try:
        waarde = int(waardeInput)
    except ValueError:
        return -3

    gegevens = regels[regelNummer].strip().split(";")

    if systeem == "1":
        if waarde < 0 or waarde > 100:
            return -3
        gegevens[1] = str(waarde)

    elif systeem == "2":
        if waarde < 0 or waarde > 4:
            return -3
        gegevens[2] = str(waarde)

    elif systeem == "3":
        if waarde != 0 and waarde != 1:
            return -3

        if waarde == 0:
            gegevens[3] = "False"
        else:
            gegevens[3] = "True"

    regels[regelNummer] = f"{gegevens[0]};{gegevens[1]};{gegevens[2]};{gegevens[3]}\n"

    file = open(outputFile, "w")
    file.writelines(regels)
    file.close()

    return 0

def smart_app_controller():
    inputFile = "input.txt"
    outputFile = "output.txt"

    while True:
        print("====== Smart App Controller ======")
        print("1: Aantal dagen weergeven")
        print("2: Automatisch actuatoren berekenen")
        print("3: Waarde overschrijven")
        print("4: Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            try:
                aantalDagen = aantal_dagen(inputFile)
                print(f"Aantal dagen: {aantalDagen}")
            except FileNotFoundError:
                print("Inputbestand niet gevonden.")

        elif keuze == "2":
            try:
                auto_bereken(inputFile, outputFile)
                print("Actuatoren berekend en opgeslagen.")
            except FileNotFoundError:
                print("Inputbestand niet gevonden.")
            except (ValueError, IndexError):
                print("Ongeldige gegevens in het inputbestand.")

        elif keuze == "3":
            try:
                resultaat = overwrite_settings(outputFile)

                if resultaat == 0:
                    print("Waarde succesvol aangepast.")
                elif resultaat == -1:
                    print("Datum niet gevonden.")
                elif resultaat == -3:
                    print("Ongeldig systeem of ongeldige waarde.")
            except FileNotFoundError:
                print("Outputbestand niet gevonden. Bereken eerst de actuatoren.")

        elif keuze == "4":
            print("Programma gestopt.")
            break

        else:
            print("Ongeldige keuze, probeer opnieuw.")

        print()
