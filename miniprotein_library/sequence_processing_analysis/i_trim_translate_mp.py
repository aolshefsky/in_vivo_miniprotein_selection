#!/usr/bin/env python
# coding: utf-8

# In[1]:


from __future__ import division
import optparse
import re
from Bio.Seq import Seq
from Bio.SeqIO.FastaIO import SimpleFastaParser
from collections import Counter

#import scipy as sc
#import numpy as np
#import matplotlib.pyplot as plt
#from scipy.stats import iqr
import pandas as pd
import os
import sys
from sys import exit
import csv


# In[2]:
if "-h" in sys.argv or "--help" in sys.argv:
    print("Input files should be .fastq files")
    print("Input arguments should be in this order: path, file name, first C term overlap sequence, second C term overlap seq")
    print("Example: python i_trim_translate_GK.py /this/is/my/path filename.fastq GGCGGAGGGTCGGCTTCGCATATG,CTCGAGGGTGGAGGTTCCGAACAAAAG")
    print("Note: depnding on your sequence, you may have to manually change line 52, which depends on the length of the adapter sequence.")
else:

    path = sys.argv[1]


    #%% trim and translate assembled fastq files
    tt_list = []

    def trim_translate(readfile):
        print('trimming and translating', readfile)
        os.chdir(path)
        x = open(readfile, 'r')
        lines = x.readlines()
        i=1
        while i < len(lines):
            line1 = lines[i]
            linestring1 = str(line1)
            # C term pentamer overlap sequences that should be in every sequence. Ex: sys.argv[3] = 'GGCGGAGGGTCGGCTTCGCATATG', sys.argv[4] = 'CTCGAGGGTGGAGGTTCCGAACAAAAG'
            if sys.argv[3] in linestring1 and sys.argv[4] in linestring1:
                index1 = int(linestring1.find(sys.argv[3]))	#Change this DNA seq to be the region of your seq you want to trim on
                index2 = int(linestring1.find(sys.argv[4])) +27 #this number might change
                while (index2-index1)%3 != 0: 
                    index2 -= 1
                trimmedDNA1 = Seq(linestring1[int(index1):int(index2)])	#Change these numbers to be the number of bases you want to keep from the start of the sequence
                #while (len(linestring1[int(index1):int(index2)]) %3 !=0):
                #        index2 +=1
                #        trimmedDNA1 = Seq(linestring1[int(index1):int(index2)], generic_dna)
                protein = trimmedDNA1.translate()
                #print(protein)
                tt_list.append(protein+'\n')
            i += 4

    readfile = sys.argv[2]#"00-ds_S1_L001_assembled.assembled.fastq" #write the name of the file here
    print(readfile)
    trim_translate(readfile) 

    # pandas dataframe to csv
    print("writing to csv")
        
    with open(str(readfile[:5])+"_tt.csv", "w") as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(tt_list)
