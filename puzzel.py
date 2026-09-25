"""Puzzel-klasse voor de escape-roomstudio (week 1: basis catalogusinformatie)."""

class Puzzel:
    """Een puzzel binnen een escape room met titel, opdracht, oplossing en hints."""

    def __init__(self, titel, opdracht, oplossing, max_punten):
        self.titel = titel
        self.opdracht = opdracht
        self.oplossing = oplossing
        self.max_punten = max_punten
        self.hint_lijst = []

    def voeg_hint_toe(self, hint):
        self.hint_lijst.append(hint)

    def get_titel(self):
        return self.titel

    def get_max_punten(self):
        return self.max_punten

    def get_aantal_hints(self):
        return len(self.hint_lijst)

    def controleer_oplossing(self, antwoord):
        """Vergelijk het antwoord zonder verschil tussen hoofd-/kleine letters."""
        if antwoord is None:
            return False
        return antwoord.strip().lower() == self.oplossing.strip().lower()

    def get_hint(self, index):
        """Retourneer de hint op de gegeven index, of None als die niet bestaat."""
        if 0 <= index < len(self.hint_lijst):
            return self.hint_lijst[index]
        return None

    def bereken_punten(self, gebruikte_hints):
        """Trek de strafpunten van de gebruikte hints af; nooit minder dan 0."""
        straf = 0
        for i in range(min(gebruikte_hints, len(self.hint_lijst))):
            straf += self.hint_lijst[i].get_strafpunten()
        punten = self.max_punten - straf
        return max(punten, 0)

    def __str__(self):
        # Toont alleen veilige, niet-geheime informatie (geen oplossing/hints).
        return (
            f"{self.titel}\n"
            f"   Opdracht: {self.opdracht}\n"
            f"   Maximaal te behalen punten: {self.max_punten}"
        )