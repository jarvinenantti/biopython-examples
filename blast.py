from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio.Blast import NCBIXML
import  xml.etree.cElementTree as ET

# ### THE TASK:

# We are back to the example in the KNN topic.
# This time, the idea is to run the sequences
# from bac_vs_hum_test.vw through BLAST
# and establish the source organism like that.
# So we want to go through the file,
# one sequence at a time, blast it, and dig the organism out.

# The simpler (but MUCH slower) way will be to run blast online.
# The other way will be run blast locally,
# as I showed in the lecture.

# Please finish this program until you are able to verify
# that the organism hits are indeed correct, ie
# that whenever a line in the .vw file has "-1" as the class,
# you successfully identify the sequence
# as EColi and whenever it says "1", you identify it as a human.

# Have fun!

#local_blast() and online_blast() do same thing, but through different means


def vwToFasta(f_name, N):
    handle = open(f_name,"r")
    new_file = open("newFile.fasta","a")
    index = 1

    for line in handle.readlines():
        if index == N:
            index_xs = line.find("|")
            new_file.write(line[index_xs+2:-1])
            break
        index = index + 1
    
    handle.close()
    new_file.close()

def remoteBlast(f_name):
    fasta_string = open(f_name).read()
    result_handle = NCBIWWW.qblast("blastn", "nr", fasta_string)

    save_file = open("remote_blast.xml", "w")
    save_file.write(result_handle.read())
    save_file.close()

def findType(f_name):
    orgtype = ""
    with open(f_name,"r") as f:
        for line in f.readlines():
            index = line.find("<")
            if line[index:index+9] == "<Hit_def>":
                orgtype = line.split( )[0:2]
                orgtype = orgtype[0][9:len(orgtype[0])] + " " + orgtype[1]

                if orgtype == "Escherichia coli" or orgtype == "Homo sapiens":
                    break
                else:
                    continue
    return orgtype

def getNumber(f_name, N):
    handle = open(f_name,"r")
    number = ""
    index = 1
    for line in handle.readlines():
        if index == N:
            number = line.split( )[0]
            break
        index = index + 1

    handle.close()
    return number

def compare(orgType, number):
    if orgType == "Escherichia coli" and number == "-1":
        print "Correct result"
        print "Specie is: " + orgType
    elif orgType == "Homo sapiens" and number == "1":
        print "Correct result"
        print "Specie is: " + orgType
    else:
        print "Didn't find the right result"
        print orgType
        print number

def find_org(f_name, N):
    vwToFasta(f_name, N)
    remoteBlast('newFile.fasta')
    orgType = findType('remote_blast.xml')
    print orgType
    number = getNumber(f_name, N)
    print number
    compare(orgType, number)
    
N = 1 #Define the seq you are examining
find_org('bac_vs_hum_test.vw', N)
