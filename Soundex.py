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

i_l=[]
for i in inp_data:
    i=i.split()
    i_l.append(i)

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

#this block makes no alteration in data.
#it only compares sound-token elements together, and compares there similarity.
#see conclusion below
# for i,j in zip(range(0,len(soundex_l)-1), range(1,len(soundex_l))):
#     print(i,j,soundex_l[i],soundex_l[j],len(soundex_l[i]),len(soundex_l[j]))

    # if len(soundex_l[i]) != len(soundex_l[j]):#probably not strictly necessary

    # for el in range( min(len(soundex_l[i]), len(soundex_l[j]))):
        #print(inp_data[i],'&',inp_data[j],soundex_l[i][el],soundex_l[j][el],'thund3r')
        ## print('ld',jlfsh.damerau_levenshtein_distance(soundex_l[i][el], soundex_l[j][el]))
        ## print('jaro',jlfsh.jaro_distance(soundex_l[i][el], soundex_l[j][el]))
        #print('hamming',jlfsh.hamming_distance(soundex_l[i][el], soundex_l[j][el]))
        ## print()
# what I'm seeing is that the soundex tokens aren't good indicators of similarity. - Dynamic & Engagement are paired 2/4 [D552 E522]
# therefore i'll move on, look at the notebook and see what's good.
# maybe i'll try to amalgamate these to programs.
# where it was useful was below..in accounting for special characters.

#a counter for r_iter, so that the iterations of the duplicate remover function dont get out of range.
r_iter=0
for i,j in zip(range(0,len(soundex_l)-1), range(1,len(soundex_l))):
    if soundex_l[i]==soundex_l[j]:
        r_iter+=1

###remove duplicates (geotargetting, google ad thing)
for i,j in zip(range(0,len(soundex_l)-r_iter-1), range(1,len(soundex_l)-r_iter)):
    if soundex_l[i]==soundex_l[j]:
        r_iter+=1
        print(soundex_l[i],'&&&',soundex_l[j],i_l[i],'+++',i_l[j])
        i_l.remove(i_l[i])
        soundex_l.remove(soundex_l[i])
        print('999',i_l)
#--------------
print('ttt',i_l)
#this block is great. it takes a nested list of
    #strings which are within the list separated by commas.
        #it then joins the separate strings together, spaced by a space in this case
        #and appended to a new list.
i_l_out=[]
for i in i_l:
    j= " ".join(i)
    print(j)
    i_l_out.append(j)
# print('21',i_l_out)
# print(len(i_l_out),len(inp_data),len(i_l),len(soundex_l),type(inp_data),type(i_l))

dicto=dict(zip(i_l_out,soundex_l))
print(dicto)

df=pd.DataFrame.from_dict(dicto,orient='index')
print(df)
df.to_csv(r"C:\Users\prozehnal\Desktop\csv_house\csv\outputSoundex.csv")
