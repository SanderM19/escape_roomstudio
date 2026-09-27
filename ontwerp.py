"""Ontwerpmodus: een room met puzzels en hints samenstellen en valideren (FR-6)."""

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