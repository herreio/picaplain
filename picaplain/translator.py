COLLECTION_CODE = {
    # 0575 / 016B / Code für Sammlungen
    # Quelle: https://swbtools.bsz-bw.de/cgi-bin/k10plushelp.pl?cmd=kat&katalog=Standard&val=0575
    # Stand: 2023-02-28
    "AUGU": "Augustinus-Literaturdatenbank Würzburg",
    "BA": "Bibliotheken der Aufklärungszeit",
    "BGTS": "Bibliographie Geschichte der Technik (Vergabe durch die SLUB Dresden)",
    "BIDL": "Mikrofiche-Ausgabe der \"Bibliothek der Deutschen Literatur\"",
    "BIIN": "Bibelwissenschaftliche Literaturdokumentation Innsbruck (IxTheo)",
    "BIST": "Mikrofiche-Ausgabe der \"Bibliothek Stein\"",
    "CeDi": "Centralasia Digital",
    "CICO": "Mikrofiche-Ausgabe der \"Cicognara Library\"",
    "DAKR": "Datenbank Kanonisches Recht Münster",
    "dfib": "Frankreich-Bibliothek des DFI Ludwigsburg",
    "DTH5": "Aufsätze und Rezensionen aus dem Digitalisierungsprojekt theologischer Zeitschriften DigiTheo_5",
    "EDCO": "Mikrofiche-Ausgabe der \"Edition Corvey\"",
    "FOOD": "Food studies",
    "FRST": "Sammlungen der Franckeschen Stiftungen Halle (IxTheo)",
    "GIRA": "Literaturdokumentation zur Mimetischen Theorie von René Girard Innsbruck",
    "HistGuide": "History Guide: Fachkatalog digitaler Ressourcen für die Geschichtswissenschaft",
    "INKA": "Daten übernommen aus dem Inkunabelkatalog deutscher Bibliotheken (INKA)",
    "KALD": "Kanonistische Literaturdokumentation Innsbruck (IxTheo)",
    "KOLK": "Kulturrat Oldenburg Karten",
    "krex": "Manueller Eintrag bei maschinell selektierten Datensätzen für KrimDok, die keinen kriminologischen Bezug haben",
    "leos": "In LEO-BW verwendet",
    "MIKA": "Missionsbibliothek und katholische Dokumentationsstelle des MWI Aachen (IxTheo)",
    "MEN": "doc	Fachinformationsdienst Nahost-, Nordafrika- und Islamstudien der Universitäts- und Landesbibliothek Sachsen-Anhalt (Halle)",
    "mkri": "Fachinformationsdienst Kriminologie",
    "mteo": "Theologische und religionswiss. Titel, maschinell gekennzeichnet",
    "mtex": "Manueller Eintrag bei maschinell ursprünglich mit \"mteo\" belegten Datensätzen, die keinen theologischen/religionswiss. Bezug haben",
    "OERR": "Open educational resources Repositorium",
    "PAHA": "Palatina-Handschrift",
    "PALA": "Mikrofiche-Ausgabe der \"Bibliotheca Palatina\"",
    "PZ": "Pommersche Zeitungen/Zeitschriften",
    "redo": "Religionswissenschaft/Dokumentationsstelle",
    "SAVE": "Sicherung des audiovisuellen Erbes in Sachsen",
    "SAXB": "Titel aus der Sächsischen Bibliographie (Vergabe durch die SLUB Dresden)",
    "SP": "Sammlung Perthes",
    "VDLN": "Verteilte digitale Landesbibliothek Niedersachsen",
    "WABU": "Mikrofiche-Ausgabe der \"Edition St. Walburg\" (Frauenklosterbibliothek St. Walburg)",
    "WLMMA": "Wolfgang Laade Music of Man Archive",
}

LENDING_INDICATOR_SWB = {
    # Pica3 7100 / Pica+ 209A/$x00-09 / Signatur
    # Quelle: https://swbtools.bsz-bw.de/cgi-bin/k10plushelp.pl?cmd=kat&katalog=Standard&val=7100
    # Stand: 2023-02-28
    "e": "Erwerbungsdaten",
    "l": "Nur für den Lesesaal",
    "p": "Präsenzbestand",
    "n": "Nicht verleihbar",
    "s": "Für die Benutzung gesperrt",
    "u": "Sonstige Ausleihbeschränkung",
    "v": "Nicht verfügbar"
}


def translate(code, db):
    if isinstance(code, str) \
            and isinstance(db, dict) \
            and code in db:
        return db[code]


def translate_lending_indicator_swb(indicator):
    return translate(indicator, LENDING_INDICATOR_SWB)


def translate_collection_code(code):
    return translate(code, COLLECTION_CODE)
