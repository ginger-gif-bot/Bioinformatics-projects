dna = "ATGC"
complement = {"A":"T",
              "T":"A",
              "G":"C",
              "C":"G"}

def reverse_comp(seq):
    comp = ""
    for base in dna:
        comp_base = complement.get(base)
        comp += comp_base
        rev_comp = comp[::-1]

    print(f"Original DNA: {dna}")
    print(f"Complementary DNA: {comp}") 
    print(f"Reverse Complement DNA: {rev_comp}")

reverse_comp(dna)


