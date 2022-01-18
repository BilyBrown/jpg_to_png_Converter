from PIL import Image, ImageFilter
import os
import sys

'''the first argument is the folder containing files, the second argument is the destination'''
dir = sys.argv[1]
new_folder = sys.argv[2]

try:
    new_path = os.path.join(dir, new_folder)
    os.mkdir(new_path)
except:
    pass

for images in os.listdir(dir):
    if images != new_folder:
        if os.path.splitext(images)[1] == ".jpg":
            image = os.path.splitext(images)[0]
            img = Image.open(f"{dir}/"+images)
            # these are options to alter the images as it runs through them.
            # blurrd = img.filter(ImageFilter.EMBOSS)
            # box = (100, 100, 400, 400)
            # rotate = blurrd.rotate(angle=60)
            # crop = rotate.crop(box)
            # rotate.save(f"boxed{image}.png", "png")
            img.save(f"{new_path}/PNG{image}.png", "png")
