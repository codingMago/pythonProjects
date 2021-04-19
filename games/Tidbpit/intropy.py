# Intro programming

#for loops


# for x in range(0, 5):
#     print("Hello")

# x = 0

# while(x != 10):
#     x += 1
#     print(x)

person = "Johnathan"
mydog = "Dogs1are2cool3"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

if 'h' in person:
    person = person.replace('h', '')
    print(person)

replace()

def removeNumbers(sentence):
    for a in sentence:
        if RepresentsInt(a):
            b = int(a)
            if b in numbers:
                sentence = sentence.replace(a, '')

    print(sentence)

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

removeNumbers(mydog)

number = 102941204810241840
number[4::]
print(number)
sentenceH = "Hello my name is blabla"
print(sentenceH[::])


