
# Returns number of lines in the file 
def countLines(file):
    count = len(file.readlines())
    return count

# Returns a list of stopWords as provide in the file
def getStopWords():
    # Read given stopwords into an array 'words'
    wordFile = open("./CS317-w07-IR Dataset for A1/Stopword-List.txt", encoding='utf8')
    numLines = countLines(wordFile)
    stopWords = []
    wordFile.seek(0)
    for i in range(numLines):
        stopWords.append(wordFile.readline())
        stopWords[i] = stopWords[i].replace('\n', '') # Removing \n from the word's end  
    print("Stop Words extracted: ", stopWords)
    return stopWords

# Removing punctuations from the 'file' recieved as argument
def removePunctuations(file, name):
    # Opening Desired File
    path = "./CS317-w07-IR Dataset for A1/ShortStories/"
    path = path + name
    file = open(path, encoding='utf8')
    fileStr = file.read()       # Single string containing whole file
    fileStr = fileStr.lower()   # Case folding
    alphabets = '''abcdefghijklmnopqrstuvwxyz'''

    # Reading the file string char-by-char, if its not an alphabet/space/newline, remove it
    for char in fileStr:
        if char is "-": # '\n;?:!.,.'
            fileStr = fileStr.replace(char, " ")    
        if char not in alphabets and char is not " " and char is not '\n':
            # print("Punc: ",char)
            fileStr = fileStr.replace(char, "")

    # Writing cleaned file to a new txt 
    path = "./CS317-w07-IR Dataset for A1/ShortStoriesNoPunc/"+name
    cleanedFile = open(path, "w+")
    for char in fileStr:
        cleanedFile.write(char)

    print("Removed Punctuations & case folding", name)

    file.close()
    return cleanedFile

# Removal of stop words from cleaned file 
def removeStopWords(cleanedFile, stopWords, name):
    # Placing cursor at file start
    cleanedFile.seek(0)
    fileStr = cleanedFile.read()
    fileWords = []
    # Storing all the words of the file in a 1D-Array
    for word in fileStr.split():
        fileWords.append(word)
    # print("file words: ", fileWords)
    
    # Replacing all stopwords with ''
    for word in fileWords:
        if word in stopWords:
            # print("word b4:", word)
            word = word.replace(word, "")
            # print("word after:", word)
    print("Stopwords removed: ", name)

    path = "./CS317-w07-IR Dataset for A1/ShortStoriesCleaned/"+name
    finalFile = open(path, "w")

    for word in fileWords:
        finalFile.write(word+'\n')
    
    finalFile.close()
    cleanedFile.close()

# Opening the file to be cleaned
def preprocessingFiles(fileNum):
    # READING THE FILE
    path = "./CS317-w07-IR Dataset for A1/ShortStories/"
    name = str(fileNum) + ".txt"
    path = path + name
    file = open(path, encoding='utf8')

    # Counting the number of line in the file
    lines = countLines(file)
    print("Num of lines in the file: ",name, lines)
    
    return file, name

###################
### DRIVER CODE ###
###################
def main():
    print()
    stopWords = getStopWords()
    for i in range(1, 51):
        NUMBER = i
        file, name = preprocessingFiles(NUMBER)
        cleanedFile = removePunctuations(file, name)
        removeStopWords(cleanedFile, stopWords, name)

if __name__ == "__main__":
    main()
