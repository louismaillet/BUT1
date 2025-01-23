from PIL import Image

i= Image.open("IUT-Orleans.bmp")
sortie = Image.new(i.mode, i.size)

for x in range(i.size[0]):
    for y in range(i.size[1]):
        sortie.putpixel((x,y), (255,)*3 if sum([i.getpixel((x,y))[k]**2 for k in range(3)]) > 255**2*3/2 else (3,)*3)
        
sortie.save("Imageout3.bmp")