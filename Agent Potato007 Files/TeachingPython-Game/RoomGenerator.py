import random

rows = 6
def GetRooms():
    Rooms =[
        0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0]

    
    roomwidth = 6

    spawnpoint = 1
    lootroom = 2
    bossroom = 3

    existing_rooms = []
    leftBound = [0, 6, 12, 18, 24, 30]
    rightbound = [5, 11, 17, 23, 29, 35]

    spawnindex = random.choice([14, 15, 20, 21])
    Rooms[spawnindex]=spawnpoint

    currentcell = spawnindex
    Room_count = 0

    while Room_count<5:
        top = False
        bottom = False
        left = True
        right = True

        if currentcell-roomwidth>=0:
            top = True
        if currentcell+roomwidth<len(Rooms):
            bottom = True
        if currentcell in leftBound:
            left = False
        if currentcell in rightbound:
            right = False 
        
        direction = random.choice([0, 1, 2, 3])
        if direction==0 and top:
            Rooms[currentcell-roomwidth]=lootroom
            currentcell-=roomwidth
        elif direction==1 and bottom:
            Rooms[currentcell+roomwidth]=lootroom
            currentcell+=roomwidth
        elif direction==2 and left:
            Rooms[currentcell-1]=lootroom
            currentcell-=1
        elif direction==3 and right:
            Rooms[currentcell+1]=lootroom
            currentcell+=1
        Room_count=len(Rooms) - Rooms.count(0)
        Rooms[spawnindex]=spawnpoint

    while Room_count<9:
        top = False
        bottom = False
        left = True
        right = True

        if currentcell-roomwidth>=0:
            top = True
        if currentcell+roomwidth<len(Rooms):
            bottom = True
        if currentcell in leftBound:
            left = False
        if currentcell in rightbound:
            right = False 
        
        direction = random.choice([0, 1, 2, 3])
        if direction==0 and top:
            Rooms[currentcell-roomwidth]=lootroom
            currentcell-=roomwidth
        elif direction==1 and bottom:
            Rooms[currentcell+roomwidth]=lootroom
            currentcell+=roomwidth
        elif direction==2 and left:
            Rooms[currentcell-1]=lootroom
            currentcell-=1
        elif direction==3 and right:
            Rooms[currentcell+1]=lootroom
            currentcell+=1
        Room_count=len(Rooms) - Rooms.count(0)
        Rooms[spawnindex]=spawnpoint

    while Rooms.count(bossroom)==0:
        top = False
        bottom = False
        left = True
        right = True

        if currentcell-roomwidth>=0:
            top = True
        if currentcell+roomwidth<len(Rooms):
            bottom = True
        if currentcell in leftBound:
            left = False
        if currentcell in rightbound:
            right = False 
        
        direction = random.choice([0, 1, 2, 3])
        if direction==0 and top:
            Rooms[currentcell-roomwidth]=bossroom
            currentcell-=roomwidth
        elif direction==1 and bottom:
            Rooms[currentcell+roomwidth]=bossroom
            currentcell+=roomwidth
        elif direction==2 and left:
            Rooms[currentcell-1]=bossroom
            currentcell-=1
        elif direction==3 and right:
            Rooms[currentcell+1]=bossroom
            currentcell+=1
        Rooms[spawnindex]=spawnpoint
    return Rooms
