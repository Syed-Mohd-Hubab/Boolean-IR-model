
import json
import numpy as np
import Stemmer
stemmer = Stemmer.Stemmer('english')

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

f = open("dictionary.json", )

data = json.load(f)

a = "ladies"
b = "gentleman"

a = stemmer.stemWord(a)
b = stemmer.stemWord(b) 

print(a)
print(b)

l1 = (data[a])
l2 = (data[b])

res = intersection(l1, l2)

print(res) 
