import json
import requests
import threading


with open("json_photo.json", "r") as file:
	file_1 = json.load(file)
	file_2 = requests.get(file_1)

def loading_function():
	for i in file_1(items):
		if i[-3:] =="jpg":
			with open("jpgfile.jpg", "wb") as gpegfile:
				jpgfile.write(i.content)
		if i[-3:] =="png":
			with open("pngfile.png", "wb") as pngfile:
				pngfile.write(i.content)


if __name__ == "__main__":
	thread_list = []
	for i in range(10):
		x = threading.Thread(target = loading_function)
		thread_list.append(x)
		x.start()
