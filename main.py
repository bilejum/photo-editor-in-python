from PIL import Image

im = Image.open("img\泉此方 壁纸.jpg")

# im = im.rotate(45)
# im.show()
print(im.filename)
print(im.size)
print(im.width)
print(im.height)
print(im.info)
