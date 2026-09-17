"""
Week 3, Day 1 (Tue Sep 15) — Biopython: Entrez ESearch
Goal: Search NCBI's nucleotide database for "Lactobacillus acidophilus 16S rRNA"
and find:
    1. Total number of matching sequences (record["Count"])
    2. The first 10 matching IDs (record["IdList"])

Notes:
- esearch only returns IDs, not the actual sequence data — that's efetch's job.
- Default ID format is numeric UID (NCBI's internal ID).
  Adding idtype="acc" instead returns human-readable accession numbers
  (e.g. 'NZ_OZ543480.1') — a completely separate identifier for the same
  record, not just a different display of the same number.
- Entrez.email is required before any call; Entrez.read() only works on
  XML output, which is what esearch always returns.
"""

from Bio import Entrez
Entrez.email = "your.email@example.com"  # replace with your own email before running
handle = Entrez.esearch(db="nucleotide", term="Lactobacillus acidophilus 16S rRNA", retmax=10,idtype="acc")
record = Entrez.read(handle)
handle.close()
print("Total sequences found:",record["Count"])
print("First 10 IDs:",record["IdList"])