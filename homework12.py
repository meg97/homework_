import random
bulls = 0
cows = 0
check = "continue"
while check == "continue":
	random_answer = random.randint(1000,9999)
	user_answer = input("Tell me 4 digit number")
	for i in user_answer:
		if i in str(random_answer):
			bulls +=1
	for j in str(random_answer):
		if i == j:
			cows +=1
		print(f"cows: {cows},bulls: {bulls}")
if int(user_answer) == random_answer:
	check != "continue"
print(f"cows: {cows},bulls: {bulls}")