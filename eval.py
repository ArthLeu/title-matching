import os
import time
import numpy


def jaccard(str1, str2): 
    ''' order of input arguments (ground truth, predicted string) does not matter '''
    a = set(str1.lower().split()) 
    b = set(str2.lower().split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


def prepare_ground_truth(gt_path = "dataset/train.csv"):
    ''' Input: ground truth path. Output: Python container for ground truth '''
    pass


def evaluate(predictions):
    ''' Input: predictions from main. Output: precision and recall values (displayed) '''
    # for each publication

    # compute Jaccard score using ground truth and predicted strings

    # categorize J-scores using beta threshold (default = 0.5)
    # TP if J-score >= 0.5, FP otherwise; unmatched predictions -> FP; Ground truth with no match -> FN.

    # calculate precision: TP / (TP+FP)

    # calculate recall: TP / (TP+FN)

    pass


if __name__ == "__main__":
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    
    # test script for eval.py below

