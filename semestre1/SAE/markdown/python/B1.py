from PIL import Image

i= Image.open("Imagetest/Imagetest.bmp")
sortie = Image.new(i.mode, i.size[::-1])

for x in range(i.size[0]):
    for y in range(i.size[1]):
        sortie.putpixel((y,x), i.getpixel((x,y)))

sortie.save("Imageout0.bmp")

