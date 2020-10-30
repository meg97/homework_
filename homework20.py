import requests

class ImageJpeg:
	def __init__(self, image_list):
		self.image_list = image_list
		self.image_ = requests.get(self.image_list)

	def download(self):
		if self.image_list[-4:] == "jpeg":
			with open("jpeg.jpeg", "wb") as jpegfile:
				jpegfile.write(self.image_.content)
		

class ImagePng:
	def __init__(self, image_list):
		self.image_list = image_list
		self.image_ = requests.get(self.image_list)
	
	def download(self):
		if self.image_list[-3:] == "png":
			with open("png.png", "wb") as pngfile:
				pngfile.write(self.image_.content)


class ImageDownload(ImageJpeg, ImagePng):
	def __init__(self, image_list):
		ImageJpeg.__init__(self, image_list)
		ImagePng.__init__(self, image_list)
		self.image_ = requests.get(self.image_list)

	def download(self):
		if self.image_list[-4:] == "jpeg":	
			ImageJpeg.download(self)
		if self.image_list[-3:] == "png":
			ImagePng.download(self)


a = ImageDownload("http://www.httpbin.org/image/jpeg")
a.download()
b = ImageDownload("https://imgs.xkcd.com/comics/python.png")
b.download()