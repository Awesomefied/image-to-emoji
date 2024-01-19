from PIL import Image
import numpy as np
import os
dirname = os.path.dirname(__file__)

path = input("Input images folder directory: ")
if path.startswith("'") or path.startswith('"'):
    path = path[slice(1,-1)]
images = os.listdir(path)
if ".DS_Store" in images:
        images.remove(".DS_Store")
allcolors = []
allcolors.append([path])
allcolors.append(images)
allcolors.append([])

for i in range(len(images)):
    image_path = path+"/"+images[i]
    image = Image.open(image_path)
    width = image.size[0]
    colors = [[],[],[]]
    print(images[i])
    if i == 0:
        allcolors[0].append(width)
    for y in range(width):
        for x in range(width):
            pixel = image.getpixel((x, y))
            if (pixel[3] > 127):
                colors[0].append(pixel[0]) 
                colors[1].append(pixel[1]) 
                colors[2].append(pixel[2]) 
    colors = [int(np.mean(colors[0])), int(np.mean(colors[1])), int(np.mean(colors[2]))]
    allcolors[2].append(colors)

f = open(os.path.join(dirname, "averages.txt"), "w")
f.write(str(allcolors))
f.close()
print("Color averages of "+str(len(images))+" images saved to 'averages.txt'")