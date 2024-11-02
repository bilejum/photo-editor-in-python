from PIL import ImageOps, Image
import os


my_image = Image.open("img\泉此方 壁纸.jpg")

flip_image = ImageOps.cover(my_image, (100, 100))

flip_image.show()
flip_image_name = os.path.abspath("img\泉此方 壁纸.jpg")

print(flip_image_name)

flip_image.save(flip_image_name)
