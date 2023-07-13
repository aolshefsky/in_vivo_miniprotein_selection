#!/usr/bin/env python
# coding: utf-8

# In[1]:


from __future__ import division
import optparse
import re
#from Bio import SeqIO
#from Bio.Seq import Seq
#from Bio.Alphabet import IUPAC
#from Bio.Alphabet import generic_dna
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


if "-h" in sys.argv or "--help" in sys.argv:
    print("Input files should be *_tt.csv files")
    print("Input files should be in this order: path, filename to be read (output of i_trim_translate_GK.py), N-term, C-term")
    print("Protein sequences from i_trim_translate_GK.py are checked for N and C termini.")
    print("The output will be a csv file containing sequences with only N and C termini. You will need to uncomment lines 153-183 if you want output files containing proteins with only N termini, only C termini, etc..")

else:
    path = sys.argv[1]
    os.chdir(path)
    filename = sys.argv[2]


    # In[3]:


    seqlist = []
    t_list = ["NXSC" , "NXC" , "NSC", "NC", "NXS","NS","NX","N", "other"]
    NXSC = []
    NXC = []
    NSC = []
    NC = []
    NXS = []
    NS = []
    NX = []
    N = []
    other = []
    temphist = {}
    hist = {}


    # In[4]:


    def sort_translations(filename):
        print("sorting sequences and making histogram", filename)
        x = open(filename,'r')
        seq = x.readlines()
        i = 1
        Nterm = sys.argv[3]
        Cterm = sys.argv[4]
        while i<len(seq):
            seq1 = seq[i]
            seqstring1 = str(seq1)
            #seqstring1 = seqstring1[3:] #get rid of ","
            if i==1:
                print(seqstring1)
            #"GGGSASHM", "LEGGGSEQK" - Nterm, Cterm
            if Nterm in seqstring1 and Cterm in seqstring1:
                #NXSC, NXC, NSC, NC conditions
                if "*" in seqstring1 and "X" in seqstring1:
                    #NXSC
                    seqlist.append(1)#seqlist[i] = 1
                    NXSC.append(seqstring1)#NXSC[i] = seqstring1
                elif "*" in seqstring1:
                    #NSC
                    seqlist.append(2)
                    NSC.append(seqstring1)
                elif "X" in seqstring1:
                    #NXC
                    seqlist.append(3)
                    NXC.append(seqstring1)
                else:
                    #NC
                    seqlist.append(4)
                    NC.append(seqstring1)
            elif Nterm[0:len(Nterm)-1] in seqstring1:
                #NXS NS NX N
                if "*" in seqstring1 and "X" in seqstring1:
                    #NXS
                    seqlist.append(5)
                    NXS.append(seqstring1)
                elif "*" in seqstring1:
                    #NS
                    seqlist.append(6)
                    NS.append(seqstring1)
                elif "X" in seqstring1:
                    #NX
                    seqlist.append(7)
                    NX.append(seqstring1)
                else:
                    #N
                    seqlist.append(8)
                    N.append(seqstring1)
            else:
                #other
                    seqlist.append(9)
                    other.append(seqstring1)
                    print(seqstring1)
            i+=1
            
        #make the histogram
        #keys will be 1-9, representing NSXC, NXC, etc. Values are frequencies.
        for j in seqlist:
            temphist[j] = temphist.get(j,0)+1
            
        #replace key labels (ex. 1 will be replaced with "NSXC", 2 with "NXC" and so on)
        count = 1
        temphistkeys = temphist.keys()
        for k in t_list:
            if count in temphistkeys:
                hist[k] = temphist[count]
            else:
                hist[k] = 0
            count +=1

    #call the method
    sort_translations(filename)
    print(hist)
    ##print(NXSC[0])
    ##print(NXSC[1])
    ##print(NXC[0])
    ##print(NXC[1])
    ##print(NSC[0])
    ##print(NSC[1])
    ##print(NC[0])
    ##print(NC[1])
    ##print(NX[0])
    ##print(NX[1])
    ##print(NS[0])
    ##print(NS[1])
    ##print(N[0])
    ##print(N[1])


    #Uncomment these to write each file, really you only need the NC sequences


    print("writing to csv")
    #with open(str(filename[:5])+"_NXSC_sequences_.csv","w") as myfile:
    #    wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
    #    wr.writerow(NXSC)
    #with open(str(filename[:5])+"_NXC_sequences_.csv","w") as myfile:
    #    wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
    #    wr.writerow(NXC)
    #with open(str(filename[:5])+"_NSC_sequences_.csv","w") as myfile:
    #    wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
    #    wr.writerow(NSC)
    with open(str(filename[:5])+"_NC_sequences.csv","w") as myfile:
        wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
        wr.writerow(NC)
    #with open(str(filename[:5])+"_NXS_sequences_.csv","w") as myfile:
    #    wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
    #    wr.writerow(NXS)
    #with open(str(filename[:5])+"_NS_sequences_.csv","w") as myfile:
    #    wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
    #    wr.writerow(NS)
    #with open(str(filename[:5])+"_NX_sequences_.csv","w") as myfile:
    #    wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
    #    wr.writerow(NX)
    #with open(str(filename[:5])+"_N_sequences_.csv","w") as myfile:
    #    wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
    #    wr.writerow(N)
    #with open(str(filename[:5])+"_other_sequences_.csv","w") as myfile:
    #    wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
    #    wr.writerow(other)
    #with open(str(filename[:5])+"_histogram_.csv","w") as myfile:
    #    wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
    #    for key, value in hist.items():
    #        wr.writerow([key,value])

