import time
import numpy as np
from numba import jit

@jit # Numba compilation decorator
def LongestCommonSubstring(document, phrase):
    ''' input: document (str), phrase to match (str); output: longest matching substring '''
    m = len(document) + 1 # add 1 because the first row/col is for when substring length is 0
    n = len(phrase) + 1
    T = np.zeros((m, n)) # DP table. (m, n) is a tuple for Numba
    maxlen = 0
    argmaxstr = ""

    for i in range(1, m):
        for j in range(1, n):
            
            localoptima = 0
            if document[i-1] == phrase[j-1]: # subtract 1 because the index of doc/phrase is still 0-based
                localoptima = T[i-1, j-1] + 1

            T[i, j] = localoptima

            # Update record
            if localoptima > maxlen:
                maxlen = int(localoptima)
                argmaxstr = phrase[j-maxlen:j]

    # Finalize results
    return (argmaxstr, maxlen)


if __name__ == "__main__":
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)

    res = LongestCommonSubstring("abcdefg", "cdea")
    print("common string \"%s\" of length %d"%res)
