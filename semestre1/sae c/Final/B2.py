from PIL import Image

i= Image.open("hall-mod_0.bmp")
sortie = Image.new(i.mode, i.size)

for x in range(i.size[0]):
    for y in range(i.size[1]):
        sortie.putpixel((i.size[0]-x-1,y), i.getpixel((x,y)))
        
sortie.save("Imageout1.bmp")