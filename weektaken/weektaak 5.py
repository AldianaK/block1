"""
author: Aldiana Kucevic
date: 11-10-23
function: alignement tool protein
"""

"""
testing with:
protein 1: A.thaliana
protein 2: X.laevis
"""

def open_file(a_thaliana, x_laevis):
    """
    opening both the files to be able to work with them
    :param a_thaliana: A.thaliana protein sequence
    :param x_laevis: X.laevis protein sequence
    :return: header en sequenties van beide proteins
    """

    # a.thaliana

    header_thaliana = ""
    seq_thaliana = ""

    for line in a_thaliana:
        opened_thaliana = line.replace("\n", "")
        # print(opened_thaliana)
        if ">" in line:
            header_thaliana += line
        else:
            seq_thaliana += line

    #x.laevis

    header_laevis = ""
    seq_laevis = ""

    for line_2 in x_laevis:
        opened_laevis = line_2.replace("\n", "")
        # print(opened_laevis)
        if ">" in line_2:
            header_laevis += line_2
        else:
            seq_laevis += line_2

    print("A.thaliana:", "\n", "header: ", "\n", header_thaliana, "\n",
          "sequence:", "\n", seq_thaliana)
    print("X.laevis:", "\n", "header: ", "\n", header_laevis, "\n",
          "sequence:", "\n", seq_laevis)

    return header_thaliana, header_laevis, seq_thaliana, seq_laevis


def align_tool(seq_thaliana, seq_laevis):
    """
    align two protein sequences
    :param seq_thaliana:
    :param seq_laevis:
    :return:
    """

    total_score = 0

    """
    gaat over de lengte van de kleinste sequentie vandaar de len en min.
    Het kan namelijk niet meer dan de kleinste sequentie alignen.
    """

    for amino_acid in range(len(min(seq_laevis, seq_thaliana))):
        if seq_laevis[amino_acid] == seq_thaliana[amino_acid]:
            total_score += 1
        # zet alle aminozuren tegen elkaar
        print(seq_thaliana[amino_acid], seq_laevis[amino_acid])


    print(total_score)
    """
    This line calculates the percentage of similarity by dividing 
    the total_score by the length of the longer of the two input sequences
    (determined using max) and then multiplying it by 100. 
    It prints this percentage to the console.
    """
    print(total_score / len(max(seq_thaliana, seq_laevis)) * 100)

    return total_score


if __name__ == "__main__":
    a_thaliana = open("LIG1 Arabidopsis thaliana protein sequence.fasta").readlines()
    x_laevis = open("LIG1 Xenopus laevis protein sequence.fasta").readlines()
    print("*" *100)
    header_thaliana, header_laevis, seq_thaliana, seq_laevis = open_file(a_thaliana, x_laevis)
    print("*"*100)
    total_score = align_tool(seq_thaliana, seq_laevis)
