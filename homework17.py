# class HouseHeating:
# 	def __init__(self, room1, room2, room3, room4):
# 		self.room1 = room1
# 		self.room2 = room2
# 		self.room3 = room3
# 		self.room4 = room4

# 		self.goal_1 = 24
# 		self.goal_2 = 25
# 		self.goal_3 = 26
# 		self.goal_4 = 27
# 		self.room = 0

# 	def compare(self):
# 		if self.room1 == self.goal_1:
# 			self.room += 1	
# 		elif self.room1 < self.goal_1:
# 			print("You should increase the temperature of the first room")
# 		elif self.room1 > self.goal_1:
# 			print("You should make lower the temperature of the first room")
		
# 		if self.room2 == self.goal_2:
# 			self.room +=1
# 		elif self.room2 < goal_2:
# 			print("You should increase the temperature of the second room")
# 		elif self.room2 > self.goal_2:
# 			print("You should make lower the temperature of the second room")

# 		if self.room3 == self.goal_3:
# 			self.room += 1
# 		elif self.room3 < self.goal_3:
# 			print("You should increase the temperature of the third room")
# 		elif self.room3 > self.goal_3:
# 			print("You should make lower the temperature of the third room")
			
# 		if self.room4 == self.goal_4:
# 			self.room +=1
# 		elif self.room4 < self.goal_4:
# 			print("You should increase the temperature of the fourth room")
# 		elif self.room4 > self.goal_4:
# 			print("You should make lower the temperature of the fourth room")
# 		print(f"{self.room} of 4 have normal temperature, the rest you should change")
			

# a = HouseHeating(26,25,26,27)
# a.compare()


class HouseHeating:
	def __init__(self, temp1, temp2, temp3, temp4):
		self.__temp1 = temp1
		self.__temp2 = temp2
		self.__temp3 = temp3
		self.__temp4 = temp4
		self.temperatures = {"room1":self.__temp1, "room2": self.__temp2, "room3": self.__temp3, "room4": self.__temp4}
		self.goal_temp = 10
		self.new_goal = {}
		self.room = 0
		
	def goal_temp1(self):
		for i, k in self.temperatures.items():
			if k == self.goal_temp:
				self.room += 1
				print(f"{self.room} of 4 have normal temperature")
			elif k != self.goal_temp:
				self.new_goal[i] = self.goal_temp
		print(self.new_goal)

	def new_grade(self, temp1_1, temp2_2, temp3_3, temp4_4):
		self.__temp1 = temp1_1
		self.__temp2 = temp2_2
		self.__temp3 = temp3_3
		self.__temp4 = temp4_4

	def change(self):
		self.choice = input("which room's temperature do you want to change?")
		self.my_temperature = input("how do you want to change. Tell me the temperature")
		for i,k in self.temperatures.items():
			if self.choice == i:
				self.new_goal[i] = self.my_temperature
		print(self.new_goal)

a = HouseHeating(10,11,12,13)
a.goal_temp1()
a.new_grade(10,10,11,13)
a.goal_temp1()
a.change()