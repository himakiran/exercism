codon_dict = {'AUG':"Methionine",'UUU':"Phenylalanine",'UUC':"Phenylalanine",'UUA' : "Leucine",'UUG':"Leucine",'UCU':"Serine",'UCC':"Serine",'UCA':"Serine",'UCG':"Serine",'UAU':"Tyrosine",'UAC':"Tyrosine", 'UGU':"Cysteine",'UGC':"Cysteine",'UGG':"Tryptophan", 'UAA':"STOP",'UAG':"STOP",'UGA':"STOP"}

def proteins(strand):
    protein_list = []
    i = 0
    j = i+3
    while(j<=len(strand)):
        if strand[i:j] in codon_dict.keys() and codon_dict[strand[i:j]]!="STOP":
            print(strand[i:j])
            protein_list.append(codon_dict[strand[i:j]])
        if codon_dict[strand[i:j]]=="STOP":
            break
        i+=3
        j=i+3
    return protein_list
        
