from PIL import Image
import numpy as np
import os
dirname = os.path.dirname(__file__)

newimages = eval(open(os.path.join(dirname, "averages.txt"), "r").read())

imginput = input("Input image or images folder directory: ").replace("\\ ", " ").replace("\\", "/").strip()
imgoutput = input("Output folder directory: ").replace("\\ ", " ").replace("\\", "/").strip()
imgamountw = int(input("How many images wide?: "))
imgamounth = 0

maxwidth = int(input("Max output image width in pixels: "))

if imginput.startswith("'") or imginput.startswith('"'):
    imginput = imginput[slice(1,-1)]
if imgoutput.startswith("'") or imgoutput.startswith('"'):
    imgoutput = imgoutput[slice(1,-1)]
if os.path.isdir((imginput)):
    images = os.listdir(imginput)
    if ".DS_Store" in images:
        images.remove(".DS_Store")
else:
    images = [imginput[slice(imginput.rindex("/")+1, len(imginput))]]
    imginput = imginput[slice(0, imginput.rindex("/"))]

for i in range(len(images)):
    image_path = imginput+"/"+images[i]
    image = Image.open(image_path)
    width, height = image.size
    imgamounth = int((imgamountw/width)*height)
    colors = [[[],[],[]]]
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            quad = int(x/(width/imgamountw))+int(y/(height/imgamounth))*imgamountw
            if len(colors) < quad+1:
                colors.append([[],[],[]])
            colors[quad][0].append(pixel[0])
            colors[quad][1].append(pixel[1])
            colors[quad][2].append(pixel[2])
    if newimages[0][1]*imgamountw < maxwidth:
        scalefactor = 1
    else:
        scalefactor = (maxwidth/imgamountw)/newimages[0][1]
    image_width = int(newimages[0][1]*scalefactor)
    image_height = int(newimages[0][1]*scalefactor)
    grid_width = imgamountw * image_width
    grid_height = imgamounth * image_height
    grid_image = Image.new("RGBA", (grid_width, grid_height))

    for z in range(len(colors)):
        colors[z] = [int(np.mean(colors[z][0])), int(np.mean(colors[z][1])), int(np.mean(colors[z][2]))]
        closest = 0
        for g in range(len(newimages[2])):
            imgavg = newimages[2][g]
            last = newimages[2][closest]
            if abs(imgavg[0]-colors[z][0])+abs(imgavg[1]-colors[z][1])+abs(imgavg[2]-colors[z][2]) < abs(last[0]-colors[z][0])+abs(last[1]-colors[z][1])+abs(last[2]-colors[z][2]):
                closest = g
        colors[z] = newimages[1][closest]
    for z in range(len(colors)):
        newimg = Image.open(newimages[0][0]+"/"+colors[z])
        newsize = tuple(int(dim * scalefactor) for dim in newimg.size)
        scaledimage = newimg.resize(newsize)
        grid_image.paste(scaledimage, (image_width*(z%imgamountw), image_height*int(z/imgamountw)))
    print(images[i])
    grid_image.save(imgoutput+"/"+images[i][slice(images[i].rindex("."))]+".png")
