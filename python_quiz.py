def nytt_spel():

    gissningar = []
    korrekta_gissningar = 0
    frågenummer = 1

    for key in frågor:
        print(key)
        for i in alternativ[frågenummer-1]:
            print(i)
        gissning = input("Skriv A, B, C eller D")
        gissning = gissning.upper()
        gissningar.append(gissning)

        korrekta_gissningar += kolla_svar(frågor.get(key),gissning)
        frågenummer += 1

    visa_resultat(korrekta_gissningar, gissningar)

def kolla_svar(svar, gissning):

    if svar == gissning:
        print("Rätt svar")
        return 1
    else:
        print("Fel svar")
        return 0


def visa_resultat(korrekta_gissningar, gissningar):
    print("Resultat")
    print("Svar: ", end="")
    for i in frågor:
        print(frågor.get(i), end=" ")
    print()
    print("Gissningar: ", end="")
    for i in gissningar:
        print(i, end=" ")
    print()

    poäng = int((korrekta_gissningar/len(frågor))*100)
    print("Dina poäng är: "+str(poäng)+"%")

def spela_igen():

    svara = input("Vill du spela igen?: (ja/nej): ")
    svara = svara.upper()

    if svara == "JA":
        return True
    else:
        return False

frågor = {
    "Vem skapade Python?: ": "A",
    "Vilket år skapades Python?: ": "B",
    "Vilket djur är Pythons logga?: ": "C",
    "Vilket programmeringsspråk är bäst?: ": "A"
}

alternativ = [["A. Guido", "B. Elon", "C. Jeff", "D. Petter"],
              ["A. 1990", "B. 1991", "C. 2004", "D. 2005"],
              ["A. Björn", "B. Ödla", "C. Orm", "Råtta"],
              ["A. Python", "B. Java", "C. PHP", "D. JavaScript"]]

nytt_spel()

while spela_igen():
    nytt_spel()

print("Tack för att du har spelat!")
