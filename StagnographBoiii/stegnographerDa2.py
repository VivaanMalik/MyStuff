from os import device_encoding
from PIL import Image
import binascii
import optparse
import codecs
from bitstring import BitArray
#import math
import time


# Conversion functions====================================================================================================
def rgb__2__hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex__2__rgb(hexcode):
        if hexcode is None:
            return None
        return tuple(codecs.decode(hexcode[1:], 'hex'))

def str__2__bin(message):
        binary = bin(int(binascii.hexlify(message.encode()), 16))
        return binary[2:]

def bin__2__str(binary):
        binary = int(('0b' + binary), 2)
        message = binary.to_bytes((binary.bit_length() + 7) // 8, 'big').decode()
        return message

def hex__2__bit(hexcode):
        hexcode = hexcode.replace('#' , '0x')
        bitstring = BitArray(hexcode)
        return  bitstring.bin

def bit__2__hex(bitstring):
        for i in range(4, 20, 4):
            bits = '0'*i
            if(bitstring[:i] == bits):
                return '#000000'
            elif(bitstring[:i] == bits):
                hexcode = hex(int(bitstring, 2))
                hexcode = '#' + '0'*(i%4) + hexcode[2:]
                return hexcode
        if bitstring == '':
            return None
        hexcode = hex(int(bitstring, 2))
        hexcode = hexcode.replace('0x' , '#')
        return (hexcode)

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

# Manipulation functions====================================================================================================

def img__2__bit(filename):
        bitstring = ''
        img = Image.open(filename)
        datas = img.getdata()
        i=0
        for item in datas:
            bitstring += hex__2__bit(rgb__2__hex(item[0], item[1], item[2]))
            if i<8:
                print(bitstring)
                i+=1
        return bitstring
        
def bit__2__img(filename, bitstring):
        bit = 24
        new_pxl_data = []
        tmp = 0
        while(bitstring[tmp:bit].format(24)):
            if len(bit__2__hex(bitstring[tmp:int(bit)]))==2:
                print(len(bitstring))
                print(tmp)
                print(bit)
                print("oh shit!")
            r, g, b = hex__2__rgb(bit__2__hex(bitstring[tmp:int(bit)]))
            new_pxl_data.append((r,g,b,255))
            tmp = bit
            bit = bit + 24
        img=Image.open(filename)
        img.putdata(new_pxl_data)
        img.save(filename.replace('new', 'preview'), 'PNG')
        return ("Successs ma boiii!")

def merge_rgb(rgb_1, rgb_2):
    r1, g1, b1 = rgb_1
    r2, g2, b2 = rgb_2
    new_rgb=(r1[:4] + r2[:4],
           g1[:4] + g2[:4],
           b1[:4] + b2[:4])
    return new_rgb

def encode(hexcode, digit):
    if hexcode[-1] in ('0', '1', '2', '3', '4', '5'):
        hexcode=hexcode[:-1]+digit
        return hexcode
    else:
        return None

def decode(hexcode):
    if hexcode[-1] in ('0', '1'):
        return hexcode[-1]
    else:
        return None





# Main functions====================================================================================================

def stegofy(filename, msg):
    img=Image.open(filename)
    binary=str__2__bin(msg)+'1111111111111110'
    if img.mode in ('RGBA'):
        img=img.convert('RGBA')
        pxl_data=img.getdata()
        new_pxl_data=[]
        digit=0
        tmp=''
        for pxl in pxl_data:
            if digit<len(binary):
                new_pxl=encode(rgb__2__hex(pxl[0], pxl[1], pxl[2]), binary[digit])
                if new_pxl==None:
                    new_pxl_data.append(pxl)
                else:
                    r, g, b=hex__2__rgb(new_pxl)
                    new_pxl_data.append((r, g, b, 255))
                    digit+=1
            else:
                new_pxl_data.append(pxl)
        img.putdata(new_pxl_data)
        img.save(filename.replace('old', 'new'), "PNG")
        return "Completed"
    else:
        return "Incorrect img_mode                          ᕦ(ò_óˇ)ᕤ"

def unstegofy(filename):
    iiiii=0
    img=Image.open(filename)
    binary=""
    if img.mode in ('RGBA'):
        img=img.convert('RGBA')
        pxl_data=img.getdata()
        for pxl in pxl_data:
            digit=decode(rgb__2__hex(pxl[0], pxl[1], pxl[2]))
            if digit==None:
                #print("", end=" ")
                pass
            else:
                print(digit, end="", flush=True)
                iiiii+=1
                if (iiiii%8==0):
                    print("", end=" ")
                if (iiiii==128):
                    iiiii=0
                    time.sleep(0.02)
                    print("")
                binary+=digit
                if binary[-16:]=='1111111111111110':
                    print("Success boi!")
                    return bin__2__str(binary[:-16])
        return bin__2__str(binary)
    else:
        return "Incorrect img_mode                          ᕦ(ò_óˇ)ᕤ" 

def stegofy_img(filename, filename_2):
    img_1=Image.open(filename)
    img_2=Image.open(filename_2)
    if img_2.size[0] > img_1.size[0]:
        img_1.resize((img_2.size[0], round(img_1.size[1]*(img_2.size[0]/img_1.size[0]))))
        print("x problem")
    if img_2.size[1] > img_1.size[1]:
        img_1.resize((round(img_1.size[0]*(img_2.size[1]/img_1.size[1])), img_2.size[1]))
        print("y problem")
    pxl_map_1=img_1.load()
    pxl_map_2=img_2.load()
    new_image = Image.new(img_1.mode, img_1.size)
    pixels_new = new_image.load()
    for i in range(img_1.size[0]):
        for j in range(img_1.size[1]):
            #print(pxl_map_1[i,j])
            rgb_1=int__2__bin(pxl_map_1[i,j])
            rgb_2=int__2__bin((0,0,0))
            if i < img_2.size[0] and j < img_2.size[1]:
                rgb_2 = int__2__bin(pxl_map_2[i, j])
            rgb=merge_rgb(rgb_1, rgb_2)
            pixels_new[i, j] = bin__2__int(rgb)
    new_image.save(filename.replace('old', 'new'))
    unstegofy_img(filename.replace('old', 'new'))
    return "completed"

def unstegofy_img(filename):
    img=Image.open(filename)
    pxl_map=img.load()
    # new_img=Image.new(img.mode, img.size)
    # pxls_new=new_img.load()
    #orig_size=img.size
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b=int__2__bin(pxl_map[i, j])
            # rgb=(r[-4:]+r[:4],
            #      g[-4:]+g[:4],
            #      b[-4:]+b[:4])
            rgb=(r[-4:]+"0000",
                 g[-4:]+"0000",
                 b[-4:]+"0000")
            pxl_map[i, j]=bin__2__int(rgb)
            #if pxls_new[i, j] != (0, 0, 0):
                #orig_size = (i + 1, j + 1)
    #new_img = new_img.crop((0, 0, orig_size[0], orig_size[1]))
    img.save(filename.replace('new', 'preview'))
    return "done myu boiii"
    
# Da Most Main function====================================================================================================
def MAIN():
    parser=optparse.OptionParser('usage %prog '+\
         '--EncodeTxt/--DecodeTxt/--EncodeImg/--DecodeImg <target file>')
    parser.add_option('--EncodeTxt', dest='stegofy', type='string',\
         help='target Image path to encode')
    parser.add_option('--DecodeTxt', dest='unstegofy', type='string',\
         help='target Image path to decode')
    parser.add_option('--EncodeImg', dest='stegofy_img', type='string',\
         help='target Image path to encode')
    parser.add_option('--DecodeImg', dest='unstegofy_img', type='string',\
         help='target Image path to decode')
    (options, args)=parser.parse_args()
    if (options.stegofy!=None):
        text=input("Enter a msg to hide: ")
        print (stegofy(options.stegofy, text))
    elif (options.unstegofy!=None):
        for i in unstegofy(options.unstegofy):
            print(i, end="", flush=True)
            time.sleep(.01)
    elif (options.stegofy_img!=None):
        text=options.stegofy_img.replace('old', 'old_preview')
        print (stegofy_img(options.stegofy_img, text))
    elif (options.unstegofy_img!=None):
        print (unstegofy_img(options.unstegofy_img))
    else:
        print (parser.usage)
        exit(0)

MAIN()