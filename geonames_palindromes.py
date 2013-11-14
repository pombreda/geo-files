import pandas as pd

pals = []
df = pd.read_csv('csv/DE.txt', sep='\t', header=None)

for n in df[1]:
    name = n.lower()
    if name == name[::-1]:
        pals.append(n)
