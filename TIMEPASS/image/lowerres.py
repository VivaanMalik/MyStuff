import os
from PIL import Image

files = []

directory = input("dir:\n")
for fname in os.listdir(directory):
    file = os.path.join(directory, fname)
    if os.path.isfile(file) and not fname.startswith("Stego") and fname.endswith(".png") or fname.endswith(".jpg"):
        files.append([file, fname])

for i in files:
    img = Image.open(i[0])
    print(i[1])
    if i[1][-4:] == ".jpg":
        img = img.convert('RGB')
    img.save("out\\"+i[1][0:-4]+"_lowres"+i[1][-4:], quality=25, optimize=True)