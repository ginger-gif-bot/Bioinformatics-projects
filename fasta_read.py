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
print(seq)

gc_content = {}
for name, sequence in seq.items():
    try:
     gc_content[name] = round(((sequence.count("G") + sequence.count("C"))/len(sequence)*100),2)
    except ZeroDivisionError:
        print("The length of the sequence is zero.") 
print(gc_content)