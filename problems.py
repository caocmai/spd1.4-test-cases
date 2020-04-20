import string
"""
Question: Convert an RNA strand to proteins. 

RNA: "AUGUUUUCU" => translates to
Codons: "AUG", "UUU", "UCU" => which become a polypeptide with the following sequence =>
Protein: "Methionine", "Phenylalanine", "Serine"

Codon	            Protein
AUG	                Methionine
UUU, UUC	        Phenylalanine
UUA, UUG	        Leucine
UCU, UCC, UCA, UCG	Serine
UAU, UAC	        Tyrosine
UGU, UGC	        Cysteine
UGG	                Tryptophan
UAA, UAG, UGA	    STOP

"""

def split_to_codons(rna):
    return [rna[i:i+3] for i in range(0, len(rna), 3)]

def covert_rna_to_proteins(rna):
    # For Bad Cases
    if len(rna) % 3 == 1:
        return "Invalid RNA strand, not multiple of 3s"

    # For Edge Cases
    for letter in rna:
        if letter.upper() not in string.ascii_uppercase:
            return "Invalid characters in RNA"

    codons = split_to_codons(rna)
    translation = { 'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 
                    'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine', 
                    'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 
                    'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan', 
                    'UAA': 'stop', 'UGA': 'stop', 'UAG': 'stop'
                    }
    
    proteins = []
    for codon in codons:
        codon_upper = codon.upper()
        if translation[codon_upper] == 'stop':
            break
        protein = translation[codon_upper]
        proteins.append(protein)
    return proteins


"""
Question: Convert a phrase to its acronym.

input: "change me to acronym"
output: "CMTA"
"""

def to_acronym(text):
    acronym = ""

    splited_text = text.split()
    for i in range(len(splited_text)):
        for letter in splited_text[i]:
            if letter.isdigit():
                acronym += letter
            elif letter in string.ascii_letters:
                acronym += letter.upper()
                break
    return acronym


if __name__ == '__main__':

    # Q1. Good Test Cases:
    rna1 = "AUGUUUUCU"
    print(covert_rna_to_proteins(rna1))
    rna2 = "AUGUCAUAUUGCUAG"
    print(covert_rna_to_proteins(rna2))

    # Q1. Bad Test Cases:
    rna3 = "auguuuucu" # Lowercase instead of uppercase
    print(covert_rna_to_proteins(rna3))
    rna4 = "AUgUcAUAUUGCUAG" 
    print(covert_rna_to_proteins(rna4))

    # Q1. Edge Test Cases:
    rna5 = "_AUGUUUUC" # Invalid RNA characters
    print(covert_rna_to_proteins(rna5))
    rna6 = "#AUGUCAUAUUGCUAG" 
    print(covert_rna_to_proteins(rna6))

    print("\n")

    # Q2. Good Test Cases:
    text1 = "change me to acronym"
    print(to_acronym(text1))
    text1b = "these are good inputs"
    print(to_acronym(text1b))

    # Q2. Bad Test Cases:
    text2 = "i  have  an  extra  space  between  words"
    print(to_acronym(text2))
    text2b = "i also have numbers in my text which is 23"
    print(to_acronym(text2b))

    # Q2. Edge Test Cases:
    text3 = " I now have $special &*characters in my string "
    print(to_acronym(text3))
    text3b = " I now have speical   cha@cters \n and sp#acing    as well as break \n\n lines"
    print(to_acronym(text3b))









