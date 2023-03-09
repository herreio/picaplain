ILN_SYSTEM_FLAG = {
    # Pica3 0000 / Pica+ 001@ / ILNs der Bibliotheken mit Exemplarsatz / Unterfeld: _;_
    # Quelle: https://swbtools.bsz-bw.de/cgi-bin/k10plushelp.pl?cmd=kat&katalog=Standard&adm=1&val=0000#_;_
    # Stand: 2023-03-09
    "A": "Aufsatz in sonstigen Filesets",
    "C": "EBSCO (obsolet)",
    "D": "Elsevier (obsolet)",
    "F": "Springer Verlag (obsolet)",
    "G": "Academic Press (obsolet)",
    "J": "Anzeige in GSO",
    "K": "Kluwer (obsolet)",
    "L": "aus GVK/K10plus kopierte Aufsätze",
    "M": "aus Fileset nach GVK/K10plus kopierte Aufsätze",
    "N": "Keine Anzeige in GSO",
    "S": "ZD18 (obsolet)",
    "U": "Aufsatz in K10plus",
    "V": "British Library (obsolet)",
    "0": "Nicht FLS (obsolet)",
    "1": "FLS (obsolet)",
    "2": "GVK StB Bremen",
    "3": "Einspielpool zur Bearbeitung",
    "4": "SBB-PK (obsolet)",
    "5": "SBB Retro (obsolet)",
    "6": "GVK und PAK",
    "7": "OLC Zeitschriften",
    "9": "Kieler Mathematik-Daten (obsolet)"
}

COLLECTION_CODE = {
    # Pica3 0575 / Pica+ 016B / Code für Sammlungen / Unterfeld: ohne
    # Quelle: https://swbtools.bsz-bw.de/cgi-bin/k10plushelp.pl?cmd=kat&katalog=Standard&val=0575#ohne
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

URL_LICENSE_CODE = {
    # Pica3 4950 / Pica+ 017C / URL zum Volltext / Unterfeld: $4 / Lizenzinformationen
    # Quelle: https://swbtools.bsz-bw.de/cgi-bin/k10plushelp.pl?cmd=kat&katalog=Standard&val=4950#$4
    # Stand: 2023-03-09
    "EL": "Einzellizenz",
    "KF": "Kostenfrei zugänglich nach Registrierung",
    "KW": "Teilweise kostenfrei zugänglich (überwiegender Teil oder ab bzw. vor einem bestimmten Zeitpunkt (Moving Wall) kostenfrei zugänglich)",
    "LF": "Kostenfrei zugänglich ohne Registrierung",
    "NL": "Nationallizenz",
    "PU": "Pay-per-Use",
    "ZZ": "Lizenzpflichtig"
}

URL_ORIGIN_CODE = {
    # Pica3 4950 / Pica+ 017C / URL zum Volltext / Unterfeld: $x / Interne Bemerkungen
    # Quelle: https://swbtools.bsz-bw.de/cgi-bin/k10plushelp.pl?cmd=kat&katalog=Standard&val=4950#$x
    # Stand: 2023-03-09
    "H": "Verlag",
    "A": "Agentur",
    "D": "Digitalisierung",
    "F": "EZB",
    "C": "Archivierung",
    "G": "Aggregator",
    "L": "Langzeitarchivierung",
    "N": "Langzeitarchivierung Nationalbibliothek",
    "R": "Resolving-System",
    "T": "DBIS"
}

LENDING_INDICATOR_SWB = {
    # Pica3 7100 / Pica+ 209A/$x00-09 / Signatur / Unterfeld: $D / Ausleihindikator (nur SWB)
    # Quelle: https://swbtools.bsz-bw.de/cgi-bin/k10plushelp.pl?cmd=kat&katalog=Standard&val=7100#$D
    # Stand: 2023-02-28
    "e": "Erwerbungsdaten",
    "l": "Nur für den Lesesaal",
    "p": "Präsenzbestand",
    "n": "Nicht verleihbar",
    "s": "Für die Benutzung gesperrt",
    "u": "Sonstige Ausleihbeschränkung",
    "v": "Nicht verfügbar"
}
