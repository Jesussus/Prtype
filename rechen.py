# Der CMD Code :  python C:\PythonProjects\rechen.py
#Aufgaben: Aufgaben erstellen, die Aufgaben haben einen einfluss auf Variablen,
#der Wert der Variable (Score) wird ausgelesen und überschrieben.
import random

score = 0
def Aufagbe_1():
    while score < 5:
        Zahl1 = random.randint(30, 50)
        Zahl2 = random.randint(1, 40)
        Frage1 = input(f"Hier ist diene Aufgabe:\n {Zahl1} - {Zahl2}\n")
        print(Frage1)
        Antwort1 = Zahl1 - Zahl2
        Antwort1 = str(Antwort1)
        if Frage1 == Antwort1:
            print("Richtig!")
            score = score + 1
        else:
            print("Falsch!!!")
            score = score - 1
def Aufgabe_2():
    zahl1 = random.randint(0, 10)
    zahl2 = ramdom.randint(0, 10)

def Aufgabe_3():
    zahl1 = random.randint(0, 10)
    zahl2 = ramdom.randint(0, 10)
    Ergebnis = zahl1 * zahl2
    Ergebnisstr = str.Ergebnis
    Frage = input(f"Berechne {zahl1}x{zahl2}")
    if Frage == Ergebnistr:
        print("Diese Antwort war richtig")
        score = score+1
    else:
        print("Diese Antwort war falsch")
        score = score - 1