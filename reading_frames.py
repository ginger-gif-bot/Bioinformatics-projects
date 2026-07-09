import sys

if len(sys.argv) <2:
    print("Error")
    sys.exit()
file = sys.argv[1]

with open(file,'r') as f:
    data = f.read()

codon_table = {
    "TTT":"F","TTC":"F","TTA":"L","TTG":"L",
    "CTT":"L","CTC":"L","CTA":"L","CTG":"L",
    "ATT":"I","ATC":"I","ATA":"I","ATG":"M",
    "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
    "TCT":"S","TCC":"S","TCA":"S","TCG":"S",
    "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
    "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
    "GCT":"A","GCC":"A","GCA":"A","GCG":"A",
    "TAT":"Y","TAC":"Y","TAA":"*","TAG":"*",
    "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "AAT":"N","AAC":"N","AAA":"K","AAG":"K",
    "GAT":"D","GAC":"D","GAA":"E","GAG":"E",
    "TGT":"C","TGC":"C","TGA":"*","TGG":"W",
    "CGT":"R","CGC":"R","CGA":"R","CGG":"R",
    "AGT":"S","AGC":"S","AGA":"R","AGG":"R",
    "GGT":"G","GGC":"G","GGA":"G","GGG":"G",
}

complement = {"A":"T",
              "T":"A",
              "G":"C",
              "C":"G"}
seq = {}
for i in data.splitlines():
    if i.startswith(">"):
        current_seq = i[1:]
        dna = []
    else:
        dna.append(i)
        seq[current_seq] = "".join(dna)

# print(seq.values())

def codon_break(seq_dict):
    transation = {"Frame 1":{},
                   "Frame 2":{},
                   "Frame 3":{}}
    dna_codons = {"Frame 1":{},
                   "Frame 2":{},
                   "Frame 3":{}}
    for frame in range(3):
     frame_key = f"Frame {frame + 1}"       
     for org, seq in seq_dict.items():
         codons = []
         protein = ""
         for dna in range(frame,len(seq),3):
            codon = seq[dna:dna+3]
            if len(codon) == 3:
             codons.append(codon)
             aa = codon_table.get(codon)
            if aa == None:
                continue
            if aa == "*":
                break
            protein += aa
         transation[frame_key][org] = protein 
         dna_codons[frame_key][org] = codons     
    return dna_codons,transation 

dna_cod,dna_to_protein = codon_break(seq)
print(dna_cod)
print(dna_to_protein) 



                


