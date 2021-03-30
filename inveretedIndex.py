dict = {}

for NUMBER in range(1, 51):
    name = str(NUMBER) + ".txt"
    path = "./CS317-w07-IR Dataset for A1/ShortStoriesStemmed/"+name
    file = open(path, encoding='windows-1252')
    words = file.readlines()

    for i in range(len(words)):
        words[i] = words[i].replace('\n', '')
        if words[i] not in dict:
            dict[words[i]] = []
        if NUMBER not in dict[words[i]]:
            dict[words[i]].append(NUMBER)

    print("Dictionary length at file",NUMBER," is: ",len(dict))
    file.close()

import json

json.dump(dict, open("dictionary.json", "w"))
