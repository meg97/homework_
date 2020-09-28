# for i in range(1,11):
# 	print(f"this is for{i}")
# 	for j in range(1,11):
# 		print(f"{i}x{j}={i*j}")

# for i in range(1,9,2):
# 	for j in range(0,10,2):
# 		print(f"{i}x{j} = {i*j}")
# for i in range(1,12):
# 	print(i * str(i))
# 	if i == 6:
# 		for j in range(5,0, -1):
# 			print(j* str(j))
		#break
# while True:
# 	password = ("Input password")
# 	if len(password) > 8:
# 		if "." in password:
# 			break
# print("it's good one")
import random

# m = random.randint(1,3)
# k = int(input("Tell me number"))
# while k != m:
# 	k = int(input("Tell me another"))
	
# m = random.randint(1,20)
# s = 0
# k = int(input("tell me number"))
# i = 0
# while i<=5:
# 	if m == k:
# 		s += 1
# 	i +=1
# print(f"you guess {s} times")
i = 0
user_score = 0
while i<=5:
	user_answer= int(input("guess the number"))
	random_number= random.randint(1,5)
	if user_answer == random_number:
			user_score +=1
	i +=1
print(F"your score is {user_score}")