import requests

class ImageJpeg:
	def __init__(self, image_list):
		self.image_list = input("tell me an adress")
		self.image_ = requests.get(self.image_list)

	def download(self):
		for i in self.image_:
			if type(i) == "jpeg":
				with open("jpeg.jpeg", "wb") as jpegfile:
					jpegfile.write(image_.content)


class ImagePng(ImageJpeg):
	def __init__(self, image_list):
		ImageJpeg.__init__(self, image_list)
		self.image_ = requests.get(self.image_list)
	def download(self):
		for k in self.image_:
			if type(k) == "png":
				with open("png.png", "wb") as pngfile:
					pngfile.write(image_.content)


class ImageDownload(ImageJpeg):
	def __init__(self, image_list):
		ImageJpeg.__init__(self, image_list)
		self.image_ = requests.get(self.image_list)

	def download(self):
		for m in self.image_:
			if type(m) == "jpeg":
				ImageJpeg.download()
			if type(m) == "png":
				ImagePng.download()


a = ImageDownload("k")
a.download()