# Escape-roomstudio

Een OOP Python **console-applicatie** waarin escape rooms worden beheerd, ontworpen,
gespeeld en op een scorebord bijgehouden. Het project is iteratief opgebouwd over
vier weekopdrachten (zie de git-historie voor het volledige proces).

## Functionele requirements

| Requirement | Omschrijving | Week |
|-------------|--------------|------|
| **FR-1** | Catalogus tonen met rooms en veilige puzzelinformatie (geen oplossing/hints) | 1 |
| **FR-2** | Spelsessie starten en huidige puzzel bijhouden | 2 |
| **FR-3** | Antwoorden controleren, alleen doorgaan na goed antwoord | 2 |
| **FR-4** | Ongebruikte hints geven met strafpunten | 2 |
| **FR-5** | Score, voortgang en afrondingsstatus tonen | 2 |
| **FR-6** | Ontwerpmodus: rooms samenstellen en valideren | 3 |
| **FR-7** | Speelmodus via hoofdmenu doorlopen | 3 |
| **FR-8** | Scorebord aflopend op score (bij gelijkspel teamnaam A-Z) | 3 |
| **FR-9** *(would-have)* | PDF-spelrapport genereren (reportlab) | 4 |
| **FR-10** *(would-have)* | Persistente opslag in SQLite-database | 4 |

## Projectstructuur

```
escape_roomstudio/
├── main.py            # Entry point met main() en hoofdmenu
├── hint.py            # Hint-klasse
├── puzzel.py          # Puzzel-klasse
├── escape_room.py     # EscapeRoom-klasse
├── spelsessie.py      # Spelsessie-klasse (spelmechaniek)
├── score_resultaat.py # ScoreResultaat-klasse (scorebord)
├── ontwerp.py         # Ontwerpmodus met validatie (FR-6)
├── speelloop.py       # Herbruikbare puzzelloop (FR-3/4/5)
├── rapport.py         # PDF-spelrapport (FR-9)
├── database.py        # SQLite-opslag (FR-10)
├── rooms_data.py      # 3 uitgewerkte standaard-rooms
├── maak_screenshots.py# Hulpscript: testruns -> PNG-screenshots
├── testruns/          # Uitvoer per FR (bewijslast)
└── screenshots/       # Terminal-screenshots per FR
```

Elke klasse staat in een eigen bestand. `main.py` bevat geen klasse, maar de
`main()`-functie waarin de applicatie start (Python-conventie).

## Gebruik

Vereist Python 3.8+ en `reportlab` voor het PDF-rapport:

```bash
pip install reportlab
python3 main.py
```

Bij de eerste start wordt de standaardcatalogus (3 rooms) in de database
`escaperoom.db` opgeslagen. Bij volgende starts worden rooms en scores uit de
database geladen.

### Hoofdmenu

1. **Catalogus bekijken** – rooms en veilige puzzelinformatie (FR-1)
2. **Room ontwerpen** – nieuwe room samenstellen met validatie (FR-6)
3. **Room spelen** – spelsessie doorlopen, antwoord geven / hint vragen (FR-2 t/m FR-5, FR-7)
4. **Scorebord tonen** – gesorteerde resultaten (FR-8)
5. **Afsluiten**

Na een afgeronde sessie kan een **PDF-spelrapport** worden gegenereerd (FR-9),
dat in de map `rapporten/` wordt opgeslagen.

## Standaard-rooms

1. **De Pyramide van Gizeh** – thema Oud-Egypte (3 puzzels)
2. **De Verzonken Onderzeeer** – thema Onderzeeër in nood (3 puzzels)
3. **Het Spookkasteel** – thema Gothic horror (3 puzzels)

## Git & inlevering

Commitlog genereren conform het gevraagde format:

```bash
git log --pretty=format:"-------%n%h %ad [%an] | %B" --date=format:"%Y-%m-%d %H:%M" --stat > commit_log.txt
```
