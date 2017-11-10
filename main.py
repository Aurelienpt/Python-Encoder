
string = input("Entrez une phrase : ")
listString = list(string)
finalText = ""
for nombre, lettre in enumerate(listString):
	i = nombre
	if lettre == "a":
		listString[i] = 1
	if lettre == "b":
		listString[i] = 2
	if lettre == "c":
		listString[i] = 3
	if lettre == "d":
		listString[i] = 4
	if lettre == "e":
		listString[i] = 5
	if lettre == "f":
		listString[i] = 6
	if lettre == "g":
		listString[i] = 7
	if lettre == "h":
		listString[i] = 8
	if lettre == "i":
		listString[i] = 9
	if lettre == "j":
		listString[i] = 10
	if lettre == "k":
		listString[i] = 11
	if lettre == "l":
		listString[i] = 12
	if lettre == "m":
		listString[i] = 13
	if lettre == "n":
		listString[i] = 14
	if lettre == "o":
		listString[i] = 15
	if lettre == "p":
		listString[i] = 16
	if lettre == "q":
		listString[i] = 17
	if lettre == "r":
		listString[i] = 18
	if lettre == "s":
		listString[i] = 19
	if lettre == "t":
		listString[i] = 20
	if lettre == "u":
		listString[i] = 21
	if lettre == "v":
		listString[i] = 22
	if lettre == "w":
		listString[i] = 23
	if lettre == "x":
		listString[i] = 24
	if lettre == "y":
		listString[i] = 25
	if lettre == "z":
		listString[i] = 26
	finalText += str(listString[i])
print (finalText)