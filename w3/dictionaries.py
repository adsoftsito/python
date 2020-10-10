nucleotidos = {"A":"Adenina", "C": "Citosina", "G":"Guanina", "T":"Timina" }

print len(nucleotidos)
print nucleotidos

print nucleotidos["A"]
print nucleotidos["C"]
print nucleotidos["G"]
print nucleotidos["T"]

nucleotidos["A"] = "ADENINA"
print nucleotidos
nucleotidos.pop('T', None)
print nucleotidos
