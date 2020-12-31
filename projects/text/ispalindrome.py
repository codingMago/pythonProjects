# Check if Palindrome - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”

def isPalindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(isPalindrome("racecar"))