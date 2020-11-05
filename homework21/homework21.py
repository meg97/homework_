import json
import requests
import threading

new_list = []
with open("json_photo.json", "r") as file:
	file_1 = json.load(file)

	for i in file_1.values():
		for m in i:
			for k,s in m.items():
				if k == "url":
					new_list.append(s)


	
for j in new_list:
	file_2 = requests.get(j)	


def loading_function():
	for gg in file_2:
		if gg[-3:] =="jpg":
			with open("jpgfile.jpg", "wb") as jpgfile:
				jpgfile.write(gg.content)
		if gg[-3:] =="png":
			with open("pngfile.png", "wb") as pngfile:
				pngfile.write(gg.content)


if __name__ == "__main__":
	thread_list = []
	for i in range(10):
		x = threading.Thread(target = loading_function)
		thread_list.append(x)
		x.start()
