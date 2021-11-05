import csv
import json
word_list=[]
with open("nl_words_sorted.csv",'r',encoding="utf-8") as file:
    reader=csv.reader(file)
    for i in reader:
        word_list.append(i)
word_dict={}
level=0
for i in range(0,5000,20):
    level+=1 
    word_dict[level]={word_list[k][0]:word_list[k][1] for k in range(i,i+20)}
with open('data.json', 'w',encoding="utf-8") as outfile:
    json.dump(word_dict, outfile)