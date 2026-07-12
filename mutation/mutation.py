with open("dna.fasta","w") as f:
    f.write(">human\n")
    f.write("ATGCTGACATAG\n")
    f.write(">mouse\n")
    f.write("ATGTTGACAGAT")

with open("dna.fasta","r") as f:
    data = f.read()
print(data)

def clean_data(fasta_seq):
    cleaned_data = {}
    for i in fasta_seq.splitlines():
        if i.startswith(">"):
            current_seq = i[1:]
        else:
            cleaned_data[current_seq] = i
    return cleaned_data
dna = clean_data(data)
print(dna)

def length_of_seq(dna_dict):
    length = {}
    for org, seq in dna_dict.items():
        length[org] = len(seq)
    return length
print(length_of_seq(dna))

complement = {
    "A":"T",
    "T":"A",
    "G":"C",
    "C":"G"
}
def rev_comp(dna_seq):
    comp_dna = ""
    for i in dna_seq:
        comp = complement.get(i)
        comp_dna += comp
        rev_comp_dna = comp_dna[::-1]
    return rev_comp_dna


def codon_breakage(dna_dict):
    dna_codons = {"Frame 1":{},
                  "Frame 2":{},
                  "Frame 3":{},
                  "Frame 4":{},
                  "Frame 5":{},
                  "Frame 6":{},}
    for org, seq in dna_dict.items():
        
        strands = {
            seq:0,
            rev_comp(seq):3}       
        for all_seq, offset in strands.items():        
          for frame in range(3):
           frame_key = f"Frame {frame + 1 + offset}"
           codons_broken = []
           for base in range(frame,len(all_seq),3):
            codon = all_seq[base:base+3]
            if len(codon) == 3:
             codons_broken.append(codon)
           dna_codons[frame_key][org] = codons_broken 
    return dna_codons
print(codon_breakage(dna)) 

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

def translation(codon_dict):
   translated_codons = {"Frame 1":{},
                  "Frame 2":{},
                  "Frame 3":{},
                  "Frame 4":{},
                  "Frame 5":{},
                  "Frame 6":{},}
   for frame,info in codon_breakage(dna).items():
      
      for org, codons in info.items():   
         protein = "" 
         for triplets in codons:
            aa = codon_table.get(triplets)
            if aa == None:
               continue
            if aa == "*":
               break
            protein += aa
         translated_codons[frame][org] = protein
   return translated_codons
print("\nProtein Translation:\n")
print(translation(codon_breakage(dna)))

def mutations(codon_dict,org_a,org_b):
   syn = []
   nsyn = []
   for frame, info in codon_dict.items():
     for cod_a, cod_b in zip(info[org_a],info[org_b]):
          aa_a = codon_table.get(cod_a)
          aa_b = codon_table.get(cod_b)
          if cod_a == cod_b:
             continue
          elif aa_a == aa_b:
             syn.append((f"{cod_a} -> {cod_b}",f"{aa_a} -> {aa_b}"))
          else:
             nsyn.append((f"{cod_a} -> {cod_b}",f"{aa_a} -> {aa_b}"))
             
   return f"Synonymous Mutations:{syn}\nNon-synonymous Mutations:{nsyn}"
print(mutations(codon_breakage(dna),"human","mouse")) 