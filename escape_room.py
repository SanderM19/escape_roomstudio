"""EscapeRoom-klasse voor de escape-roomstudio."""

class EscapeRoom:
    """Een escape room met een thema, tijdslimiet en een geordende reeks puzzels."""

    def __init__(self, naam, thema, tijdslimiet):
        self.naam = naam
        self.thema = thema
        self.tijdslimiet = tijdslimiet  # in minuten
        self.puzzel_lijst = []

    def voeg_puzzel_toe(self, puzzel):
        self.puzzel_lijst.append(puzzel)

    def get_puzzels(self):
        return self.puzzel_lijst

    def get_naam(self):
        return self.naam

    def get_aantal_puzzels(self):
        return len(self.puzzel_lijst)

    def __str__(self):
        regels = [
            f"Escape room: {self.naam}",
            f"Thema: {self.thema}",
            f"Tijdslimiet: {self.tijdslimiet} minuten",
            f"Aantal puzzels: {len(self.puzzel_lijst)}",
        ]
        return "\n".join(regels)