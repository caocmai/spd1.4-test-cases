import string
"""
Question: Convert an RNA strand to proteins. 

RNA: "AUGUUUUCU" => translates to
Codons: "AUG", "UUU", "UCU" => which become a polypeptide with the following sequence =>
Protein: "Methionine", "Phenylalanine", "Serine"

Codon	Protein
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
    if len(rna) % 3 == 1:
        return "Invalid RNA strand, not multiple of 3s"
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


if __name__ == '__main__':

    # Good Test Cases:
    rna1 = "AUGUUUUCU"
    print(covert_rna_to_proteins(rna1))
    rna2 = "AUGUCAUAUUGCUAG"
    print(covert_rna_to_proteins(rna2))
    # Bad Test Cases:
    rna3 = "auguuuucu"
    print(covert_rna_to_proteins(rna3))
    rna4 = "AUgUcAUAUUGCUAG"
    print(covert_rna_to_proteins(rna4))
    # Edge Test Cases:
    rna5 = "_AUGUUUUCU"
    print(covert_rna_to_proteins(rna5))
    # rna6 = "#AUGUCAUAUUGCUAG"
    # print(covert_rna_to_proteins(rna6))







