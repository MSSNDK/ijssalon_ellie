def print_aanbieding():
    prijzen = {
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5
    }
    aanbieding = 0.8 * prijzen["aardbei"]
    reclame = (f"vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}.")
    reclame_tekst2 = reclame[:63]
    reclame_tekst3 = reclame_tekst2.upper()
    reclame_tekst4 = reclame_tekst3.split()
    el = reclame_tekst4
    for el in reclame_tekst4:
        if len(el) >= 5:
            print(el.upper())
        else:
            print(el.lower())
print_aanbieding()
