"""ScoreResultaat-klasse voor het scorebord."""


class ScoreResultaat:
    """Een afgerond resultaat met teamnaam, roomnaam en score."""

    def __init__(self, teamnaam, roomnaam, score):
        self.teamnaam = teamnaam
        self.roomnaam = roomnaam
        self.score = score

    def __str__(self):
        return f"{self.teamnaam} - {self.roomnaam}: {self.score} punten"