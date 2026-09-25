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

    def __str__(self):
        # Toont alleen veilige, niet-geheime informatie (geen oplossing/hints).
        return (
            f"{self.titel}\n"
            f"   Opdracht: {self.opdracht}\n"
            f"   Maximaal te behalen punten: {self.max_punten}"
        )