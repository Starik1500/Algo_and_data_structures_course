def pattern_search(haystack, needle):
    comparisons = 0 
    last_index = -1  
    
    for idx in range(len(haystack) - len(needle) + 1):
        match = True
        for i in range(len(needle)):
            comparisons += 1
            if haystack[idx + i] != needle[i]:
                match = False
                break
        if match:
            last_index = idx

    return last_index, comparisons

if __name__ == "__main__":
    haystack = "AABAACAADAABAABA"
    needle = "AABA"
    last_index, comparisons = pattern_search(haystack, needle)
    print("Last index:", last_index)
    print("Number of comparisons:", comparisons)
