#ReadMe
#1  save as excel worksheet - otherwise (CSV, CSV-DOS, etc.) a warning will throw, so might as well not reformat.
#2  If output excel sheet is open, and you try to run script again, error 'No13 - Permission Denied' will be thrown

#import libraries
import pandas as pd
import os
from collections import Counter
import stringdist as sd
import jellyfish as jlfsh
import itertools

#show current directory and files in current directory
os.chdir(r"C:\Users\prozehnal\Desktop\csv_house\csv") #changes to correct directory from absolute reference
print(os.getcwd(),'<--current directory') #prints current directory to ensure you're in the right folder
print(os.listdir(os.getcwd()),'<----files in current dir') #lists files in current directory
print('\n\n')

#input -> output data manipulation
inp_data= pd.read_csv('db1.csv',usecols=[0],verbose=False) #potentially useful: skipinitialspace, squeeze,verbose
inp_data=inp_data["Features"].tolist()

i_l=[]
for i in inp_data:
    i=i.split()
    i_l.append(i)
# print(i_l)
# print('000',inp_data)
# print('111',i_l)
# flat_l=[item  for sublist in i_l for item in sublist] #
# print(222,flat_l)

temp_l=[] #temp holds soundex values to match length of elements, so each element is soundexed.
combined_l=[] #sublist of combined string and soundex.
soundex_l=[]
# print(i_l,i_l[0])
for i in i_l:
    for element in range(len(i)):
        jellied = jlfsh.soundex(i[element])
        temp_l.append(jellied)
        if len(temp_l)==len(i):
            soundex_l.append(temp_l)
            combined_l.append(i)
            combined_l.append(temp_l)
            temp_l=[]

# print(len(soundex_l),soundex_l)
# print(len(i_l),i_l)
# print(len(combined_l),combined_l)
def flattener(ilist):
    o=[]
    for i in ilist:
        j= " ".join(i) #join replaces commas with " " j = i.replace(',',' ') DOES not work, i believe replace only works within a string, rather than between strings. #str.replace == str.split().join()
        # print(j)
        o.append(j)
    return o
inp_flat=flattener(i_l)
# print(1231231,flattener(i_l))
sound_flat=flattener(soundex_l)
# print(999,flattener(soundex_l))

################################# print(dir(dict()))
hashmap = {}
print(type(hashmap))
for i in range(len(soundex_l)): #soundex_l and all the others all have the same lengths.
    hashmap.update({inp_flat[i]:sound_flat[i]}) #damn colon gave me issues

for k,v in hashmap.items():
    print (k,'and',v)

for a in hashmap.keys():
    print (a)

for b in hashmap.values():
    print (b)




#
#
# for i,k in hashmap:
#     print(i,k)
