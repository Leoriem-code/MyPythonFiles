from math import sqrt

global PrimeNumbers
global PrimeToTest
global LastPrime
PrimeNumbers = [2, 3]
PrimeToTest = [3]
LastPrime = 2

def write(number):
	with open("PrimeNumbers.txt", 'a') as file:
		file.write(str(number))
		file.write('\n')

def CreatePrime(aim, start=3, writing=True):
	global PrimeNumbers
	global PrimeToTest
	global LastPrime

	print("Creation began...")
	for candidate in range(start, aim, 2):
		for j in PrimeToTest:
			if candidate%j == 0:
				break				#if candidate divisible
		if candidate%j == 0:			#then not prime
			continue

		PrimeNumbers.append(candidate)
		RootTest = int(sqrt(candidate)) +1
		if RootTest > LastPrime:
			LastPrime = PrimeNumbers[len(PrimeToTest)+1]
			PrimeToTest.append(LastPrime)

		if writing:
			write(candidate)
	print("Creation ended!")
	if writing:
		print('Numbers are saved in "PrimeNumbers.txt')

def CompletePrimeList(number):
	global PrimeToTest

	with open("PrimeNumbers.txt", 'r') as file:
		text = file.read().split('\n')
	if int(text[-1]) > number:
		index = text.index(str(number))
		for i in range(index+1):
			PrimeToTest.append(int(i))
	else:
		for i in text:
			PrimeToTest.append(int(i))
		CreatePrime(number+2, int(text[-1]))

def VerifPrimeList(number):
	if int(sqrt(number)) +1 > PrimeToTest[-1]:
		if number < 10000000:
			CreatePrime(number+2, 3, False)
		else:
			CompletePrimeList(number)

def FindPrime(number):
	if number%2 == 0:
		return False
	VerifPrimeList(number)
	for i in PrimeToTest:
		if number%i == 0:
			return True
	return False

def FindFactors(prime):
	VerifPrimeList(prime)
	if not FindPrime(prime):
		PrimeToTest.insert(0, 2)
		factors = ""
		while prime != 1:
			for i in PrimeToTest:
				if prime%i == 0:
					factors += '%i*' %i
					prime = prime//i
					break
		return factors[:-1]
	else:
		return str(prime)
