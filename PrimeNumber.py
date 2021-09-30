from math import sqrt

PrimeNumbers = [2, 3]
PrimeToTest = [3]
prime = 2
aim = int(input("Search prime numbers from 3 to "))

with open("PrimeNumbers.txt", 'w') as file:
	file.write('2\n3\n')

for candidate in range(3, aim, 2):
	for j in PrimeToTest:
		if candidate%j == 0:
			break				#if candidate divisible
	if candidate%j == 0:			#then not prime
		continue

	PrimeNumbers.append(candidate)
	print(candidate)
	RootTest = int(sqrt(candidate)) +1
	if RootTest > prime:
		prime = PrimeNumbers[len(PrimeToTest)+1]
		PrimeToTest.append(prime)
		print("New prime added: %i" %prime)

	with open("PrimeNumbers.txt", 'a') as file:
		file.write(str(candidate))
		file.write('\n')
input("Numbers saved in PrimeNumbers.txt\nPress enter to close python")
