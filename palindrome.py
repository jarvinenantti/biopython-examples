from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio import SeqIO
from Bio.Alphabet import generic_dna

def ispalindrome(seq, w):
    sequence = seq
    complement = sequence.reverse_complement()
    palindroms = []
    starts = []
    ends = []

    for s in range(0, len(sequence)-w):
        wind = sequence[s:s+w]
    
        for t in range(0, len(complement)-w):
            vind = complement[t:t+w]

            if str(wind) == str(vind):
                palindroms.append(str(wind))
                starts.append(s)
                ends.append(s+w)

    for i in range(0,len(palindroms)):
        print (starts[i])
        print (ends[i])
        print (sequence[starts[i]:ends[i]])

    return palindroms

seq = Seq("AGTGAATCCCGACCTAGGTAAAGTGTCTCGTA", generic_dna)
palindroms = ispalindrome(seq, 3)
