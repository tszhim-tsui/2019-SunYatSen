# -*- coding: utf-8 -*-


import pandas as pd

cancor = pd.read_csv("../01-frequency/hkcancorFrequency.csv", header=None)
cancor.head()

sun= pd.read_csv("../01-frequency/sunFrequency.csv", header=None)
sun.head()

#check
type(sun)

cancor.columns = ["word", "freq"]
sun.columns = ["word", "freq"]


#check
sun.word
sun.freq
cancor.word

type(sun.word)


# sort
#cancor = cancor.sort_values(by=["freq"], ascending=False)
#sun = sun.sort_values(by=["freq"], ascending=False)

# 1. what appears more then usual
# 2. what words appear in Sun but not in Cancor
# 3. where do sun words appear in the sorted cancor frequency


#149781
cancor.freq.sum()

#613
sun.freq.sum()


#Add relative frequency
cancor["relfreq"] = list(cancor.freq/149781)
sun["relfreq"] = list(sun.freq/613)


#make a new dataframe
comb = sun



#check
comb.word[0]

cancor.loc[cancor["word"] == comb.word[0]]
cancor.loc[cancor["word"] == comb.word[0]].freq
cancor.loc[cancor["word"] == comb.word[0]].relfreq



# references
# https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
# https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/






#Set up new list
cancorfreq = []
#run through each word in SunYatSen
for i in comb.word:
    #if word doesn't appear in cancor
    if cancor.loc[cancor["word"] == i].empty == True:
        #insert "0" as frequency
        cancorfreq.append(0)
    #Othewise
    else:
        #append frequency to list
        cancorfreq.append(cancor.loc[cancor["word"] == i].freq.array[0])

cancorfreq


# same for relative frequency
cancorrelfreq = []
for i in comb.word:
    #if word doesn't appear in cancor
    if cancor.loc[cancor["word"] == i].empty == True:
        #insert "0" as frequency
        cancorrelfreq.append(0)
    #Othewise
    else:
        #append frequency to list
        cancorrelfreq.append(cancor.loc[cancor["word"] == i].relfreq.array[0])
cancorrelfreq


comb["cancorfreq"] = cancorfreq
comb["cancorrelfreq"] = cancorrelfreq


comb.head()
comb.to_csv("combined.csv")







