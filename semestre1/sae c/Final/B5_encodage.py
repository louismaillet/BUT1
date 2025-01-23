from PIL import Image
def cacher(i,b):
    return i-(i%2)+b


Image_Visible=Image.open("ImagePython/hall-mod_0.bmp")
Image_Cache=Image.open("ImagePython/Imageout3.bmp")
Image2=Image_Visible.copy()
Image_resize_cache = Image_Cache.resize((Image_Visible.size[0],Image_Visible.size[1]))
for y in range(Image_Visible.size[1]):
    for x in range(Image_Visible.size[0]):
        pixel = Image_Visible.getpixel((x,y))
        valeur_R = pixel[0] - (pixel[0]%2)
        pixel = (valeur_R,pixel[1],pixel[2])
        
        pixel_cache = Image_resize_cache.getpixel((x,y))
        if pixel_cache == (255,255,255):
            Image2.putpixel((x,y),(cacher(pixel[0],0),pixel[1],pixel[2]))
        elif pixel_cache == (0,0,0):
            Image2.putpixel((x,y),(cacher(pixel[0],1),pixel[1],pixel[2]))


Image2.save("ImagePython/Imageout_steg_1.bmp")