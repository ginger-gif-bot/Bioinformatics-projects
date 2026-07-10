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

