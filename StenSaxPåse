 import random

while True:
    val = ["sten","sax","påse"]

    dator = random.choice(val)
    spelare = None

    while spelare not in val:
        spelare = input("Sten, Sax eller Påse?: ").lower()

    if spelare == dator:
        print("Dator: ", dator)
        print("Spelare: ", spelare)
        print("Lika")
    elif spelare == "sten":
        if dator == "påse":
            print("Dator: ", dator)
            print("Spelare: ", spelare)
            print("Förlust")
        if dator == "sax":
            print("Dator: ", dator)
            print("Spelare: ", spelare)
            print("Vinst")
    elif spelare == "sax":
        if dator == "sten":
            print("Dator: ", dator)
            print("Spelare: ", spelare)
            print("Förlust")
        if dator == "påse":
            print("Dator: ", dator)
            print("Spelare: ", spelare)
            print("Vinst")
    elif spelare == "påse":
        if dator == "sten":
            print("Dator: ", dator)
            print("Spelare: ", spelare)
            print("Vinst")
        if dator == "sax":
            print("Dator: ", dator)
            print("Spelare: ", spelare)
            print("Förlust")
    spela_igen = input("Spela igen? (ja/nej)").lower()

    if spela_igen != "ja":
        break
print("Hejdå!")
