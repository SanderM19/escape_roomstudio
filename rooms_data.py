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
        "Op de muur staan symbolen voor de zon. Typ de naam van de "
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


def _spookkasteel():
    room = EscapeRoom("Het Spookkasteel", "Gothic horror", 50)

    p1 = Puzzel(
        "De tikkende klok",
        "De spookklok in de hal wijst middernacht aan. Hoeveel keer slaat een "
        "klok om 12 uur 's nachts?",
        "12",
        80,
    )
    p1.voeg_hint_toe(Hint("Een klok slaat evenveel keer als het uur.", 10))

    p2 = Puzzel(
        "Het grafschrift",
        "Op de grafsteen staat: 'Ik ben zwart als de nacht en ik jaag geluidloos'. "
        "Welk nachtdier wordt bedoeld (denk aan een roofvogel)?",
        "uil",
        100,
    )
    p2.voeg_hint_toe(Hint("Het draait zijn kop bijna helemaal rond.", 15))
    p2.voeg_hint_toe(Hint("Het zegt 'oehoe'.", 25))

    p3 = Puzzel(
        "De geheime bibliotheek",
        "Trek een boek uit de kast. Het codewoord is het aantal letters in het "
        "woord 'SPOOK'. Typ dat getal.",
        "5",
        60,
    )
    p3.voeg_hint_toe(Hint("Tel letter voor letter: S-P-O-O-K.", 10))

    for p in (p1, p2, p3):
        room.voeg_puzzel_toe(p)
    return room


def bouw_catalogus():
    """Bouw en retourneer de lijst met standaard escape rooms."""
    return [_pyramide(), _onderzeeer(), _spookkasteel()]