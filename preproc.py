
def countLines(file):
    count = len(file.readlines())
    return count

# Removing punctuations from the text
def removePunctuations(file):
    file.seek(0)
    read = file.read()
    punc = '''!()-[]{};:'"\,<>./?@’#$“”%^&*_~�'''
    for line in read:
        if line in punc:
            print("Punc: ",line)
            read = read.replace(line,"")

    cleanedFile = open("./CS317-w07-IR Dataset for A1/ShortStoriesCleaned/1-pp.txt","w+")
    for line in read:
        cleanedFile.write(line)
    cleanedFile.close()
    print("Wrote new file without punctuations") 

def removeStopWords():
    # Read stopword into an array
    wordFile = open("./CS317-w07-IR Dataset for A1/Stopword-List.txt", encoding='utf8')
    numLines = countLines(wordFile)
    words = []
    wordFile.seek(0)
    for i in range(numLines):
        words.append(wordFile.readline())
        words[i] = words[i].replace('\n', '') # Removing \n from all words end 
    print("Words", words)

def preprocessingFiles():
    # READING THE FILE
    file = open("./CS317-w07-IR Dataset for A1/ShortStories/1.txt", encoding='utf8')
    print("First line of the file: "+file.readline())
    # Counting the number of line in the file
    lines = countLines(file)
    print("Num of lines in the file: ", lines)
    return file


def main():
    # file = preprocessingFiles()
    # removePunctuations(file)
    removeStopWords()

if __name__ == "__main__":
    main()
