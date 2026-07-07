import sys

if len(sys.argv) <2:
    print("Error: Please provide a valid input file")
    sys.exit()

sequence = sys.argv[1]

with open(sequence,"r") as f:
    seq = f.readlines()

def clean_seq(dna_seq):
    clean = []
    for line in dna_seq:
        if line.startswith(">"):
            continue
        clean.append(line.strip())
    return clean

cleaned_seq = "".join(clean_seq(seq)).upper()

try:
    gc_content = (cleaned_seq.count('G') + cleaned_seq.count("C"))/len(cleaned_seq)
    print(f"The GC content of the DNA sequence is: {gc_content:.2%}")
    print(f"The total length of the DNA sequence is: {len(cleaned_seq)}")
    print(f"The first 50 nucleotides are : {cleaned_seq[:50]}")
except Exception as e:
    print(e)