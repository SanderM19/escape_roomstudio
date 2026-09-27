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