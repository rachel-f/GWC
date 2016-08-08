from PIL import Image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

im = Image.open("yoda.jpg")

data = im.getdata()
data_list = list(data)

data_list

picture_list = []

length = len(data_list)

for tuple in data_list:
	total = tuple[0] + tuple[1] +tuple[2]
	if total < 182:
		picture_list.append(darkBlue)
	elif total > 182 and total <= 364:
		picture_list.append(red)
	elif total > 364 and total <= 546:
		picture_list.append(lightBlue)
	else:
		picture_list.append(yellow)




new_img = Image.new("RGB", (1800, 1200), "white")
new_img.putdata(picture_list)




new_img.show()


