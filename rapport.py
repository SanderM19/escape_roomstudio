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

    # Puzzeloverzicht
    y -= 1.2 * cm
    c.setFont("Helvetica-Bold", 13)
    c.drawString(2 * cm, y, "Opgeloste puzzels")
    y -= 0.3 * cm
    c.setStrokeColor(colors.grey)
    c.line(2 * cm, y, breedte - 2 * cm, y)
    y -= 0.7 * cm

    c.setFont("Helvetica", 11)
    puzzels = sessie.escape_room.get_puzzels()
    aantal_opgelost = min(sessie.huidige_puzzel_index, len(puzzels))
    for i in range(aantal_opgelost):
        puzzel = puzzels[i]
        hints = sessie.gebruikte_hints.get(i, 0)
        punten = puzzel.bereken_punten(hints)
        c.drawString(2.2 * cm, y, f"{i + 1}. {puzzel.get_titel()}")
        c.drawRightString(breedte - 2 * cm, y,
                          f"{hints} hint(s) - {punten} pnt")
        y -= 0.6 * cm
        if y < 4 * cm:
            c.showPage()
            y = hoogte - 3 * cm

    # Eindscore-blok
    y -= 0.5 * cm
    c.setFillColor(colors.HexColor("#c8e6c9"))
    c.rect(2 * cm, y - 1.5 * cm, breedte - 4 * cm, 1.6 * cm, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#1b5e20"))
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(breedte / 2, y - 0.7 * cm,
                        f"EINDSCORE: {sessie.score} punten  |  "
                        f"Voortgang: {sessie.get_voortgang_procent()}%")

    c.setFillColor(colors.grey)
    c.setFont("Helvetica-Oblique", 9)
    c.drawCentredString(breedte / 2, 1.5 * cm,
                        "Gefeliciteerd! Bewaar deze scorekaart als bewijs van jullie prestatie.")
    c.showPage()
    c.save()
    return bestandsnaam