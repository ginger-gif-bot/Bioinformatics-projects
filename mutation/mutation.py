with open("dna.fasta","w") as f:
    f.write(">human\n")
    f.write("ATGCTGACATA\n")
    f.write(">mouse\n")
    f.write("ATGTTGACAGA")

with open("dna.fasta","r") as f:
    data = f.read()

print(data)


    