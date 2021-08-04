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


covid_words = ["epidemic", "pandemic", "virus", "crown", "crown's", "crownvirus", "coronavirus", "covid", "covid-19",  "covid19", "covid 19", "covidvirus", "bat virus", "vaccination", "vaccinating", "vaccinations", "vaccine", "vaccines", "vaccine's", "contagious", "infectious", "isolated", "isolating", "isolation", "quarantine", "quarantining", "contact tracing", "contact trace", "travel ban", "travel bans", "outbreak", "outbreaks"]
covid_posts=0




  
with open('censored_posts.json') as data_file:    
    inf = json.load(data_file)
    for result in inf:
        txt=result["text__1"]
        if(isinstance(txt, str)):
            txt=result["text__1"].lower()
        else:
            txt=str(txt).lower()
        if any(s in txt for s in covid_words):
            covid_posts+=1
            with open('covid_related_censored_posts.jsonl', 'a') as data:
                information = {"postnumber":covid_posts, "status_id": result["status_id"],'original_text': result['text'], 'translated_text': result["text__1"]}
                data.write(json.dumps(information))
                data.write("\n")
data.close()



def random_lines(filename):
    idxs = random.sample(range(covid_posts), 50)
    return [linecache.getline(filename, i) for i in idxs]

fi = open("50_censored_covid_samples_new.jsonl", "w")
for line in random_lines('covid_related_censored_posts.jsonl'):
      fi.write(line)
fi.close()
