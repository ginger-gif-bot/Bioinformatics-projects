import sys

if len(sys.argv) <2:
    print("Error")
    sys.exit()
file = sys.argv[1]

with open(file,"r") as f:
    data = f.read()
print(f"The contents of the file are: \n{data}")

dna = []
for i in data.split():
    if i.startswith("seq"):
        continue
    dna.append(i)
print(f"The sequences in the file are: \n{dna}")

g_count = {}
for i in data.splitlines():
    name, seq = i.split()
    g_count[name] = seq.count("G")   
print(g_count) 

with open("result.txt","w") as f:
    f.write(str(dna))
    f.write("\n")
    for name, count in g_count.items():
     f.write(f"{name}\t{count}\n")