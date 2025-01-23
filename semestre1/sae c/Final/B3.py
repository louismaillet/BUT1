from PIL import Image

i= Image.open("IUT-Orleans.bmp")
sortie = Image.new(i.mode, i.size)

for x in range(i.size[0]):
    for y in range(i.size[1]):
        sortie.putpixel((x,y), (sum(i.getpixel((x,y)))//3,)*3)
        
sortie.save("imageout2.bmp")