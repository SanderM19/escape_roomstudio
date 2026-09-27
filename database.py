"""Persistente opslag van rooms, puzzels, hints en scores in SQLite."""

import sqlite3

from hint import Hint
from puzzel import Puzzel
from escape_room import EscapeRoom
from score_resultaat import ScoreResultaat

DB_PAD = "escaperoom.db"


def _verbinding(db_pad=DB_PAD):
    conn = sqlite3.connect(db_pad)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_database(db_pad=DB_PAD):
    """Maak de tabellen aan als ze nog niet bestaan."""
    conn = _verbinding(db_pad)
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naam TEXT NOT NULL,
            thema TEXT NOT NULL,
            tijdslimiet INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS puzzels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_id INTEGER NOT NULL,
            volgorde INTEGER NOT NULL,
            titel TEXT NOT NULL,
            opdracht TEXT NOT NULL,
            oplossing TEXT NOT NULL,
            max_punten INTEGER NOT NULL,
            FOREIGN KEY (room_id) REFERENCES rooms(id) ON DELETE CASCADE
        );
        CREATE TABLE IF NOT EXISTS hints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            puzzel_id INTEGER NOT NULL,
            volgorde INTEGER NOT NULL,
            tekst TEXT NOT NULL,
            strafpunten INTEGER NOT NULL,
            FOREIGN KEY (puzzel_id) REFERENCES puzzels(id) ON DELETE CASCADE
        );
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teamnaam TEXT NOT NULL,
            roomnaam TEXT NOT NULL,
            score INTEGER NOT NULL
        );
        """
    )
    conn.commit()
    conn.close()


def bewaar_room(room, db_pad=DB_PAD):
    """Sla een EscapeRoom met puzzels en hints op."""
    conn = _verbinding(db_pad)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO rooms (naam, thema, tijdslimiet) VALUES (?, ?, ?)",
        (room.get_naam(), room.thema, room.tijdslimiet),
    )
    room_id = cur.lastrowid
    for p_index, puzzel in enumerate(room.get_puzzels()):
        cur.execute(
            "INSERT INTO puzzels (room_id, volgorde, titel, opdracht, oplossing, max_punten) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (room_id, p_index, puzzel.titel, puzzel.opdracht,
             puzzel.oplossing, puzzel.max_punten),
        )
        puzzel_id = cur.lastrowid
        for h_index, hint in enumerate(puzzel.hint_lijst):
            cur.execute(
                "INSERT INTO hints (puzzel_id, volgorde, tekst, strafpunten) "
                "VALUES (?, ?, ?, ?)",
                (puzzel_id, h_index, hint.tekst, hint.strafpunten),
            )
    conn.commit()
    conn.close()
    return room_id


def bewaar_alle_rooms(rooms, db_pad=DB_PAD):
    for room in rooms:
        bewaar_room(room, db_pad)


def laad_rooms(db_pad=DB_PAD):
    """Laad alle rooms (met puzzels en hints) uit de database."""
    conn = _verbinding(db_pad)
    cur = conn.cursor()
    rooms = []
    cur.execute("SELECT id, naam, thema, tijdslimiet FROM rooms ORDER BY id")
    for room_id, naam, thema, tijdslimiet in cur.fetchall():
        room = EscapeRoom(naam, thema, tijdslimiet)
        cur.execute(
            "SELECT id, titel, opdracht, oplossing, max_punten FROM puzzels "
            "WHERE room_id = ? ORDER BY volgorde",
            (room_id,),
        )
        for puzzel_id, titel, opdracht, oplossing, max_punten in cur.fetchall():
            puzzel = Puzzel(titel, opdracht, oplossing, max_punten)
            cur.execute(
                "SELECT tekst, strafpunten FROM hints WHERE puzzel_id = ? ORDER BY volgorde",
                (puzzel_id,),
            )
            for tekst, strafpunten in cur.fetchall():
                puzzel.voeg_hint_toe(Hint(tekst, strafpunten))
            room.voeg_puzzel_toe(puzzel)
        rooms.append(room)
    conn.close()
    return rooms


def bewaar_score(resultaat, db_pad=DB_PAD):
    conn = _verbinding(db_pad)
    conn.execute(
        "INSERT INTO scores (teamnaam, roomnaam, score) VALUES (?, ?, ?)",
        (resultaat.teamnaam, resultaat.roomnaam, resultaat.score),
    )
    conn.commit()
    conn.close()


def laad_scores(db_pad=DB_PAD):
    conn = _verbinding(db_pad)
    cur = conn.cursor()
    cur.execute("SELECT teamnaam, roomnaam, score FROM scores")
    resultaten = [ScoreResultaat(t, r, s) for t, r, s in cur.fetchall()]
    conn.close()
    return resultaten


def database_is_gevuld(db_pad=DB_PAD):
    conn = _verbinding(db_pad)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM rooms")
    aantal = cur.fetchone()[0]
    conn.close()
    return aantal > 0