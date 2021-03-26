
def countLines(file):
    count = len(file.readlines())
    return count+1

def countLines2(file):
    file.seek(0)
    line = 1
    for word in file:
        if word == '\n':
            line = line + 1
    print("Number of lines in file is: ", line)

def preprocessingFiles():
    # READING THE FILE
    file = open("./CS317-w07-IR Dataset for A1/ShortStories/1.txt", encoding='utf8')
    print("First line of the file: "+file.readline())
    lines = countLines(file)
    print("Num of lines in the file: ", lines)

def main():
    preprocessingFiles()

if __name__ == "__main__":
    main()
