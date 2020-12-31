# Vigenere / Vernam / Ceasar Ciphers - Functions for encrypting and decrypting data messages. Then send them to a friend.

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesarCypher(shift: int, word):
    for a, b in word:
        if b in alphabet:
            word[a] = alphabet[a+shift]
    return word



def letterShift(amount, array):
    return array[-amount:] + array[:-amount]

print(caesarCypher(1, "abcd"))