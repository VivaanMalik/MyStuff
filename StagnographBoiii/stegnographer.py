from os import device_encoding
from PIL import Image
import binascii
import optparse
import codecs

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

# Manipulation functions====================================================================================================
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
    img=Image.open(filename)
    binary=""
    if img.mode in ('RGBA'):
        img=img.convert('RGBA')
        pxl_data=img.getdata()
        for pxl in pxl_data:
            digit=decode(rgb__2__hex(pxl[0], pxl[1], pxl[2]))
            if digit==None:
                pass
            else:
                binary+=digit
                if binary[-16:]=='1111111111111110':
                    print("Success boi!")
                    return bin__2__str(binary[:-16])
        return bin__2__str(binary)
    else:
        return "Incorrect img_mode                          ᕦ(ò_óˇ)ᕤ" 

# Da Most Main function====================================================================================================
def MAIN():
    parser=optparse.OptionParser('usage %prog '+\
         '-e/-d <target file>')
    parser.add_option('-e', dest='stegofy', type='string',\
         help='target Image path to encode')
    parser.add_option('-d', dest='unstegofy', type='string',\
         help='target Image path to decode')
    (options, args)=parser.parse_args()
    if (options.stegofy!=None):
        text=input("Enter a msg to hide: ")
        print (stegofy(options.stegofy, text))
    elif (options.unstegofy!=None):
        print (unstegofy(options.unstegofy))
    else:
        print (parser.usage)
        exit(0)

MAIN()