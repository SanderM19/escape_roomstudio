"""Escape-roomstudio - hoofdapplicatie (week 1: alleen catalogusmodus)."""

from rooms_data import bouw_catalogus

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