"""
Week 3, Day 2 (wed Sep 16) — Biopython: Entrez EFetch
------------------------------------------------------
Goal: Download 5 Lactobacillus 16S rRNA sequences (IDs from yesterday's
esearch) and save them as one local FASTA file: lactobacillus_16S.fasta
"""

from Bio import Entrez
Entrez.email = "your.email@example.com"  # replace with your own email before running
id_list = ["NZ_OZ543480.1", "NZ_OZ543876.1", "NZ_OZ544144.1", "NZ_OZ543289.1", "NZ_OZ543288.1"]
handle = Entrez.efetch(db="nucleotide", id=",".join(id_list), rettype="fasta", retmode="text")
data = handle.read()
handle.close()
with open ("lactobacillus_16S.fasta","w") as file:
    file.write(data)
print("Saved 5 sequences to lactobacillus_16S.fasta")