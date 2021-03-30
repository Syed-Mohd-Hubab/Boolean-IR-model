import Stemmer
stemmer = Stemmer.Stemmer('english')

words = []

for NUMBER in range(1, 51):
    name = str(NUMBER) + ".txt"
    path = "./CS317-w07-IR Dataset for A1/ShortStoriesCleaned/"+name
    file = open(path, encoding='windows-1252')
    words = file.readlines()
    file.close()
    
    for i in range(len(words)):
        words[i] = words[i].replace('\n', '')
    
    stems = stemmer.stemWords(words)

    path = "./CS317-w07-IR Dataset for A1/ShortStoriesStemmed/" + name
    file = open(path, "w")

    for i in range(len(stems)):
        file.write(stems[i]+'\n')
    
    file.close()

    print(NUMBER, " before ->", len(words))
    print(NUMBER, " after ->", len(stems)) 
