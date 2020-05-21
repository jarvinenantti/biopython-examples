"""Gene TP53, human, grab the record of the protein associated
with the gene TP53 in human"""
##Take query '(human[Organism]) AND tp53[Gene Name]' and run through ncbi records
##Use eutilities
##equery first (usehistory = "y")
##efetch second
##=> get XML
##use parser
##=> python object
##esearch
##epost, upload list of IDs => makes URL

from Bio import Entrez
Entrez.email = "_@_.com"

handle = Entrez.esearch(db="protein", term="(human[Organism]) AND tp53[Gene Name] ", usehistory = "y", retmax = 100) #alternatively post
result = Entrez.read(handle)
print result
##print result["IdList"][0]
webenv = result["WebEnv"]
query_key = result["QueryKey"]
print webenv
print query_key
N = 20
for i in range(0,len(result["IdList"]),N):
    fetch_handle = Entrez.efetch(db="protein",rettype="fasta", retmode="text", retstart=i, retmax=20, webenv=result["WebEnv"], query_key=result["QueryKey"])
    data = fetch_handle.read()
    out_handle = open("efetched100.txt","a")
    out_handle.write(data)
fetch_handle.close()
out_handle.close()
out_handle = open("efetched100.txt","r")
print len(out_handle.readlines())
out_handle.close()
