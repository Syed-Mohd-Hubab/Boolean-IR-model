
# Returns number of lines in the file 
def countLines(file):
    count = len(file.readlines())
    return count


# Removing punctuations from the 'file' recieved as argument
def removePunctuations(file):
    # Opening Desired File
    file = open("./CS317-w07-IR Dataset for A1/ShortStories/1.txt", encoding='utf8')
    fileStr = file.read()       # Single string containing whole file
    fileStr = fileStr.lower()   # Case folding
    alphabets = '''abcdefghijklmnopqrstuvwxyz'''

    # Reading the file string char-by-char, if its not an alphabet/space/newline, remove it
    for char in fileStr:
        if char not in alphabets and char is not " " and char is not '\n':
            # print("Punc: ",char)
            fileStr = fileStr.replace(char, "")

    # Writing cleaned file to a new txt 
    cleanedFile = open("./CS317-w07-IR Dataset for A1/ShortStoriesCleaned/1-noPunc.txt","w+")
    for char in fileStr:
        cleanedFile.write(char)

    print("New clean file created!!!")
    return cleanedFile


# Removal of stop words from cleaned file 
def removeStopWords(cleanedFile):
    # Read given stopwords into an array 'words'
    wordFile = open("./CS317-w07-IR Dataset for A1/Stopword-List.txt", encoding='utf8')
    numLines = countLines(wordFile)
    stopWords = []
    wordFile.seek(0)
    for i in range(numLines):
        stopWords.append(wordFile.readline())
        stopWords[i] = stopWords[i].replace('\n', '') # Removing \n from the word's end  
    print("Stop Words extracted: ", stopWords)

    cleanedFile.seek(0)
    fileStr = cleanedFile.read()
    fileWords = []
    for word in fileStr.split():
        fileWords.append(word)
    print("file words: ", fileWords)
    for word in fileWords:
        if word in stopWords:
            # print("word b4:", word)
            word = word.replace(word, "")
            # print("word after:", word)
    print("All stopwords have been removed from file word array!")
    finalFile = open("./CS317-w07-IR Dataset for A1/ShortStoriesCleaned/1-final.txt","w")

    for word in fileWords:
        finalFile.write(word+'\n')
    
    finalFile.close()


# Opening the file to be cleaned
def preprocessingFiles():
    # READING THE FILE
    file = open("./CS317-w07-IR Dataset for A1/ShortStories/1.txt", encoding='utf8')
    print("First line of the file: "+file.readline())
    # Counting the number of line in the file
    lines = countLines(file)
    print("Num of lines in the file: ", lines)
    return file

###################
### DRIVER CODE ###
def main():
    print()
    file = preprocessingFiles()
    cleanedFile = removePunctuations(file)
    removeStopWords(cleanedFile)

if __name__ == "__main__":
    main()
