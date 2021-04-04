import json
import numpy as np
import Stemmer
stemmer = Stemmer.Stemmer('english') 
f1 = open("dictionary.json", )
data = json.load(f1)
f2 = open("positions.json", )
data2 = json.load(f2)

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return sorted(lst3)

def union(lst1, lst2):
    lst3 = list(set(lst1) | set(lst2))
    return sorted(lst3)

def complement(lst1):
    lst2 = []
    for i in range(1, 51):
        lst2.append(i)
    lst3 = [value for value in lst2 if value not in lst1]
    return lst3

def replaceNot(query):
    # print('Before: ',query)
    booleans = ['and', 'or']
    res1 = []
    res2 = []
    res3 = []
    i = 0
    while(i < len(query)):
        # print("Now at {}, {}".format(i, query[i]))
        if query[i] == 'not':
            term = query[i+1]
            query.pop(i)
            query.pop(i)
            # i += 2
            if term == []:
                lst = []
            else:
                lst = data[term]
            res1 = complement(lst) 
            query.insert(i, res1)
            # print('Not encountered, current query: ', query)
        elif query[i] not in booleans:
            term = query[i]
            query.pop(i)
            query.insert(i, data[term])
            # print('!bool encountered, current query: ', query)
        i += 1
    # print('After: ', query)
    boolProcessing(query)

def boolProcessing(query):
    # print('#################')
    # print('Before: ',query)
    booleans = ['and', 'or']
    res1 = []
    res2 = []
    res3 = []
    i = 0
    while(i < len(query)):
        if query[i] in booleans:
            t1 = query[i-1]
            ope = query[i]
            t2 = query[i+1]
            # print('perform {} on {},,,, {}'.format(query[i].upper(), t1, t2))
            query.pop(i)
            query.pop(i)
            query.pop(i-1)
            if ope == 'and':
                res1 = intersection(t1, t2)
            if ope == 'or':
                res1 = union(t1, t2)
            query.insert(i-1, res1)
            i = i-1
            # print('Current query: ', query)
        else:
            i += 1
    # print('After: ',len(query),query)
    if len(query)>1:
        print('Wrong query Entered!')
    else:
        print('Final Result:', query[0])
        
def checkTermsExistance(query):
    for i, term in enumerate(query):
        if term not in data and term not in booleans: 
            print('`{}`not in data'.format(term))
            query[i] = []
    return query

def proximityQuery(query):
    t1 = query.pop(0)
    t2 = query.pop(0)
    dist = int(query[0][1])
    t1 = data2[t1]
    t2 = data2[t2]
    lst1, lst2 = [], []
    for file in t1:
        lst1.append(file)
    for file in t2:
        lst2.append(file)
    lst = intersection(lst1, lst2)
    # lst = sorted(lst)
    # print('Intersecting docs: ', lst)
    finalDocs = []
    for doc in lst:
        for i in t1[doc]:
            # print(num, end=', ')
            # print(type(i))
            for j in t2[doc]:
                if abs(i-j) <= dist:
                    # print("In doc {} at {}, {}".format(doc ,i, j))
                    finalDocs.append(doc)
    print('Result of proximity query: ', finalDocs)    

if __name__ == "__main__":
    query = input('Enter the query:')
    queryWords = query.split()
    query = []
    booleans = ['and', 'or', 'not']
    operators = []
    terms = []

    for word in queryWords:
        word = word.lower()
        if word in booleans:
            operators.append(word)
            query.append(word)
        else:
            stem = stemmer.stemWord(word)
            query.append(stem)
            terms.append(stem)

    if len(operators) == 0 and len(query) == 3 and query[2][1].isnumeric():
        print('Proximity query with {} words apart.'.format(query[2][1]))
        proximityQuery(query)

    elif (len(operators) == 0 and len(terms) > 2) or (len(operators) > 0 and len(terms) == 0):
            print('Wrong query entered!')
            quit()
    
    else:
        print('Boolean query with {} boolean operators.'.format(len(operators)))
        query = checkTermsExistance(query)
        # print('query after removing non-existant terms: ', query)
        replaceNot(query)

