"""
Week 3 — GenBank format: gene features and efflux search
Goal: fetch a Lactobacillus GenBank record, count annotated genes,
check if any are efflux-related.
"""

from Bio import Entrez,SeqIO
Entrez.email = "your.email@example.com"  # replace with your own email before running
handle = Entrez.efetch(db="nucleotide", id="NZ_CP102533.1", rettype="gbwithparts", retmode="text")
record = SeqIO.read(handle,"genbank")
handle.close()
print("RECORD ID: ",record.id)
print("RECORD DESCRIPTION: ",record.description)

#The first loop had exactly one job: "out of every feature on this record — 
# genes, CDS, source, everything — keep only the ones that are actually genes."
genes = []
for feature in record.features:
    if feature.type == "gene":
        genes.append(feature)
print("Number of annotated genes: ",len(genes))


cds_features = []
for feature in record.features:
    if feature.type == "CDS":
        cds_features.append(feature)

print("Number of annotated CDS features:", len(cds_features))

efflux_products = []
for cds in cds_features:
    if "product" in cds.qualifiers:
        product_name = cds.qualifiers["product"][0]
    else:
        product_name = ""

    if "efflux" in product_name.lower():
        efflux_products.append(product_name)

print("Efflux-related products found:", efflux_products)

"""
.type == "gene" — a short label/ID tag. Qualifiers mainly hold "gene" 
(the cryptic short name, like gyrA) and "locus_tag". No description field.

.type == "CDS" — the protein-coding entry. Qualifiers hold richer info,
 including "product" — a full plain-English description (e.g. "multidrug efflux MFS transporter").
 """