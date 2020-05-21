from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio import SeqIO
from Bio.Alphabet import generic_dna

def is_palindrome(seq):
    return str(seq)==str(seq.reverse_complement())

#Receives a sequence and will search in it for all reverse complement palindromes
#of length >= min_len and length <= max_len
def rp(seq,min_len,max_len):
    #The function rp() should return a list of positions and lengths
    #where these palindromic subsequences are found,
    #i.e. it returns [(index0,len0),(index1,len1),...]

    #Because a subsequence of a palindrome is a palindrome as well,
    #it would be wonderful if you could preserve only the longest hit.
    #I.e. do not return all the subsequences separately.
    #This is optional, but will be highly appreciated by me.

##    rev_comp = seq.reverse_complement()
    palindroms = []
    counter = 0

    for index in range(0,len(seq)):
        for window in range(max_len,min_len,-1): #Starting with the max window
            if (index + window > len(seq)): #Passing if the window goes over sequence length
                continue
            if (counter > index + window): #Avoiding to take subsequences of palindromes
                continue
            if (is_palindrome(seq[index:index+window])==True):
                palindroms.append(str(index)+","+str(window))
                counter = index + window
                    
    return palindroms   #Should return only longest hits

def pretty_print(seq,hits):
    #seq is the sequence and hits is the output of rp() for that sequence.
    #This function should then print seq on one line,
    #and on a line below it mark the hits with '*' symbols

    places = ""
    print(seq)
    indexes = [] #List of all positions of individuals in palindromes

    counter = -1
    for _ in range(0,len(hits)):
        index = int(hits[_][0:hits[_].index(',')])
        length = int(hits[_][hits[_].index(',')+1:len(hits[_])])
        for i in range(0,length):
            if (counter < index + i):
                indexes.append(index+i)
                counter = index + i


    counter = 0
    counter2 = 0
    while(len(places)<len(seq)-1):
        for _ in range(0, len(indexes)): #Parses every index of indexes
            place=(indexes[_])
            if (len(places)==len(seq)):
                break
            if (counter < place):
                counter2 = counter
                for i in range(0,place-counter2):
                    places = places + seq[len(places)]
                    counter = counter + 1
            if (counter == place):
                places = places + "*"
                counter = counter +1
            if (place > counter):
                places = places + "*"
                counter = counter +1

    print(places)
        

seq = Seq("AAATTTAAATTTAGTGAATCCCGACCTAGGTAAAGTGTCTCGTAACCTAGGT", generic_dna) #includes 'ACCTAGGT'
palindroms = rp(seq, 4, 8)
pretty_print(seq,palindroms)
