import random
def int__2__bin(rgb):
    #print ("rgb: "+str(rgb))
    r, g, b = rgb
    return ('{0:08b}'.format(int(r)),
            '{0:08b}'.format(int(g)),
            '{0:08b}'.format(int(b)))

def bin__2__int(rgb):
    r, g, b=rgb
    return (int(r, 2),
            int(g, 2),
            int(b, 2))

def merge_rgb(rgb_1, rgb_2):
    r1, g1, b1 = rgb_1
    r2, g2, b2 = rgb_2
    new_rgb=(r1[:4] + r2[:4],
           g1[:4] + g2[:4],
           b1[:4] + b2[:4])
    return new_rgb

print(random.randrange(0, 2))
print(random.randrange(0, 2))
print(merge_rgb(("11110000", "11110000", "11110000"), ("00001111", "00001111", "00001111")))
print(bin__2__int(int__2__bin((253,173,63))))