def gc_content(substring): #percentage 0.0-1.0
    count_cg = float(substring.count('g'))+float(substring.count('c'))
    return count_cg/float(len(substring))
