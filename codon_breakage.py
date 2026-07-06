import sys
#so that we can use sys.exit() to exit the program if the user does not provide a valid input file
if len(sys.argv) <2:
    print("Please provide a valid input file")
    sys.exit()

fasta_file = sys.argv[1]

with open(fasta_file,"r") as f:
    sequence = f.readlines()

def clean_seq(seq):
    clean = []
    for line in seq:
        if line.startswith(">"):
            continue
        clean.append(line.strip())
    return clean

clean_seq = "".join(clean_seq(sequence)).upper()
print(f"The cleaned DNA sequence is: {clean_seq}")

def codon(seq):
    codon = []
    for i in range(0, len(seq),3):
        codon_seq = seq[i:i+3]
        if len(codon_seq) ==3:
            if codon_seq == "ATG":
                codon.append((i+1, codon_seq))
    return codon

atg_codons = codon(clean_seq)
print(f"The ATG codons are located at positions: {atg_codons}")

try:
    gc_content = (clean_seq.count('G') + clean_seq.count("C"))/len(clean_seq)
    print(f"The GC content of the DNA sequence is: {gc_content:.2%}")
    print(f"The total length of the DNA sequence is: {len(clean_seq)}")
    print(f"The first 50 nucleotides are : {clean_seq[:50]}")
except Exception as e:
    print(e)
