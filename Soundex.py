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
# print(combined_l)
# for i in combined_l:
#     print(i)
print(len(inp_data),len(soundex_l),len(i_l))
# print('i_l',i_l)
# print('soundex_l',soundex_l)
# print('inp_data',inp_data,'\n')


# print(soundex_l,inp_data)

for i,j in zip(range(0,len(soundex_l)-1), range(1,len(soundex_l))):
    # print(soundex_l[i],soundex_l[j])
    if soundex_l[i]==soundex_l[j]:
        print(soundex_l[i],'&&&',soundex_l[j])
#2312312312312312312312312312312312        soundex_l.remove(soundex_l[i]) ###investigate soundex_l
        # soundex_l.remove(inp_data[i])

# for i in range(len(inp_data)):
#     print(soundex_l[i],inp_data[i])

    # if a<5 and len(data[i])>4 and len(data[j])>4:
    #     fillup.extend([a,data[i],'&',data[j]])

dicto=dict(zip(inp_data,soundex_l))
# print(dicto)

# df=pd.DataFrame.from_dict(dicto,orient='index')
# print(df)
# df.to_csv(r"C:\Users\prozehnal\Desktop\csv_house\csv\outputSoundex.csv")
