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
    dna_codons = {}
    for org, seq in dna_dict.items():
        codons_broken = []
        print(f"the complements are: {rev_comp(seq)}")
        strands = {
            seq:0,
            rev_comp(seq):3
        }
        
        for base in range(0,len(seq),3):
         codon = seq[base:base+3]
         if len(codon) == 3:
             codons_broken.append(codon)
             dna_codons[org] = codons_broken 
    return dna_codons

print(codon_breakage(dna)) 