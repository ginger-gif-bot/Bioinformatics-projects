import sys

if len(sys.argv) <2:
    print("Error")
    sys.exit()
file = sys.argv[1]

with open(file,'r') as f:
    data = f.read()

# print(data.split())

seq = {}
for i in data.splitlines():   
    if i.startswith(">"):
        current_line = i[1:]
        dna = []
    else:  
        dna.append(i)
        seq[current_line] = "".join(dna)
# print(seq)

gc_content = {}
for name, sequence in seq.items():
    try:
     gc_content[name] = round(((sequence.count("G") + sequence.count("C"))/len(sequence)*100),2)
    except ZeroDivisionError:
        print("The length of the sequence is zero.") 
print(gc_content)

codons_in_dna = {}
for name, dna in seq.items():
    dna_codon = []
    for i in range(0,len(dna),3):
        codon = dna[i:i+3]
        if len(codon) == 3:
            dna_codon.append(codon)
            codons_in_dna[name] = dna_codon
# print(codons_in_dna)

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


protein = {}
for name, cod in codons_in_dna.items():
    amino = ""
    for i in cod:
         aa = codon_table.get(i)
         
         if aa == None:
          continue
         amino += aa
         if aa == "*":
             break
        
         protein[name] = amino

for animal, pro_seq in protein.items():
    
 print(f"{animal}:\t{[pro_seq]}\n") 