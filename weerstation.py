def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius

def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - luchtvochtigheid / 100 * windsnelheid

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif gevoel >= 0 and gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif gevoel >= 0 and gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif gevoel >= 10 and gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"

def weerstation():
    totaalTemperatuur = 0
    aantalDagen = 0

    for dag in range(1, 8):
        while True:
            tempInput = input(f"Wat is op dag {dag} de temperatuur[C]: ")

            if tempInput.strip() == "":
                print("bye")
                return

            try:
                tempCelsius = float(tempInput)
                break
            except ValueError:
                print("Ongeldige temperatuur, probeer opnieuw.")

        while True:
            windInput = input(f"Wat is op dag {dag} de windsnelheid[m/s]: ")

            if windInput.strip() == "":
                print("bye")
                return

            try:
                windsnelheid = float(windInput)

                if windsnelheid >= 0:
                    break
                else:
                    print("Windsnelheid mag niet negatief zijn.")
            except ValueError:
                print("Ongeldige windsnelheid, probeer opnieuw.")

        while True:
            vochtInput = input(f"Wat is op dag {dag} de vochtigheid[%]: ")

            if vochtInput.strip() == "":
                print("bye")
                return

            try:
                luchtvochtigheid = int(vochtInput)

                if luchtvochtigheid >= 0 and luchtvochtigheid <= 100:
                    break
                else:
                    print("Vochtigheid moet tussen 0 en 100 liggen.")
            except ValueError:
                print("Ongeldige vochtigheid, probeer opnieuw.")

        totaalTemperatuur = totaalTemperatuur + tempCelsius
        aantalDagen = aantalDagen + 1

        gemiddeldeTemperatuur = totaalTemperatuur / aantalDagen
        tempFahrenheit = Fahrenheit(tempCelsius)

        print(f"Het is {tempCelsius}C ({tempFahrenheit}F)")
        print(weerrapport(tempCelsius, windsnelheid, luchtvochtigheid))
        print(f"Gem. temp tot nu toe is {gemiddeldeTemperatuur}")
        print("======================================")
