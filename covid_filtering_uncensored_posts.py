#filtering uncensored posts 

import pathlib
import ntpath
import json
import pandas as pd
from os import X_OK, remove
import json
from pprint import pprint
import pandas as pd
import random
import linecache

covid_words = ["epidemic", "pandemic", "virus", "crown", "crown's", "crownvirus", "coronavirus", "covid", "covid-19",  "covid19", "covid 19", "covidvirus", "bat virus", "flu", "vaccination", "vaccinating", "vaccinations", "vaccine", "vaccines", "vaccine's", "contagious", "infectious", "isolated", "isolating", "isolation", "quarantine", "quarantining", "contact tracing", "contact trace", "travel ban", "travel bans", "outbreak", "outbreaks"]
 
covid_posts=0
files=[]
for path in pathlib.Path("/Users/sophiawang/Desktop/May18/translated").iterdir(): #put the path of the translated posts in jsonl files
    if path.is_file():
        if ntpath.basename(path).endswith(".jsonl"):
            files.append(path)    #append the path to a files list 


for file in files: #goes through list of jsonl files and read them 
    with open(file, 'r') as json_file:
        json_list = list(json_file)
    for json_str in json_list:
        result = json.loads(json_str)
        txt=result["translated_text"].lower() #lowercase
        if any(s in txt for s in covid_words):
            covid_posts+=1 #counts how many covid posts there are 
            with open('covid_related_uncensored_posts.jsonl', 'a') as data:
                information = {"postnumber":covid_posts, "link":result["link"], "itemid": result["itemid"],'id': result["id"], 'mid': result["mid"], 'original_text': result['original_text'], 'translated_text': result["translated_text"], 'HTMLtext': result["HTMLtext"]}
                data.write(json.dumps(information))
                data.write("\n")
data.close()


def random_lines(filename):
    idxs = random.sample(range(covid_posts), 50) # random sample of 50 covid related posts
    return [linecache.getline(filename, i) for i in idxs]

fi = open("50uncensoredsamples.jsonl", "w") #name of new file with uncensored samples
for line in random_lines('covid_related_uncensored_posts.jsonl'):
      fi.write(line)
fi.close()
