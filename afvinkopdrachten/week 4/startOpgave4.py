# Iteratie opdracht
# Start script voor opgave over sikkelcel
# (c) Martijn van der Bruggen, 2007-2010
# Updates:
# November 2010, code bijgewerkt met instructies voor de opdracht
# Hogeschool van Arnhem en Nijmegen

# Sequenties voor respectievelijk sikkelcel- en normale cellen
# Bekend is dat het gen coderend voor hemoglobine bij sikkelcel aandoening een andere nucleotide heeft
# De sequentie voor de sikkelcel en een "gezonde bloedcel" zijn hier onder gegeven
sikkel_seq = 'GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'
normaal_seq ='GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'

# In het bestand enzymen. txt staan kandidaat restrictie enzymen
# Opdracht schrijf een programma dat al deze enzymen doorloopt een suggestie
# geeft welk restrictie enzym welk knipt in de ene sequentie en niet in de andere sequentie
# Hiermee kunnen we diagnostisch enzym voorstellen om vast te stellen of een persoon
# drager is van het sikkelcel allel

with open("enzymen.txt", "r") as bestand:
    geopende_bestand = bestand.readlines() # lees door de lines
    for regel in geopende_bestand:
        enzym, seq = regel.split() # split items
        enzym_sequentie = seq.replace("^", "") # haalt dakjes weg
        print(enzym," ",enzym_sequentie)
        if enzym_sequentie in sikkel_seq and enzym_sequentie not in normaal_seq:
            print(enzym, "enzym gevonden in sikkelcel sequentie")
        elif enzym_sequentie in normaal_seq and enzym_sequentie not in sikkel_seq:
            print(enzym, "enzym gevonden in normale sequentie")
        elif enzym_sequentie in normaal_seq and enzym_sequentie in sikkel_seq:
            print(enzym, "enzym in beide sequenties gevonden")
        else:
            print(enzym, "in geen van de sequenties gevonden")

"""
checkt dus of die enzymen in het bestand voorkomen, door te zoeken naar enzym
sequentie in de andere gegeven sequenties.
"""



# Aanwijzingen voor het schrijven van je programma
# -------------------------------------------------------------
# Het lezen van een regel kan met bestand.readline() bijvoorbeeld: regel = bestand.readline(). Print de regel en bekijk wat hieruit komt
# Lees door totdat je een lege regel aantreft
# Een regel bestaat uit twee stukken enzym en knipsequentie. Bijvoorbeeld: DdeI C^TGAG
# Het opsplitsen van een regel in twee stukken op de spatie kan middels: enzym, seq = regel.split()
# Door bovenstaande split verkrijg je twee variabelen enzym en seq, respectievelijk de naam van het enzym en de sequentie waar deze in knipt
# Verwijderen het dakje uit de seq met seq.replace("^","")
# --------------------------------------------------------------------

# Auteur: Aldiana
# Datum: 6-10-2023
# Functie: week 4 opdracht 3

