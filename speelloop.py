"""Herbruikbare puzzelloop voor een spelsessie (FR-3, FR-4, FR-5)."""


def speel_sessie(sessie):
    """Doorloop alle puzzels van een sessie tot deze is afgerond.

    Bij een fout antwoord blijft dezelfde puzzel actief; bij een goed antwoord
    wordt de volgende getoond. Een hint kan per puzzel maar zo vaak als er
    ongebruikte hints zijn worden opgevraagd en verlaagt de te behalen punten.
    """
    print(f"\nSpelsessie gestart voor team '{sessie.teamnaam}' "
          f"in room '{sessie.escape_room.get_naam()}'.")

    while not sessie.is_afgerond():
        puzzel = sessie.get_huidige_puzzel()
        nummer = sessie.huidige_puzzel_index + 1
        totaal = sessie.escape_room.get_aantal_puzzels()
        print("\n" + "=" * 45)
        print(f"Puzzel {nummer}/{totaal}: {puzzel.get_titel()}")
        print(f"Opdracht: {puzzel.opdracht}")
        print(f"Voortgang: {sessie.get_voortgang_procent()}% | "
              f"Huidige score: {sessie.score}")

        actie = input("Kies een actie - [a]ntwoord geven / [h]int vragen: ").strip().lower()

        if actie == "h":
            hint = sessie.vraag_hint()
            if hint is None:
                print(">> Geen ongebruikte hint meer beschikbaar voor deze puzzel.")
            else:
                print(f">> Hint: {hint}")
        elif actie == "a":
            antwoord = input("Jouw antwoord: ")
            if sessie.geef_antwoord(antwoord):
                print(">> Correct! Door naar de volgende puzzel.")
            else:
                print(">> Helaas, dat is niet juist. Probeer het opnieuw.")
        else:
            print(">> Ongeldige actie. Kies 'a' of 'h'.")

    print("\n" + "*" * 45)
    print("Escape room afgerond!")
    print(f"Team: {sessie.teamnaam}")
    print(f"Eindscore: {sessie.score}")
    print(f"Voortgang: {sessie.get_voortgang_procent()}%")
    print("*" * 45)