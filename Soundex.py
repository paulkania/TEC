#ReadMe
#1  save as excel worksheet - otherwise (CSV, CSV-DOS, etc.) a warning will throw, so might as well not reformat.
#2  If output excel sheet is open, and you try to run script again, error 'No13 - Permission Denied' will be thrown


#import libraries
import pandas as pd
import os
from collections import Counter
import stringdist as sd
import jellyfish as jlfsh

#show current directory and files in current directory
os.chdir(r"C:\Users\prozehnal\Desktop\csv_house\csv") #changes to correct directory from absolute reference
print(os.getcwd(),'<--current directory') #prints current directory to ensure you're in the right folder
print(os.listdir(os.getcwd()),'<----files in current dir') #lists files in current directory
print('\n\n')

#input -> output data manipulation
inp_data= pd.read_csv('seo.csv',usecols=[0],verbose=False) #potentially useful: skipinitialspace, squeeze,verbose
inp_data=inp_data["Features"].tolist()

print('000',inp_data)
i_l=[]
for i in inp_data:
    i=i.split()
    i_l.append(i)

print('111',i_l)
flat_l=[item for sublist in i_l for item in sublist]
print(222,flat_l)

temp_l=[]
combined_l=[]
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

# for i,j in zip(range(0,len(soundex_l)-1), range(1,len(soundex_l))):
#     # print(i,j,soundex_l[i],soundex_l[j],len(soundex_l[i]),len(soundex_l[j]))
#     # if len(soundex_l[i]) != len(soundex_l[j]):#probably not strictly necessary
#     for el in range( min(len(soundex_l[i]), len(soundex_l[j]))):
        # print(inp_data[i],'&',inp_data[j],soundex_l[i][el],soundex_l[j][el],'thund3r')
        #print('ld',jlfsh.damerau_levenshtein_distance(soundex_l[i][el], soundex_l[j][el]))
        #print('jaro',jlfsh.jaro_distance(soundex_l[i][el], soundex_l[j][el]))
        # print('hamming',jlfsh.hamming_distance(soundex_l[i][el], soundex_l[j][el]))
        # print()
#what I'm seeing is that the soundex tokens aren't good indicators of similarity.
#therefore i'll move on, look at the notebook and see what's good.
#maybe i'll try to amalgamate these to programs.
#where it was useful was below..in accounting for special characters.

# print(123,soundex_l)

for i,j in zip(range(0,len(soundex_l)-1), range(1,len(soundex_l))):
    print(soundex_l[i],soundex_l[j])
    # if soundex_l[i]==soundex_l[j]:
    #     # print(soundex_l[i],'&&&',soundex_l[j])
    #     soundex_l.remove(soundex_l[i]) ###investigate soundex_l
    #     # print('eee',inp_data[i])
    #     inp_data.remove(inp_data[i])
    #     continue
# print(321,soundex_l)

    # print('altt',i,j,soundex_l[i],soundex_l[j],len(soundex_l[i]),len(soundex_l[j]))
    # # soundex_l[i] = soundex_l[j]
    # print('thnd',i,j,soundex_l[i],soundex_l[j],len(soundex_l[i]),len(soundex_l[j]),'\n')
# if soundex_l[i]==soundex_l[j]:
        # print('entry',soundex_l[i],soundex_l[j])
    # print(min(    (range(len(soundex_l[i]))) , (range(len(soundex_l[j])))))
    # for el in min(range(len(soundex_l[i]), range(len(soundex_l[j])))):
    #     print(soundex_l[i],soundex_l[j],'thund3r',jlfsh.damerau_levenshtein_distance(soundex_l[i][el], soundex_l[j][el]))
    #     # print())
    #     print(soundex_l[i][el], soundex_l[j][el])

    # c=jlfsh.damerau_levenshtein_distance(soundex_l[i], soundex_l[j])
    # if c<5 and len(data[i])>4 and len(data[j])>4:
#         fillup.extend([a,data[i],'&',data[j]])
# fup=[]
# for i in range(0, len(fillup), 4):
#      fup.append(fillup[i : i+4])
# fup=sorted(fup)
# for i in range(len(fup)):
#     print(fup[i]



# for i in range(len(inp_data)):
#     print(soundex_l[i],inp_data[i])

    # if a<5 and len(data[i])>4 and len(data[j])>4:
    #     fillup.extend([a,data[i],'&',data[j]])

dicto=dict(zip(inp_data,soundex_l))
# print(dicto)

# df=pd.DataFrame.from_dict(dicto,orient='index')
# print(df)
# df.to_csv(r"C:\Users\prozehnal\Desktop\csv_house\csv\outputSoundex.csv")
