from __future__ import division
import random
import math
#alternatives:
#from random import choice
#from random import *


## TASK 1:
##
## modify the function below such that it takes a third parameter,
## which is a list of probabilities corresponding to the letters of
## the alphabet so rnd_seq(5,"acgt",[0.0,0.5,0.25,0.25]) should
## generate a random sequence of length 5, which has no a's and on
## average about half c's, quarter g's, quarter t's. The probabilities
## of course sum up to 1, so you can assume this in your solution.
##
## TASK 2:
##
## Write a function rnd_seq_matrix(l,alphabet,M) where M is a matrix
## of NxN probabilities (where N is the number of characters in the
## alphabet). The matrix is simply a list of lists. Every row in the
## matrix corresponds to one letter in the alphabet and specifies the
## probability distribution of the next letter.
##
## So calling rnd_seq_matrix(10,"ac",[[0.5,0.5],[0.95,0.05]]) would generate strings
## such that every a is followed by a or c with 50:50 chance, but a c is very unlikely
## to be followed by another c.

def rnd_seq(length,alphabet,possibilities): #write a third parameter
    """Generates a random sequence of length 'length' drawn from alphabet"""

    #One-liner version:
##    return "".join([random.choice(alphabet) for _ in range(length)])
    #Longer version of same:

    seq=""            

    while len(seq) < length:
        r = random.random() #Return the next random floating point number in the range [0.0, 1.0).
        ri = random.randint(0,len(alphabet)-1) #Random int 0<ri<len(alphabet)-1
        if possibilities[ri] > r: #Possibility of single alphabet
##              seq+=random.choice(chance)
            seq+=alphabet[ri] #Adding that alphabet to seq

    return seq

def rnd_seq_matrix(length,alphabet,M):
    """Generates strings accodring to possibilities of matrix M"""

    seq=""
    ri = random.randint(0,len(alphabet)-1)
    seq+=alphabet[ri]   #adding first random alphabet to str

    while len(seq) < length:
        r = random.random() #Return the next random floating point number in the range [0.0, 1.0).
        lastCharacter = seq[len(seq)-1] #Last char of str
        place = alphabet.index(lastCharacter) #Place of that last char
        ri = random.randint(0,len(alphabet)-1) #Random int 0<ri<len(alphabet)-1
        if M[place][ri] > r: #Possibility of single alphabet
            seq+=alphabet[ri] #Add alphabet to seq
            
    return seq
    
    

## TASK 3:
##
## Modify the function below to get rid of the parameter w, i.e. you don't care what the
## length of the subsequence is. This will lead to the problem that a single c or g
## have 100% GC content, so you will be getting degenerate solutions. You need to find a way
## to balance the GC content and the length. Be creative in how you approach that. Some possible
## directions were shown on the lecture.

def max_gc_area(seq,w):
    pass
    """Finds the subsequence of seq of length w which has the highest GC content.
    In case there are several subsequences with the same GC content, returns the first one"""
    max_gc=None
    max_i=None
    for i in range(len(seq)-w+1):
        sub_seq=seq[i:i+w]
        gc=(sub_seq.count("g")+sub_seq.count("c"))/w
        if max_gc is None or gc>max_gc:
            max_gc=gc
            max_i=i
    assert max_gc is not None
    return max_i

def max_gc_area(seq):   # Define ratio from length to points
    """Finds the subsequence of seq of highest GC content.
    In case there are several subsequences with the same GC content, returns the first one"""
    max_gc=None
    max_i=None
    width=1
    window=0
    for i in range (len(seq)):
        #Tests every subseq place of the sequence
        for width in range (len(seq)- i):
            #Tests every window of the place
            sub_seq=seq[i:i+width]  #[i:i+width] this is the window
            gc=float(sub_seq.count("g")+sub_seq.count("c")-(sub_seq.count("a")+sub_seq.count("t"))*1.5)   #g+c-(t+a)*1.5
            if max_gc is None or gc>max_gc: #install best gc and the place and the window
                max_gc=gc
                max_i=i
                window=width
    assert max_gc is not None
    print(max_i)
    return seq[max_i:max_i+window]   #return gc-seq

def percentContent(seq):
    """Returns the percentage of g or c in sequence"""
    gc=0
    for i in range (len(seq)):
        if seq[i]=='g' or seq[i]=='c':
            gc+=1
    return str(gc/len(seq)*100) + "% of 'g' or 'c'"


s=rnd_seq(100,"acgt",[0.25,0.25,0.25,0.25])+"cccca"
print (s)

print ("\n")

t=rnd_seq_matrix(30,"ac",[[0.5,0.5],[0.95,0.05]])
print (t)

print("\n")

u=max_gc_area(s)
print(u)
print(str(len(u))+" = length of gc seq")
content = percentContent(u)
print (content)


        

