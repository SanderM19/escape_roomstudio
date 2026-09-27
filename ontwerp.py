"""Ontwerpmodus: een room met puzzels en hints samenstellen en valideren"""

from hint import Hint
from puzzel import Puzzel
from escape_room import EscapeRoom


def _vraag_positief_geheel(prompt):
    while True:
        waarde = input(prompt).strip()
        if waarde.isdigit() and int(waarde) >= 1:
            return int(waarde)
        print("Foutmelding: voer een positief geheel getal in (>= 1).")


def _vraag_niet_leeg(prompt):
    while True:
        waarde = input(prompt).strip()
        if waarde:
            return waarde
        print("Foutmelding: dit veld mag niet leeg zijn.")


def _ontwerp_hints(max_punten):
    hints = []
    while True:
        nog = input("Nog een hint toevoegen? (j/n): ").strip().lower()
        if nog != "j":
            break
        tekst = _vraag_niet_leeg("Hinttekst: ")
        while True:
            straf = input("Strafpunten voor deze hint: ").strip()
            if straf.isdigit() and 0 <= int(straf) <= max_punten:
                hints.append(Hint(tekst, int(straf)))
                break
            print(f"Foutmelding: strafpunten moeten tussen 0 en {max_punten} liggen.")
    return hints

def _ontwerp_puzzel(bestaande_titels):
    while True:
        titel = _vraag_niet_leeg("Puzzeltitel: ")
        if titel.lower() in [t.lower() for t in bestaande_titels]:
            print("Foutmelding: puzzeltitel moet uniek zijn binnen de room.")
            continue
        break
    opdracht = _vraag_niet_leeg("Opdracht: ")
    oplossing = _vraag_niet_leeg("Oplossing: ")
    max_punten = _vraag_positief_geheel("Maximale punten (>= 1): ")
    puzzel = Puzzel(titel, opdracht, oplossing, max_punten)
    for hint in _ontwerp_hints(max_punten):
        puzzel.voeg_hint_toe(hint)
    return puzzel


def ontwerp_room():
    """Doorloop de ontwerpstappen en retourneer een geldige EscapeRoom.

    Een room wordt pas geretourneerd als naam, tijdslimiet en minimaal twee
    complete puzzels met unieke titels geldig zijn.
    """
    print("\n=== ONTWERPMODUS ===")
    naam = _vraag_niet_leeg("Naam van de room: ")
    thema = _vraag_niet_leeg("Thema: ")
    tijdslimiet = _vraag_positief_geheel("Tijdslimiet in minuten (>= 1): ")

    room = EscapeRoom(naam, thema, tijdslimiet)
    titels = []
    while True:
        puzzel = _ontwerp_puzzel(titels)
        room.voeg_puzzel_toe(puzzel)
        titels.append(puzzel.get_titel())

        if room.get_aantal_puzzels() < 2:
            print("De room heeft minimaal twee puzzels nodig; voeg nog een puzzel toe.")
            continue
        nog = input("Nog een puzzel toevoegen? (j/n): ").strip().lower()
        if nog != "j":
            break

    print(f"\nRoom '{room.get_naam()}' is gevalideerd en toegevoegd aan de catalogus "
          f"({room.get_aantal_puzzels()} puzzels).")
    return room