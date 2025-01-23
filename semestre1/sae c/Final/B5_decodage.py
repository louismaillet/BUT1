from PIL import Image
def trouver(i):
    return i%2

Image_Init = Image.open("ImagePython/Imageout_steg_1.bmp")
Image2=Image_Init.copy()
for y in range(Image_Init.size[1]):
    for x in range(Image_Init.size[0]):
        pixel = Image_Init.getpixel((x,y))
        if trouver(pixel[0]) == 1:
            Image2.putpixel((x,y),(255,255,255))
        elif trouver(pixel[0]) == 0:
            Image2.putpixel((x,y),(0,0,0))
Image2.save("ImagePython/Imageout_steg_2.bmp")