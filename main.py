string = input("Entrez une phrase : ")
string = string.lower()
output = []

for char in string:
	id = ord(char) - 96
	output.append(id)
print(output)