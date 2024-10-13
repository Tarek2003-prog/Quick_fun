import random
import json
from datetime import datetime
# Functie om woorden te laden uit een tekstbestand
def laad_woorden(moeilijkheidsgraad):
    if moeilijkheidsgraad == "makkelijk":
        bestandsnaam = "makkelijk.txt"
    elif moeilijkheidsgraad == "gemiddeld":
        bestandsnaam = "gemiddeld.txt"
    else:
        bestandsnaam = "moeilijk.txt"

    with open(bestandsnaam, "r") as bestand:
        woorden = bestand.readlines()
    return [woord.strip() for woord in woorden]


# Functie om de gebruiker om een letter te laten raden
def vraag_om_raad(geraden_letters):
    while True:
        gok = input("Raad een letter: ").lower()
        if len(gok) == 1 and gok.isalpha():
            if gok not in geraden_letters:
                return gok
            else:
                print(f"Je hebt '{gok}' al geraden.")
        else:
            print("Ongeldige invoer. Voer een enkele letter in.")


# Functie om de huidige status van het woord te laten zien
def toon_woord(woord, geraden_letters):
    return " ".join([letter if letter in geraden_letters else "_" for letter in woord])


# Functie om de score op te slaan in een scorebestand
def sla_score_op(naam, woord, geraden, pogingen):
    score_data = {
        "naam": naam,
        "woord": woord,
        "geraden": geraden,
        "pogingen": pogingen,
        "datum": str(datetime.now())
    }
    with open("score.txt", "a") as score_bestand:
        score_bestand.write(json.dumps(score_data) + "\n")


# Hoofdfunctie van het spel
def speel_spel():
    naam = input("Wat is je naam? ")

    # Vraag moeilijkheidsgraad
    moeilijkheidsgraad = ""
    while moeilijkheidsgraad not in ["makkelijk", "gemiddeld", "moeilijk"]:
        moeilijkheidsgraad = input("Kies een moeilijkheidsgraad (makkelijk, gemiddeld, moeilijk): ").lower()

    # Kies een woord
    woorden = laad_woorden(moeilijkheidsgraad)
    woord = random.choice(woorden)

    # Initieer spelvariabelen
    geraden_letters = []
    resterende_pogingen = 7
    woord_geraden = False

    print(f"Welkom, {naam}! Je speelt galgje. Je hebt {resterende_pogingen} pogingen.")

    # Spel lus
    while resterende_pogingen > 0 and not woord_geraden:
        print(f"\nStatus van het woord: {toon_woord(woord, geraden_letters)}")
        print(f"Geraden letters: {', '.join(geraden_letters)}")
        print(f"Resterende pogingen: {resterende_pogingen}")

        gok = vraag_om_raad(geraden_letters)
        geraden_letters.append(gok)

        if gok in woord:
            print(f"Goed gedaan! De letter '{gok}' zit in het woord.")
        else:
            resterende_pogingen -= 1
            print(f"Helaas! De letter '{gok}' zit niet in het woord.")

        # Controleer of het woord geraden is
        if all(letter in geraden_letters for letter in woord):
            woord_geraden = True

    # Eindresultaat
    if woord_geraden:
        print(f"Gefeliciteerd, {naam}! Je hebt het woord '{woord}' geraden.")
    else:
        print(f"Helaas, {naam}. Je hebt verloren. Het woord was '{woord}'.")

    # Sla score op
    sla_score_op(naam, woord, woord_geraden, 7 - resterende_pogingen)


# Start het spel
if __name__ == "__main__":
    speel_spel()