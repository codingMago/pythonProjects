# Count Vowels - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

vowels = ["a", "e", "i", "o", "u"]

def countVowels(word):
    counter = 0
    for i in word:
        if i in vowels:
            counter += 1
    
    return counter

print(countVowels("apples"))