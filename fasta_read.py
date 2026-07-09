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
