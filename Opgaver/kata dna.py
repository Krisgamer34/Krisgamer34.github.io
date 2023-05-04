dna = "ATTGC"

s = dna
d = dna

    
if "A" in dna:
    s = dna.replace("A","T")
    
if "T" in dna:
    s = d.replace("T","A")
    
if "G" in dna:
    s = dna.replace("G","C")
    
if "C" in dna:
    s = d.replace("C","G")

print(s)