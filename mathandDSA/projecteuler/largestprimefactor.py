# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

target = 13195

def primefactor(target):
    # Variable initialization
    primeFactors = []

    # Initial condition
    while target != 1:
        for i in range(2, target+1): # Loop from begnning of possible prime #'s
            remainder = target/i
            divisorString = str(remainder)

            if ".0" in divisorString[-2:] and i % 2 != 0: # As long as i seems to be a prime
                target = int(remainder)
                primeFactors.append(i)
                break
    
    return primeFactors

primefactor(600851475143)

# x = 1234
# s = str(x)
# print(s[-2:])