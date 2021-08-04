#combines jsonlines from desired jsonl files into one, and takes a desired sample from the lines
import pathlib
import ntpath
import random
import os
import linecache
x=0
files=[]
for path in pathlib.Path("/Users/sophiawang/Desktop/May18").iterdir(): #replace the path with the folder of jsonl files you want to merge
    if path.is_file():
        print(path)
        if ntpath.basename(path).endswith(".jsonl"): 
            files.append(ntpath.basename(path))   
         

f = open("bigfile.txt", "w") #creates a file called bigfile.txt, with all json lines in file from the jsonl files in the path specified
for file in files:
    with open(file) as file:
      f.write(file.read())
f.close()

def random_lines(filename):
    idxs = random.sample(range(25919), 50) # (range(amount of lines there are in total), sample amount you want)
    return [linecache.getline(filename, i) for i in idxs]



fi = open("randomsamples.jsonl", "w") #creates randomsamples.jsonl with random lines according to the amount you put
for line in random_lines('bigfiletest.txt'):
      fi.write(line)
fi.close()



"""
def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open('counseling3.json', 'w') as output_file:
        json.dump(result, output_file)

merge_JsonFiles(files)

"""

