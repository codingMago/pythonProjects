# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def isPalindrome(number):
	holder = str(number)
	if holder == holder[::-1]:
		return True
	
	return False
	

def palindromeFinder():
	maxnum = 999 * 999
	highestPal = 0
	palHolder = []
	for i in range(maxnum, 800_000, -1):
		if isPalindrome(i) == True:
			palHolder.append[i]
			print(i)
			break


time = 1
space = 3

timespace = [1,2,3,4]
timespaceR = [[1][2][3][4]]





		

			
	
palindromeFinder()

# print(isPalindrome(988889))

# num = 988889
# stNum = str(num)
# print(stNum)
# print(stNum[-1])


