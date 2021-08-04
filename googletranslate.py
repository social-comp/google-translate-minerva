
#google cloud api translator


from os import remove
#from googletrans import Translator
import json
from pprint import pprint
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
#from nltk.corpus import stopwords
import pandas as pd
import time
import logging
from google.cloud import translate_v2 as translate 
import os
import pathlib
import ntpath



def removeSpecialCharacters(text):
    text=text.translate ({ord(c): " " for c in "】【!@#$%^&*()[]{};:,./<>?\|`~-=_+↓"}) #take out special characters
    re.findall(r'[\u4e00-\u9fff]+', text)   #chinese characters
    re.sub(r'\d+', '', text)
    text = text.replace(',', '')
    text = text.replace(':', '')
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

translate_client = translate.Client()


with open('Xinjiang_Propaganda_Department.jsonl', 'r') as json_file: #replace the jsonl file  you want to translate
    json_list = list(json_file)

t0 = time.time()
i=0

for json_str in json_list:
    i=i+1
    print(i, end =" ")
    print(": ")
    result = json.loads(json_str)
    txt=result["mblog"]["text"] #the text to be translated
    HTMLtext=txt #the text with all tags 
    txt=re.sub("<.*?>", "", txt) #take out any text that is in between the <> tags
    txt = txt.replace("#", " ") #delete hashtags 
    txt = txt.replace("@", " ") #take out @ so it translates well

  
    if(txt==""): # if there is no text to translate, just print a space
        print(" ")
        continue
    #translation = translator.translate(txt, src='zh-cn').text
    translation = translate_client.translate(txt,source_language='zh-CN' ,target_language='en')
    translatedtext= translation["translatedText"]
    translatedtext= translatedtext.replace("&quot;", '\'')
    translatedtext= translatedtext.replace("&#39;", '\'')  
  

    with open('Xinjiang_Propaganda_Department.jsonl', 'a') as data: #the name of new translated jsonl file  with url link, item id, id, mid, original text, translated text, and html text
        information = {"link":result["scheme"], "itemid": result["itemid"],'id': result["mblog"]["id"], 'mid': result["mblog"]["mid"], 'original_text': txt, 'translated_text': translatedtext, 'HTMLtext': HTMLtext}
        data.write(json.dumps(information))
        data.write("\n")

  
    print(translatedtext)
   
    
data.close()
t1 = time.time() #tracking how much time it took
total_n = t1-t0
print(total_n)
