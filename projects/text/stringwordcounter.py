# Count Words in a String - Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.


"""
FILE HANDLING
"""
# Define a filename.
filename = "/home/secimax/Repositories/pythonProjects/projects/text/file.txt"

# Open the file as f.
# The function readlines() reads the file.
with open(filename, "r") as f:
    data = f.readlines()


"""
METHOD AREA
"""
# String word counter
def wordCounter(inputdata):
    count = 1

    for i in inputdata:
        if i == " ":
            count += 1

print(wordCounter("chunkysalsa is gooooood, very good!"))

# File word counter
def filewordCounter(inputdata):
    sentence = inputdata[0]
    count = 1

    for i in sentence:
        if i == " ":
            count += 1
    
    return count


print(wordCounter(data))