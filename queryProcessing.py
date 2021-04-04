import json
import numpy as np
import Stemmer
stemmer = Stemmer.Stemmer('english') 
f = open("dictionary.json", )
data = json.load(f)

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

def processing(operators, terms):
    result = []

    if terms == 2:
        twoTermProcessing(operators, terms)
    elif terms == 3:
        threeTermProcessing(operators, terms)
    else:
        print(">3 terms qeuries not supported...")
        return

def twoTermProcessing(operators, terms):
    result = []
    operator = operators.pop(0)
    if operator == "not":
        term = terms.pop(0)
        lst = data[term]
        res1 = complement(lst)
        operator = operators.pop(0)
        term = term.pop(0)
        if operator == 'and':
            result = intersection(res1, data[term])
        elif operator == 'or':
            result = union(res1, data[term])
        else:
            print("WRONG QUERY")
        print("!Final result of 2 terms:", result)
        return
    else:
        t1 = terms.pop(0)
        t2 = terms.pop(0)
        if operator == 'and':
            result = intersection(data[t1], data[t2])
        elif operator == 'or':
            result = union(data[t1], data[t2])
        print("Final result of 2 terms:", result)

def replaceNot(query):
    print('Before: ',query)
    booleans = ['and', 'or']
    res1 = []
    res2 = []
    res3 = []
    i = 0
    while(i <len(query)):
        print("Now at {}, {}".format(i, query[i]))
        if query[i] == 'not':
            term = query[i+1]
            query.pop(i)
            query.pop(i)
            # i += 2
            res1 = complement(data[term]) 
            query.insert(i, res1)
            print('Not encountered, current query: ', query)
        elif query[i] not in booleans:
            term = query[i]
            query.pop(i)
            query.insert(i, data[term])
            print('!bool encountered, current query: ', query)
        i += 1
    print('After: ', query)
    boolProcessing(query)

def boolProcessing(query):
    print('#################')
    print('Before: ',query)
    booleans = ['and', 'or']
    res1 = []
    res2 = []
    res3 = []
    i = 0
    while(len(query)):
        if query[i] in booleans:
            t1 = query[i-1]
            ope = query[i]
            t2 = query[i+1]
            print('perform {} on {},,,, {}'.format(query[i].upper(), t1, t2))
            query.pop(i)
            query.pop(i)
            query.pop(i-1)
            if ope == 'and':
                res1 = intersection(t1, t2)
            if ope == 'or':
                res1 = union(t1, t2)
            query.insert(i-1, res1)
            i = i-1
            print('Current query: ', query)
        else:
            i += 1
    print('After: ',i,query)
        
def checkTermsExistance(terms):
    flag = True
    for term in terms:
        if term not in data:
            print('The stemmed term `{}` does not exist in the dictionry!'.format(term))
            flag = False
    return flag


if __name__ == "__main__":
    query = input('Enter the query:')
    queryWords = query.split()
    query = []
    booleans = ["and", "or", "not"]
    operators = []
    terms = []
    i=0
    for word in queryWords:
        word = word.lower()
        if word in booleans:
            operators.append(word)
            query.append(word)
        else:
            stem = stemmer.stemWord(word)
            query.append(stem)
            terms.append(stem)
            i = i+1

    if( not checkTermsExistance(terms)):
        print('Exiting program, terms not found!')
        quit()

    replaceNot(query)


    # print("Operators extracted:", operators)
    # print("Terms extracted:", terms)
    # print("Query stemmed: ", query)

    ### SIMPLE QUERY PROCESSING ###



