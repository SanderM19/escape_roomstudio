"""Escape-roomstudio - hoofdapplicatie (week 1: alleen catalogusmodus)."""

from rooms_data import bouw_catalogus


def toon_catalogus(rooms):
    print("\n=== CATALOGUS ESCAPE ROOMS ===")
    for index, room in enumerate(rooms, start=1):
        print(f"{index}. {room.get_naam()} ({room.get_aantal_puzzels()} puzzels)")