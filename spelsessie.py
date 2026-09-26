"""Spelsessie-klasse: koppelt een team aan een room en bewaakt score en voortgang."""


class Spelsessie:
    """Beheert het spelen van een escape room door een team.

    Oplossingsstatus en gebruikte hints horen bij de sessie, zodat meerdere
    teams dezelfde room onafhankelijk kunnen spelen.
    """

    def __init__(self, teamnaam, escape_room):
        self.teamnaam = teamnaam
        self.escape_room = escape_room
        self.huidige_puzzel_index = 0
        self.score = 0
        # index van de puzzel -> aantal gebruikte hints
        self.gebruikte_hints = {}

    def get_huidige_puzzel(self):
        puzzels = self.escape_room.get_puzzels()
        if self.huidige_puzzel_index < len(puzzels):
            return puzzels[self.huidige_puzzel_index]
        return None

    def _aantal_gebruikte_hints(self, index):
        return self.gebruikte_hints.get(index, 0)

    def geef_antwoord(self, antwoord):
        """Controleer het antwoord. Bij goed: punten optellen en doorgaan.

        Retourneert True bij een goed antwoord, anders False.
        """
        puzzel = self.get_huidige_puzzel()
        if puzzel is None:
            return False
        if puzzel.controleer_oplossing(antwoord):
            gebruikt = self._aantal_gebruikte_hints(self.huidige_puzzel_index)
            self.score += puzzel.bereken_punten(gebruikt)
            self.huidige_puzzel_index += 1
            return True
        return False

    def vraag_hint(self):
        """Geef de eerstvolgende ongebruikte hint van de huidige puzzel.

        Retourneert de Hint, of None als er geen ongebruikte hint meer is.
        """
        puzzel = self.get_huidige_puzzel()
        if puzzel is None:
            return None
        index = self.huidige_puzzel_index
        gebruikt = self._aantal_gebruikte_hints(index)
        hint = puzzel.get_hint(gebruikt)
        if hint is None:
            return None
        self.gebruikte_hints[index] = gebruikt + 1
        return hint

    def get_voortgang(self):
        """Voortgang als fractie tussen 0.0 en 1.0."""
        totaal = self.escape_room.get_aantal_puzzels()
        if totaal == 0:
            return 1.0
        return self.huidige_puzzel_index / totaal

    def get_voortgang_procent(self):
        return round(self.get_voortgang() * 100)

    def is_afgerond(self):
        return self.huidige_puzzel_index >= self.escape_room.get_aantal_puzzels()

    def __str__(self):
        return (
            f"Team '{self.teamnaam}' speelt '{self.escape_room.get_naam()}' | "
            f"Score: {self.score} | Voortgang: {self.get_voortgang_procent()}%"
        )