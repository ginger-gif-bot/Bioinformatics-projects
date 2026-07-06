with open("nucleotide.fasta","r") as f:
    seq = f.readlines()

dna_seq = seq

def clean_seq(seq):
    seq_clean = []
    for i in seq:
        if i.startswith(">"):
            continue
        else:
            seq_clean.append(i.strip())

    return seq_clean

clean_dna_seq = clean_seq(dna_seq)
ready_dna = "".join(clean_dna_seq).upper()

try:
    gc_content = (ready_dna.count('G') + ready_dna.count("C"))/len(ready_dna)
    print(f"The GC content of the DNA sequence is: {gc_content:.2%}")
    print(f"The total length of the DNA sequence is: {len(ready_dna)}")
    print(f"The first 50 nucleotides are : {ready_dna[:50]}") 
except Exception as e:
    print(e)