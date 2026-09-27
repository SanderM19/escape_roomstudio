"""Genereer een PDF-spelrapport (scorekaart) van een afgeronde sessie."""

import os
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def genereer_spelrapport(sessie, map_pad="rapporten"):
    """Maak een PDF-scorekaart voor een afgeronde spelsessie.

    Bevat team, room, opgeloste puzzels, gebruikte hints en eindscore.
    Retourneert het pad naar de gegenereerde PDF.
    """
    os.makedirs(map_pad, exist_ok=True)
    tijd = datetime.now().strftime("%Y%m%d_%H%M%S")
    veilige_team = "".join(c for c in sessie.teamnaam if c.isalnum() or c in "-_") or "team"
    bestandsnaam = os.path.join(map_pad, f"spelrapport_{veilige_team}_{tijd}.pdf")

    c = canvas.Canvas(bestandsnaam, pagesize=A4)
    breedte, hoogte = A4