# image-to-emoji
Convert any image into a grid of emojis or any set of images.

<img src="https://raw.githubusercontent.com/Awesomefied/image-to-emoji/main/github%20emoji%20logo.png">

This project requires Python 3 and the [Python Imaging Library (PIL)](https://pillow.readthedocs.io/en/stable/installation.html) to be installed. Note that it may take up to a few minutes to compute the final image depending on how many refrence images you select.

Start by running 'setup.py' and entering the folder directory of the [emoji images](https://github.com/Awesomefied/image-to-emoji/blob/main/apple%20emojis.zip) or any refrence images. The refrence images must all be the same size and the pixel width and height must be the same (the images must all be squares). The names of the images will be printed when the color average is calculated. The color averages of all of the images are saved in the file 'averages.txt' for the other py file to read from. You only need to run 'setup.py' once or when you want to use diffferent refrence images.  
```
Input images folder directory: '/Example/Directory/Folder/Path'
```

After running 'setup.py', start running 'render.py'. You can either input a path to a single image or a folder with multiple images. If given a folder with multiple images, the program will convert each image in the folder one at a time.
```
Input images folder directory: '/Example/Image/Folder/Path'
```
```
Input images folder directory: '/Example/Image/Path.png'
```

Enter the output folder path.
```
Output folder directory: '/Example/Output/Folder/Path'
```

Enter how many refrence images wide you want the output to be. The height will be calculated from the refrence image.
```
How many images wide?: 50
```

Enter the maximum width of the output image in pixels. Height will be calculated from the aspect ratio of the refrence image.
```
Max output image width in pixels: 1000
```

The program will print the image name once the conversion is finished.
