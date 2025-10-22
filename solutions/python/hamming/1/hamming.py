def distance(strand_a, strand_b):
    hmng_dist=0
    if len(strand_a)!=len(strand_b):
        raise ValueError("Strands must be of equal length.")
    for i in range(len(strand_a)):
        if strand_a[i]!=strand_b[i]:
            hmng_dist+=1
    return hmng_dist
