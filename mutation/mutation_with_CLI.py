from tabulate import tabulate
import sys

if len(sys.argv) <2:
   print("Error:Please provide all files")
   sys.exit()

data_dna = sys.argv[1]

with open(data_dna,"r") as f:
   data = f.read()

def clean_data(fasta_seq):
    cleaned_data = {}
    for i in fasta_seq.splitlines():
        if i.startswith(">"):
            current_seq = i[1:]
        else:
            cleaned_data[current_seq] = i
    return cleaned_data
dna = clean_data(data)

def length_of_seq(dna_dict):
    length = {}
    for org, seq in dna_dict.items():
        length[org] = len(seq)
    return length

def gc_content(dna_dict):
    gc_content = {}
    for org, seq in dna_dict.items():
        value = round(((seq.count("G") + seq.count("C"))/len(seq))*100,2)
        gc_content[org] = value
    return gc_content

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
             syn.append((frame,f"{cod_a} -> {cod_b}",f"{aa_a} -> {aa_b}"))
          else:
             nsyn.append((frame,f"{cod_a} -> {cod_b}",f"{aa_a} -> {aa_b}"))
   return syn, nsyn        

def make_report(clean_dna_dict):
   codons = codon_breakage(clean_dna_dict)
   # flat dictionaries
   ## length of sequences table
   length = length_of_seq(clean_dna_dict)
   rows_len = [[org,val] for org,val in length.items()]
   table_len = tabulate(rows_len,headers=["Organisms","Length"],tablefmt="grid")

   ## GC content table
   gc = gc_content(clean_dna_dict)
   rows_gc = [[org,val] for org,val in gc.items()]
   table_gc = tabulate(rows_gc,headers=["Organisms","GC percentage"],tablefmt="grid")
  
   # nested dictionaries
   ## Codon table
   rows_codon = []
   for frame, info in codons.items():
      for org, cods in info.items():
         rows_codon.append([frame,org,cods])
   table_codon = tabulate(rows_codon,headers=["Frame","Organism","Codons"],tablefmt="grid")
         
    # translation table
   translation_aa = translation(codons)
   rows_aa = []
   for frame, info in translation_aa.items():
      for org, aa in info.items():
         rows_aa.append([frame,org,aa])
   table_aa = tabulate(rows_aa,headers=["Frame","Organism","Amino Acid Sequence"],tablefmt="grid")    
    
    # list of tuples
    ## Mutation table
   syn,nsyn = mutations(codons,"human","mouse")
   syn_table = tabulate(syn,headers=["Frame","Codon Change","Amino Acid Change"],tablefmt="grid")
   nsyn_table = tabulate(nsyn,headers=["Frame","Codon Change","Amino Acid Change"],tablefmt="grid")
   
    # writing everything in a file
   with open("results.txt","w") as f:
      f.write("GC Content:\n"+ table_gc)
      f.write("\n\nLength of the Sequences:\n" + table_len)
      f.write("\n\nCodons by Frame:\n" + table_codon)
      f.write("\n\nAmino Acids (Translation) by Frame:\n" + table_aa)
      f.write("\n\nSynonymous Mutations:\n" + syn_table)
      f.write("\n\nNon-synonymous Mutations:\n" + nsyn_table)
make_report(dna)

print("Done!!")


    
   