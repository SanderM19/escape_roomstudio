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

    # Kop / certificaat-banner
    c.setFillColor(colors.HexColor("#1a237e"))
    c.rect(0, hoogte - 3.5 * cm, breedte, 3.5 * cm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(breedte / 2, hoogte - 2.2 * cm, "ESCAPE-ROOMSTUDIO")
    c.setFont("Helvetica", 13)
    c.drawCentredString(breedte / 2, hoogte - 3.0 * cm, "Officieel Spelrapport & Scorekaart")

    y = hoogte - 5 * cm
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(2 * cm, y, f"Team: {sessie.teamnaam}")
    y -= 0.8 * cm
    c.drawString(2 * cm, y, f"Escape room: {sessie.escape_room.get_naam()}")
    y -= 0.8 * cm
    c.setFont("Helvetica", 11)
    c.drawString(2 * cm, y, f"Thema: {sessie.escape_room.thema}   |   "
                            f"Tijdslimiet: {sessie.escape_room.tijdslimiet} min")
    y -= 0.6 * cm
    c.drawString(2 * cm, y, f"Datum: {datetime.now().strftime('%d-%m-%Y %H:%M')}")