def gc_area(sequence,window):
    index=0
    gc_max=0.0
    for i in range(len(sequence)):
        if (i+window) <= len(sequence):
            gc_pro = gc_content(sequence[i:i+window])
            if gc_pro > gc_max:
                gc_max = gc_pro
                index = i
    print("Sequence is", sequence, "and window length is:", window)
    print("best substring:", sequence[index:index+window],"with gc content:", gc_max)
    return sequence[index:index+window]
