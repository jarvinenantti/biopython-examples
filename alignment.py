"""Informative sites (submit finished program)

The task was to read a multiple sequence alignment
and produce a new multiple sequence alignment
which has only the informative sites from the point of view
of the maximum parsimony criterion in phylogenetics.
If you have no clue what that is, check it out here:
http://www.icp.ucl.ac.be/~opperd/private/parsimony.html#informative

So, once again - alignment in - filtered alignment out.
You can use the alignment file in the example programs and data as your test case."""

from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment

def readAlign(f_name):
    handle = open(f_name)
    alignment = AlignIO.read(handle, "clustal")
    print "Alignment length %i" % alignment.get_alignment_length()
    print "Alignment:"
    for record in alignment :
        print "%s - %s" % (record.seq, record.id)

    handle.close()

    return alignment

def inforSites(alignment):
    character = ""
    counter = 0
    edited = alignment[:, 1:2]
    start = 0

    for i in range (alignment.get_alignment_length()):
        column = str(alignment[:, i])
        character = column[0]
        counter = 0
        for j in range (len(column)-1):
            if str(column[j+1]) != character:
                character = column[j+1]
                counter+=1
                if counter == 1:
                    start = j
                
        #A site is informative only when there are at least
        #two different kinds of nucleotides at the site,
        #each of which is represented in at least
        #two of the sequences under study.        
        if counter == 1 and start != 0 and start != 5:
            edited = edited + alignment[:, i:i+1]
        if counter > 1:
            edited = edited + alignment[:, i:i+1]

    edited = edited[:, 1:]
    print edited
    return edited

def handleAlign(f_name):
    seqs = readAlign(f_name)
    infor = inforSites(seqs)
    AlignIO.write(infor, "informative_sites.aln", "clustal")

handleAlign('opuntia.aln')
