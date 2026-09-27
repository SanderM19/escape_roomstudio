"""Escape-roomstudio - hoofdapplicatie (week 3: alle must-haves)."""

from py_compile import main
from rooms_data import bouw_catalogus
from spelsessie import Spelsessie
from speelloop import speel_sessie
from ontwerp import ontwerp_room
from score_resultaat import ScoreResultaat


def toon_catalogus(rooms):
    print("\n=== CATALOGUS ESCAPE ROOMS ===")
    for index, room in enumerate(rooms, start=1):
        print(f"{index}. {room.get_naam()} ({room.get_aantal_puzzels()} puzzels)")


def kies_room(rooms):
    keuze = input("Kies een room (nummer) of 'q' om terug te gaan: ").strip()
    if keuze.lower() == "q":
        return None
    if not keuze.isdigit() or not (1 <= int(keuze) <= len(rooms)):
        print("Escape room niet gevonden.")
        return None
    return rooms[int(keuze) - 1]


def toon_room_details(room):
    """Toon naam, thema, tijdslimiet en de puzzels in speelvolgorde (FR-1).

    Alleen veilige informatie: nooit de oplossing of de hintteksten.
    """
    print("\n" + "-" * 45)
    print(room)
    print("-" * 45)
    print("Puzzels (in speelvolgorde):")
    for index, puzzel in enumerate(room.get_puzzels(), start=1):
        print(f"\n{index}. {puzzel}")
    print("-" * 45)


def catalogusmodus(rooms):
    """Toon de catalogus en de veilige puzzeldetails van een gekozen room (FR-1)."""
    print("\n=== CATALOGUS BEKIJKEN ===")
    toon_catalogus(rooms)
    room = kies_room(rooms)
    if room is not None:
        toon_room_details(room)


def _rond_sessie_af(sessie, scorebord):
    """Sla resultaat op in het scorebord."""
    resultaat = ScoreResultaat(sessie.teamnaam, sessie.escape_room.get_naam(), sessie.score)
    scorebord.append(resultaat)
    print("Resultaat toegevoegd aan het scorebord.")


def speelmodus(rooms, scorebord):
    """Kies een room, speel de sessie en sla het resultaat op (FR-7)."""
    print("\n=== SPEELMODUS ===")
    toon_catalogus(rooms)
    room = kies_room(rooms)
    if room is None:
        return
    teamnaam = input("Voer jullie teamnaam in: ").strip() or "Naamloos team"
    sessie = Spelsessie(teamnaam, room)
    speel_sessie(sessie)
    _rond_sessie_af(sessie, scorebord)


def ontwerpmodus(rooms, scorebord):
    """Stel een room samen en bied optioneel een testsessie aan (FR-6)."""
    room = ontwerp_room()
    rooms.append(room)
    testen = input("Wil je de nieuwe room direct testen? (j/n): ").strip().lower()
    if testen == "j":
        teamnaam = input("Testteamnaam: ").strip() or "Testteam"
        sessie = Spelsessie(teamnaam, room)
        speel_sessie(sessie)
        _rond_sessie_af(sessie, scorebord)


def toon_scorebord(scorebord):
    """Toon resultaten aflopend op score; bij gelijke score teamnaam A-Z (FR-8)."""
    print("\n=== SCOREBORD ===")
    if not scorebord:
        print("Nog geen resultaten beschikbaar.")
        return
    gesorteerd = sorted(scorebord, key=lambda r: (-r.score, r.teamnaam.lower()))
    for plaats, resultaat in enumerate(gesorteerd, start=1):
        print(f"{plaats}. {resultaat}")


def toon_hoofdmenu():
    print("\n========== ESCAPE-ROOMSTUDIO ==========")
    print("1. Catalogus bekijken")
    print("2. Room ontwerpen")
    print("3. Room spelen")
    print("4. Scorebord tonen")
    print("5. Afsluiten")


def main():
    print("Welkom bij de Escape-roomstudio!")
    rooms = bouw_catalogus()
    scorebord = []
    while True:
        toon_hoofdmenu()
        keuze = input("Maak een keuze (1-5): ").strip()
        if keuze == "1":
            catalogusmodus(rooms)
        elif keuze == "2":
            ontwerpmodus(rooms, scorebord)
        elif keuze == "3":
            speelmodus(rooms, scorebord)
        elif keuze == "4":
            toon_scorebord(scorebord)
        elif keuze == "5":
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze. Kies 1, 2, 3, 4 of 5.")


if __name__ == "__main__":
    main()