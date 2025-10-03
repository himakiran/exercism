def to_rna(dna_strand):
    dna2rna_dict = {'G':'C','C':'G','T':'A','A':'U'}
    rna=""
    for each in list(dna_strand):
        if each in dna2rna_dict.keys():
            each=dna2rna_dict[each]
        rna+=each
    return rna
