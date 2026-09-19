"""
Week 3 — Parsing GenBank features: keyword search + sequence extraction
Goal: extract all CDS features, check product names for "efflux",
"resistance", or "pump", and print the actual sequence for each match.
"""

from Bio import Entrez,SeqIO
Entrez.email = "your.email@example.com"  # replace with your own email before running

handle = Entrez.efetch(db="nucleotide",id="NZ_CP102533.1", rettype="gbwithparts", retmode="text")
record = SeqIO.read(handle,"genbank")
handle.close()
print("RECORD ID: ",record.id)
print("RECORD DESCRIPTION: ",record.description)

# --- Step 1: filter down to just CDS features ---
cds_features = []
for features in record.features:
    if features.type == "CDS":
        cds_features.append(features)
print("Number of annotated CDS features:",len(cds_features))

# --- Step 2: check each CDS's product name against three keywords ---
keywords = ["efflux","pump","resistance"]
matches = []
for cds in cds_features:
    if "product" in cds.qualifiers: #pulling out the "product" name safely 
        product_name = cds.qualifiers["product"][0] #If yes, grab the actual text (the [0] because it's stored as a list)
    else:
        product_name = ""
    matched_keyword = [] #checking that product name against all three keywords:
    for keyword in keywords:
        if keyword in product_name.lower():
            matched_keyword.append(keyword) #If none of the three are found, this list simply stays empty ([]).
    if len(matched_keyword) > 0: #finally append to original matches list at the top
        matches.append({"cds": cds, "product": product_name, "matched_keyword": matched_keyword})
print("Number of matching CDS features found:",len(matches))

# --- Step 3: extract and print the actual sequence for each match ---
for match in matches:
    sequence = str(match["cds"].extract(record.seq))
    print("Product:", match["product"])
    print("Matched keyword:", match["matched_keyword"])
    print("Sequence length:", len(sequence))
    print("Sequence:", sequence)
    print("---")