"""Escape-roomstudio - hoofdapplicatie (week 1: alleen catalogusmodus)."""

from py_compile import main
from rooms_data import bouw_catalogus
from spelsessie import Spelsessie


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


def speel_sessie(sessie):
    """Doorloop alle puzzels van een sessie tot deze is afgerond (FR-2 t/m FR-5)."""
    print(f"\nSpelsessie gestart voor team '{sessie.teamnaam}' "
          f"in room '{sessie.escape_room.get_naam()}'.")

    while not sessie.is_afgerond():
        puzzel = sessie.get_huidige_puzzel()
        nummer = sessie.huidige_puzzel_index + 1
        totaal = sessie.escape_room.get_aantal_puzzels()
        print("\n" + "=" * 45)
        print(f"Puzzel {nummer}/{totaal}: {puzzel.get_titel()}")
        print(f"Opdracht: {puzzel.opdracht}")
        print(f"Voortgang: {sessie.get_voortgang_procent()}% | "
              f"Huidige score: {sessie.score}")

        actie = input("Kies een actie - [a]ntwoord geven / [h]int vragen: ").strip().lower()

        if actie == "h":
            hint = sessie.vraag_hint()
            if hint is None:
                print(">> Geen ongebruikte hint meer beschikbaar voor deze puzzel.")
            else:
                print(f">> Hint: {hint}")
        elif actie == "a":
            antwoord = input("Jouw antwoord: ")
            if sessie.geef_antwoord(antwoord):
                print(">> Correct! Door naar de volgende puzzel.")
            else:
                print(">> Helaas, dat is niet juist. Probeer het opnieuw.")
        else:
            print(">> Ongeldige actie. Kies 'a' of 'h'.")

    print("\n" + "*" * 45)
    print("Escape room afgerond!")
    print(f"Team: {sessie.teamnaam}")
    print(f"Eindscore: {sessie.score}")
    print(f"Voortgang: {sessie.get_voortgang_procent()}%")
    print("*" * 45)


def speelmodus(rooms):
    """Kies een room en speel een testsessie (FR-2 t/m FR-5)."""
    print("\n=== ROOM SPELEN ===")
    toon_catalogus(rooms)
    room = kies_room(rooms)
    if room is None:
        return
    teamnaam = input("Voer jullie teamnaam in: ").strip() or "Naamloos team"
    sessie = Spelsessie(teamnaam, room)
    speel_sessie(sessie)


def toon_hoofdmenu():
    print("\n========== ESCAPE-ROOMSTUDIO ==========")
    print("1. Catalogus bekijken")
    print("2. Room spelen")
    print("3. Afsluiten")


def main():
    print("Welkom bij de Escape-roomstudio!")
    rooms = bouw_catalogus()
    while True:
        toon_hoofdmenu()
        keuze = input("Maak een keuze (1-3): ").strip()
        if keuze == "1":
            catalogusmodus(rooms)
        elif keuze == "2":
            speelmodus(rooms)
        elif keuze == "3":
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze. Kies 1, 2 of 3.")


if __name__ == "__main__":
    main()