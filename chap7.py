# Enter your answrs for chapter 7 here
# Name: Lei Wang


# Ex. 7.5

from math import *

def estimate_pi():

	eps = 1e-15

	term = 1
	myPi=0
	k=0

	while term>= eps:
		term = factorial(4*k) * (1103 + 26390 * k)/ float(pow(factorial(k),4) * pow(396, 4*k))
		myPi = myPi + term
		print k, term, myPi
		k= k+1

	myPi = 2 * sqrt(2) / float(9801) * myPi

	myPi = 1/myPi

	print "exiting function with estimation = ", myPi

	return myPi


myPi = estimate_pi()
print "my estimated pi = ", myPi



# How many iterations does it take to converge?
# Answer: 4