"""
Author: Aldiana Kucevic
Date: 17-10-2022
Function: thematoets 1, Deel II Python
"""


def aantal_a_t_mutaties(chr1_oefenbestand):
    """leest het bestand en telt mutaties van A naar T
    PARAMETERS: chr1_oefenbestand en uiteindelijk chr1
    RETURN: chr1_lijst, bestand die is overgezet naar een lijst. mutatieslijst, die alle mutaties van A naar T in een lijst heeft gezet
    """

    chr1_lijst = []
    mutaties_lijst = []

    bestand_chr1 = open("chr1_oefenbestand.vcf", "r").readlines()
    
    for regels in bestand_chr1:
        print(regels) # opent het bestand om te testen of die werkt (print alle lijnen uit)
        # vanaf hier beneden gaat het niet goed:
        # ik wilde zoeken naar een command die de eerste regel zou skippen
        regels = regels.replace("\t", ",").replace("\n", ",") # vervangt alle tabs en lege regels met een komma
        regels = regels.split(",") # zou het bestand moeten splitten bij een komma en dan dus in een lijst moeten zetten
        # als alle tabs en next lines omgezet worden naar komma's, kan ik ze in een keer in een lijst zetten door te splitten op komma's
        chr1_lijst.append(regels) # voeg alles toe in deze lijst
        if regels[3] in chr1_lijst == "A" and regels[4] in chr1_lijst == "T": # als op de 3de index van de lijst een "A" staat en op de 4de index een "T" staat:
            mutaties_lijst.append(regels[3], regels[4]) # voeg het toe aan deze lijst

        return(chr1_lijst, mutaties_lijst)

    
    


def quality_lager_dan(chr1_lijst, quality = 35):
    """ print het aantal puntmutaties met een quality score onder 35 in dit geval
        PARAMETERS: variabele van de qualiteit
        RETURN: quality lijst (een lijst die alle qualities lager dan 35 moet printen)
    """

    quality_lijst = [] # maak een lege lijst aan voor alle qualities die kleiner of gelijk zijn aan 35, dan zit het in een overzicht

    for regel in chr1_lijst:
        print(regel) # test of die de lijst print
        if regel[5] in chr1_lijst <= quality: # als in de lijst index 5 het nummer gelijk of kleiner is dan quality (35)
            quality_lijst.append(regel[5]) # voeg het toe aan deze lijst
    return quality_lijst
        



def unieke_filters(chr1_lijst):
    """ leest de unieke filter namen uit de kolom en retourneert in een lijst
        PARAMETERS: chr1_lijst (een lijst van het bestand)
        RETURN: een lijst met de unieke filters
    """

    unieke_filter_lijst = [] # maak een nieuwe lijst aan voor de opsomming van unieke filters
    
    for lijn in chr1_lijst:
        if "FILTER" not in lijn[6]: # als deze string niet in de lijn zit, willen we de overige printen
            print(lijn[6]) # om te testen of die print zonder de header
            unieke_filter_lijst.append(lijn[6]) # voeg deze lijn toe aan de nieuwe lijst
            
    return unieke_filter_lijst
            
    
     

def main():
    """ Hier komen alle functies in en worden uiteindelijk opgeroepen door de main
    """

    # Het is me niet gelukt om de bestanden in de main te zetten (zodat ze recycled kunnen worden)
    chr1_lijst, mutaties_lijst = aantal_a_t_mutaties("chr1_oefenbestand.vcf")
    quality_lijst = quality_lager_dan(chr1_lijst, quality = 35)
    unieke_filter_lijst = unieke_filters(chr1_lijst)
    

main()
    
