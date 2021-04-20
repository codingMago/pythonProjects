# Runtime: 32 ms, faster than 87.62% of Python3 online submissions for Check if the Sentence Is Pangram.
# Memory Usage: 14.4 MB, less than 20.01% of Python3 online submissions for Check if the Sentence Is Pangram.

sentence = "thequickbrownfoxjumpsoverthelazydog"

def checkIfPangram(sentence):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w","x","y","z"]
    for i in sentence:
        if i in alphabet:
            alphabet.remove(i)
    
    return True if len(alphabet) == 0 else False

print(checkIfPangram(sentence))