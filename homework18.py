import os

b = os.getcwd()
a = os.chdir("..")
os.makedirs("new_folder/Dir1/dir3/Dir4")
k = os.chdir("new_folder/Dir1")
os.mkdir("Dir2")

m = os.chdir("..")
list_ = os.listdir(m)
s = os.chdir("Dir1")
mmm = os.listdir(s)
list_.append(mmm)
ss = os.chdir("dir3")
mmmm = os.listdir(ss)
list_.append(mmmm)


while os.listdir():
	answer = input("do you want to delite the file?")
	file = F"{os.getcwd()}/{os.listdir()[0]}"
	if answer == "yes": #and #type(file) is dir:
		os.rmdir(file)
		print(os.listdir())
	if answer == "yes" and type(file) is not dir:
		os.remove(file)
		print(os.listdir)


 	
