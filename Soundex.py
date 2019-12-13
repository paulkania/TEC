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

#this block makes no alteration in data.
#it only compares sound-token elements together, and compares there similarity.
#see conclusion below
close_ld=[]
for i,j in zip(range(0,len(soundex_l)-1), range(1,len(soundex_l))):
    # print('RESSSET',i,j,soundex_l[i],soundex_l[j],len(soundex_l[i]),len(soundex_l[j]))

    # if len(soundex_l[i]) != len(soundex_l[j]):#probably not strictly necessary
    ld=0
    for el in range( min(len(soundex_l[i]), len(soundex_l[j]))):
        # print(inp_data[i],'&',inp_data[j],soundex_l[i][el],soundex_l[j][el],'thund3r')
        ld_el= jlfsh.damerau_levenshtein_distance(soundex_l[i][el], soundex_l[j][el])
        # print('ld',jlfsh.damerau_levenshtein_distance(soundex_l[i][el], soundex_l[j][el]))
        # print('jaro',jlfsh.jaro_distance(soundex_l[i][el], soundex_l[j][el]))
        # print('hamming',jlfsh.hamming_distance(soundex_l[i][el], soundex_l[j][el]))
        ld+= ld_el
        if ld<4:
            close_ld.extend(inp_data[i])
            close_ld.extend(inp_data[j])
        # print()

# print(close_ld)


###remove duplicates (geotargetting, google ad thing)
r_iter=0
for i,j in zip(range(0,len(soundex_l)-1), range(1,len(soundex_l))):
    if soundex_l[i]==soundex_l[j]:
        r_iter+=1
for i,j in zip(range(0,len(soundex_l)-r_iter-1), range(1,len(soundex_l)-r_iter)):
    if soundex_l[i]==soundex_l[j]:
        r_iter+=1
        # print(soundex_l[i],'&&&',soundex_l[j],i_l[i],'+++',i_l[j])
        i_l.remove(i_l[i])
        soundex_l.remove(soundex_l[i])
        # print('item removed',i_l)

#this block is great. it takes a nested list of
    #strings which are within the list separated by commas.
        #it then joins the separate strings together, spaced by a space in this case
        #and appended to a new list.
# print('markin',i_l[0],i_l[0][0],i_l) #granularity is by word
i_l_out=[]
for i in i_l:
    j= " ".join(i) #join replaces commas with " " j = i.replace(',',' ') DOES not work, i believe replace only works within a string, rather than between strings. #str.replace == str.split().join()
    # print(j)
    i_l_out.append(j)
# print('markout',i_l_out[0],i_l_out) #granularity is by letter
# print(len(i_l_out),len(inp_data),len(i_l),len(soundex_l),type(inp_data),type(i_l))

dicto=dict(zip(i_l_out,soundex_l))
print(dicto)

df=pd.DataFrame.from_dict(dicto,orient='index')
# print(len(df),'\n\n\n',df)
# print(df.loc[:,0])

# print(df[0],df[1],df[2],df[3],df[4]) # turns index into a column of it's own, new index is a numbered index (0->42,len=43)

#iamlegend
# print(df[0:5]) #first 5 rows all columns
# print(df['index'][1]) #gives first column...must include ' '
# print(df[0]) #gives first column...must include ' '
df.reset_index(inplace=True)
df.reset_index(inplace=True)

print(df)
dupe=[]
j='A330'
print(df[0][4])
for i in range(len(df[0])-1):
    j=df[0][i+1]
    # print('iii',i)
    if jlfsh.damerau_levenshtein_distance(df[0][i], j) <3:
        print(df[0][i],j)
        dupe.append(df['index'][i]+' '+df[0][i])#+df[0][j])
        j=df[0][i-1]

print('dupe',dupe)
#

#itertools
# dupes=[]
for token,combos in itertools.combinations(df[0],2):
    print('1000',token,combos)
#     if token is not None and combos is not None:
#         d_ld= jlfsh.damerau_levenshtein_distance(token, combos)
#         # print(df[0])
#         if d_ld>1:
#             continue
#         else:
#             # print(token,'<',combos,'>',d_ld) #df['index'][token]
#             # dupes.append(token+' '+combos) #df['index']
#             for token,combos in itertools.combinations(df[1],2):
#                 if token is not None and combos is not None:
#                     d_ld= jlfsh.damerau_levenshtein_distance(token, combos)
#                     if d_ld>1:
#                         continue
#                     else:
#                         print(token,combos,d_ld)
#                         dupes.append(token+' '+combos) #df['index']
# print('MARKOUT',len(dupes),dupes)



# for i in range(len(df)):
#     print(df[0])
df.to_csv(r"C:\Users\prozehnal\Desktop\csv_house\csv\outputSoundex.csv")
