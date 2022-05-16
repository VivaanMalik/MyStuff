import json


filenem=input("OBJ FILE NAME: \n")
if filenem[-4:]!=".obj":
    print("Failure")
    quit()

objectdata={"vertices":[], "edges":[], "faces":[]}

filenem="objs\\"+filenem

with open(filenem, "r") as f:
    lines = f.readlines()
    for i in lines:
        if i.startswith("v "):
            spliti=i.replace("\n", "").replace("v ", "").split(" ")
            objectdata["vertices"].append([])
            for j in spliti:
                objectdata["vertices"][len(objectdata["vertices"])-1].append([float(j)])
            objectdata["vertices"][len(objectdata["vertices"])-1].append([1.0])
        elif i.startswith("f "):
            spliti=i.replace("\n", "").replace("f ", "").split(" ")
            objectdata["faces"].append([])
            for j in spliti:
                objectdata["faces"][len(objectdata["faces"])-1].append([int(j)])
            for index, j in enumerate(spliti):
                if index<len(spliti)-1:
                    objectdata["edges"].append([[int(j)], [int(spliti[index+1])]])
                else:
                    objectdata["edges"].append([[int(j)], [int(spliti[0])]])

with open("Jsons\\"+filenem[5:-4]+".json", "w+") as f:
    json.dump(objectdata, f, indent=4)