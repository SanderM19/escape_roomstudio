"""Hint-klasse voor de escape-roomstudio."""

class Hint:
    """Een hint bij een puzzel. Kost strafpunten wanneer hij gebruikt wordt."""

    def __init__(self, tekst, strafpunten):
        self.tekst = tekst
        self.strafpunten = strafpunten

    def get_tekst(self):
        return self.tekst

    def get_strafpunten(self):
        return self.strafpunten

    def __str__(self):
        return f"{self.tekst} (-{self.strafpunten} punten)"