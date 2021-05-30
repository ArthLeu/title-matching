

def search_sentences(label, text, pre=5, post=4):
    ''' KMP algorithm in text and return k words before and after matches '''
    
    pos = KMP(label, text)
    m = len(label)
    n = len(text)
    pre += 1
    activations, deactivations = [], []
    terminators = [" ", "\n"]
    pauses = ['.', ',']

    for p in pos:
        if p >= 2 and text[p-2] in pauses:
            beg = p-2
        else:
            beg = p
            c = 0
            while beg >= 0:
                if text[beg] == ".":
                    c = pre
                elif text[beg] in terminators:
                    c += 1

                if c == pre:
                    beg += 1
                    break
                else:
                    beg -= 1
        
        if p+m <= n-1 and text[p+m] in pauses:
            end = p+m
        else:
            end = p+m+1
            c = 0

            while end < n:
                if text[end] == ".":
                    c = post
                elif text[end] in terminators:
                    c += 1
                
                if c == post:
                    break
                else:
                    end += 1

        activations.append(text[beg:p-1])
        deactivations.append(text[p+m:end])

    return activations, deactivations


# Python program for KMP Algorithm
def KMP(pat, txt):
    M = len(pat)
    N = len(txt)
    IDX = []
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
  
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            IDX.append(i-j)
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    
    return IDX

def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1



def consecutive_caps(text):
    pass


if __name__ == "__main__":
    txt = "ABABDABACDABABCABAB"
    pat = "ABAB"
    KMP(pat, txt)