import os
import numpy
#import matplotlib.pyplot as plt
import json
import time

import LCS


# Global Variables
DATASET_LABEL = "NOAA" # TEMP: single exact match
print("Searching dataset label:", DATASET_LABEL)
LMKS = [i for i in range(101) if i % 5 == 0] # landmarks for printing progress
DATA_LIMIT = 1000


def print_progress(i, total):
    global LMKS 
    percent = round(i/total*100)
    
    if LMKS != [] and percent == LMKS[0]:
        print("%d%% completed"%percent)
        LMKS.pop(0)

        
def main():
    ''' this is the main function '''

    PredictionDict = {}
    begintime = time.time()
    
    # PART 01: Preprocess the documents
    
    train_data_path = "dataset/train"
    train_list = os.listdir(train_data_path)
    train_list = train_list[:DATA_LIMIT] # TEMP
    total_train_count = len(train_list)

    for i, filepath in enumerate(train_list):
        print_progress(i, total_train_count)
        
        file = open(train_data_path + filepath, 'r')
        id = filepath.split(".")[0] # remove .json filename extension
        doc = json.load(file)


    # PART 02: Run matching algorithms in each document
    
        for section in doc:
            section_text = section['text']

            # TODO: Matching algorithms below

            #matching_string = DATASET_LABEL if DATASET_LABEL in section_text else "None"  # Hack for exact match (using this instead can humiliate me)
            matching_string = LCS.LongestCommonSubstring(section_text, DATASET_LABEL)[0]
            
            if matching_string not in PredictionDict and matching_string == DATASET_LABEL: # == for exact match
                PredictionDict[id] = matching_string

            # Matching algorithm ends here

    # PART 03: Output statistics
    
    endtime = time.time()
    print("\nTotal: %.2f seconds"%(endtime - begintime))
    

    # TEMP: TEST SCRIPTS
    test_keys = PredictionDict.keys()
    print("Searched %d documents."%total_train_count)
    print("Found keys in %d documents, showing first 10.\n"%len(test_keys))
    print("Id, PredicitonString")
    for i in range(min([10, len(test_keys)])):
        k = list(test_keys)[i]
        print("%s, %s"%(k, PredictionDict[k]))


    return 0



if __name__ == "__main__":
    main()
