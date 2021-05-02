import os
import numpy
import matplotlib.pyplot as plt

import LCS
import json
import time


def main():
    ''' this is the main function '''
    dict = {}
    # PART 01: preprocess the documents
<<<<<<< HEAD
    
=======
    file = open('0a2c7004-f763-4846-b95f-1fdf537f8a04.json', 'r')
    doc = json.load(file)

    beginning = time.time()

    for section in doc:
        section_body = section['text']
        matching_string = LCS.LongestCommonSubstring(section_body, '2010')
        if matching_string not in dict:
            dict['0a2c7004-f763-4846-b95f-1fdf537f8a04'] = matching_string[0]

        print(dict)
    endtime = time.time()
    print(endtime-beginning)
>>>>>>> e3f25d3b6f3d1750f1de554affa79dda5f9d733f

    # PART 02: run matching algorithms in each document
    

    # PART 03: output statistics

    pass


if __name__ == "__main__":
    main()
