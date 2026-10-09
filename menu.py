from weerstation import weerstation
from smartAppController import smart_app_controller
from openMeteo import actueelWeer

def menu():
    while True:
        print("====== Smart App ======")
        print("1: Weerstation")
        print("2: Smart App Controller")
        print("3: Actuele weersinformatie")
        print("4: Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            weerstation()

        elif keuze == "2":
            smart_app_controller()

        elif keuze == "3":
            actueelWeer()

        elif keuze == "4":
            print("Programma gestopt.")
            break

        else:
            print("Ongeldige keuze, probeer opnieuw.")

        print()

menu()
