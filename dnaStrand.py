def DNA_strand(dna):
    nucleotide = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    newStrand = []

    for n in dna:
        newStrand.append(nucleotide[n])

    return ''.join(newStrand)


print(DNA_strand("AAGGCCTT"))
