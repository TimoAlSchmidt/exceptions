solliciteren = True
antwoord = True
geslacht = "Man"

class WeightError(Exception):
    pass

class HeightError(Exception):
    pass

class LengthError(Exception):
    pass

print("Wat is uw naam?")
naam = input()

print("Bent u een man? Y/N")
if(input() == "N"):
    geslacht = "Vrouw"

print("Hoe lang bent u? Graag gehele centimeters.")
lengte = int(input())
if(lengte < 150):
    solliciteren = False
if(lengte > 300):
    raise HeightError("Je bent te lang!!!!")

print("Hoe zwaar bent u? Graag gehele kilogrammen.")
gewicht = int(input())
if(gewicht < 90):
    solliciteren = False
if (gewicht > 400):
    raise WeightError("Je bent te zwaar!")


print("Heeft u praktijkervaring met dieren-dressuur? Y/N")
if(input() == "Y"):
    print("Hoeveel jaren ervaring heeft u gehad? Graag gehele nummers invullen.")
    if(int(input()) < 4):
        antwoord = False
print("Heeft u ervaring met jongleren? Y/N")
if(input() == "Y"):
    print("Hoeveel jaren ervaring heeft u met jongleren? Graag gehele nummers invullen.")
    if(int(input()) < 5 and not antwoord):
        antwoord = False
    else:
        antwoord = True
print("Heeft u ervaring met acrobatiek? Y/N")
if(input() == "Y"):
    print("Hoeveel jaren ervaring heeft u met acrobatiek? Graag gehele nummers invullen.")
    if(int(input()) < 3 and not antwoord):
        antwoord = False
    else:
        antwoord = True

if(not antwoord):
    solliciteren = False

print("Heeft u bezit van een MBO-4 diploma? Y/N")
if(input() == "N"):
    solliciteren = False

print("Heeft u bezit van een geldig vrachtwagen rijbewijs? Y/N")
if(input() == "N"):
    solliciteren = False

print("Heeft u bezit van een pizza bakkerij's diploma? Y/N")
input()

print("Heeft u bezit van een hoge hoed? Y/N")
if(input() == "N"):
    solliciteren = False

if(geslacht == "Man"):
    print("Hoe breed is uw snor? Graag gehele centimeters.")
    if(int(input()) < 10):
        solliciteren = False
else:
    print("Heeft u rood krulhaar? Y/N")
    if(input() == "N"):
        solliciteren = False
    else:
        print("Hoe lang is uw haar? Graag gehele centimeters.")
        lengte = int(input())
        if(lengte < 20):
            solliciteren = False
        if(lengte > 100):
            raise LengthError("Je haar is veelst te lang")

print("Heeft u zwarte kleding thuis? Y/N")
input()

print("Hoe snel kunt u rennen? Graag gehele kilometers per uur.")
input()

print("Heeft u een certificaat \"Overleven met gevaarlijk personeel\"? Y/N")
if(input() == "N"):
    solliciteren = False

print("Heeft u kinderen? Y/N")
input()

if(solliciteren):
    print("Beste "+naam+",\nProficiat! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV")
else:
    print("Helaas voldoet U niet aan onze strenge eisen, het spijt ons.")