import time
import numpy as np

def LongestCommonSubstring(document, phrase):
    ''' input: document (str), phrase to match (str); output: longest matching substring '''
    m = len(document) + 1 # add 1 because the first row/col is for when substring length is 0
    n = len(phrase) + 1
    T = np.zeros([m, n]) # DP table
    maxlen = 0
    argmaxstr = ""

    for i in range(1, m):
        for j in range(1, n):
            if document[i-1] == phrase[j-1]: # subtract 1 because the index of doc/phrase is still 0-based
                T[i, j] = T[i-1, j-1] + 1
            else:
                T[i, j] = 0

            # update record
            if T[i, j] > maxlen:
                maxlen = int(T[i, j])
                argmaxstr = phrase[j-maxlen:j]

    # finalize results
    #print("longest substring:", argmaxstr)
    #print("length:", maxlen)

    return (argmaxstr, maxlen)


if __name__ == "__main__":
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)

    LongestCommonSubstring("abcdefg", "cdea")
