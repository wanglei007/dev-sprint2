# Enter your answrs for chapter 6 here
# Name: Lei Wang


# Ex. 6.6

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if len(word)==0 or len(word)==1:
		return True
	else:
		if first(word) == last(word):
			return is_palindrome(middle(word))
		else:
			return False

word = raw_input("give me a word: ")
if is_palindrome(word):
	print "It is Palidrome!"
else:
	print "Sorry, try another one"

# Ex 6.8 GCD

def GCD(a,b):
	if b==0:
		return a
	else:
		r = a % b
		return GCD(b, r)

a = raw_input("give me a number: ")
b = raw_input("give me another number: ")
print GCD(int(a), int(b))

