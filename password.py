from random import choice
characters = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ """

def create_password(length):
	password = []

	for i in range(length):
		password.append(choice(characters))

	return ''.join(password)

def create_passwords(how_many, length=15):
	for i in range(how_many):
		print(create_password(length))

if __name__ == "__main__":
	variables = input("Length of the password: (length*number)").split("*")
	if len(variables) == 1:
		print(create_password(int(variables[0])))
	else:
		create_passwords(int(variables[0]), int(variables[1]))
