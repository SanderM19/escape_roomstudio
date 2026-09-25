"""Vaste catalogus met drie volledig uitgewerkte escape rooms.

Elke room heeft een samenhangend thema, minimaal 3 puzzels met echte,
controleerbare oplossingen en verdeeld over de room minimaal 2 bruikbare hints.
"""

from hint import Hint
from puzzel import Puzzel
from escape_room import EscapeRoom


def _pyramide():
    room = EscapeRoom("De Pyramide van Gizeh", "Oud-Egypte", 60)

    p1 = Puzzel(
        "De vervloekte hieroglief",
        "Op de muur staan symbolen voor de zon (RA). Typ de naam van de "
        "Egyptische zonnegod die bij het zonsymbool hoort.",
        "Ra",
        100,
    )
    p1.voeg_hint_toe(Hint("De god wordt vaak afgebeeld met een valkenkop.", 10))
    p1.voeg_hint_toe(Hint("Zijn naam bestaat uit twee letters.", 20))

    p2 = Puzzel(
        "Het getal van de farao",
        "De sarcofaag heeft 3 sloten met getallen 7, 14 en het ontbrekende getal. "
        "De reeks verdubbelt telkens. Welk getal komt na 14?",
        "28",
        80,
    )
    p2.voeg_hint_toe(Hint("Elk getal is het dubbele van het vorige.", 15))

    p3 = Puzzel(
        "De grafkamer",
        "Rangschik de dodenmasker-kleuren. De belangrijkste kleur van "
        "Toetanchamon's masker (naast blauw) is een edelmetaal. Welke?",
        "goud",
        120,
    )
    p3.voeg_hint_toe(Hint("Het glimt en is zeer kostbaar.", 10))

    for p in (p1, p2, p3):
        room.voeg_puzzel_toe(p)
    return room

def _onderzeeer():
    room = EscapeRoom("De Verzonken Onderzeeer", "Onderzeeër in nood", 45)

    p1 = Puzzel(
        "SOS in morse",
        "De radio piept: ... --- ... . Wat is het internationale noodsignaal "
        "(drie letters) dat hierbij hoort?",
        "SOS",
        90,
    )
    p1.voeg_hint_toe(Hint("Drie korte, drie lange, drie korte tonen.", 15))

    p2 = Puzzel(
        "Ballasttanks",
        "Om te stijgen moet lucht in de tanks. Typ het woord voor het naar boven "
        "komen van de onderzeeer.",
        "opstijgen",
        70,
    )
    p2.voeg_hint_toe(Hint("Het tegenovergestelde van duiken.", 10))
    p2.voeg_hint_toe(Hint("Het werkwoord begint met 'op'.", 20))

    p3 = Puzzel(
        "De dieptemeter",
        "De meter staat op 200 meter. Per minuut stijg je 25 meter. Na hoeveel "
        "minuten ben je aan het oppervlak (0 meter)?",
        "8",
        110,
    )
    p3.voeg_hint_toe(Hint("Deel de diepte door de stijgsnelheid.", 15))

    for p in (p1, p2, p3):
        room.voeg_puzzel_toe(p)
    return room