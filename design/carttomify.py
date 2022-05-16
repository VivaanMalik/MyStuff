from PIL import Image, ImageOps
import numpy
image  = Image.open("nanuamuiva.jpeg")
grayskelimg = ImageOps.grayscale(image)
pxldata = image.load()
graypxldata = grayskelimg.load()
# colors = [[68, 59, 49]]
colors = []
rangeval = 3
multiplyval = 85
for r in range(rangeval):
    for g in range(rangeval):
        for b in range(rangeval):
            colors.append([r*multiplyval, g*multiplyval, b*multiplyval])
print("colors added")
def getColorDistance(rgb1, rgb2):
    rgb1 = numpy.array(rgb1)
    rgb2 = numpy.array(rgb2)
    rm = 0.5*(rgb1[0]+rgb2[0])
    d = abs(sum((2+rm,4,3-rm)*(rgb1-rgb2)**2))**0.5
    return d

output = Image.new(image.mode, image.size)
for x in range(image.width):
    for y in range(image.height):
        r = pxldata[x, y][0]
        g = pxldata[x, y][1]
        b = pxldata[x, y][2]
        intensity = graypxldata[x, y]
        output.putpixel((x, y), pxldata[x, y])
        for i in colors:
            cd = getColorDistance(i, [r, g, b])
            if cd < 50:
                output.putpixel((x, y), (i[0], i[1], i[2]))
print("added data")
output = output.save("output.png")