# -*- coding: utf-8 -*-


import pycantonese as pc
import csv


corpus = pc.hkcancor()
hkcancorFreq = corpus.word_frequency()


with open('hkcancorFrequency.csv', encoding='utf-8', mode='w', newline='') as csvfile:
    writer=csv.writer(csvfile)
    for key, value in hkcancorFreq.items():
        writer.writerow([key, value]) 




sun = pc.read_chat('../00-source/sun_1924_tagged.cha')
sun.word_frequency()
sunFreq = sun.word_frequency()



with open('sunFrequency.csv', encoding='utf-8', mode='w', newline='') as csvfile:
    writer=csv.writer(csvfile)
    for key, value in sunFreq.items():
        writer.writerow([key, value]) 
