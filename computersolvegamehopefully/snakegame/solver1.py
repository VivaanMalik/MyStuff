class SolvingAlgorithms():
    def __init__(self, gridsize, grid):
        print("\n")
        self.HamiltonianCycleToUseOld=[]
        AM = []
        for _y in range(gridsize**2):
            row = []
            for _x in range(gridsize**2):
                row.append(0)
            AM.append(row)
        self.GridSize = gridsize
        self.Grid = grid

        print(self.Grid)

        for y in range(gridsize**2):
            for x in range(gridsize**2):
                AM[y][x] = self.isneighbour(self.Grid[x], self.Grid[y])
        
        self.AdjecencyMatrix = AM
        self.ModifiedAjecencyMatrix = AM
        
        print("Adjecency Matrix:")
        self.printlistasboxesfor1andzero(self.AdjecencyMatrix)  
    
    def FindHamiltonianCycle(self, snake):
        self.HamiltonianCycles=[]
        self.ModifyAdjecencyMatrix(snake)
        self.FindCycle(self.Grid.index(snake[len(snake)-1]), [self.Grid.index(snake[len(snake)-1])])
        print(len(self.HamiltonianCycles))

    def FindCycle(self, curentnode, nodelist):
        for i in range(len(self.ModifiedAjecencyMatrix[curentnode])):
            if self.ModifiedAjecencyMatrix[curentnode][i] == 1 and not i in nodelist:
                nodelist.append(i)
                self.FindCycle(i, nodelist)
        if len(nodelist)==len(self.Grid):
            nl=[]
            for i in nodelist:
                nl.append(i)
            self.HamiltonianCycles.append(nl)
        nodelist.pop(-1)

    def ModifyAdjecencyMatrix(self, snake):
        self.ModifiedAjecencyMatrix = self.AdjecencyMatrix
        am = self.ModifiedAjecencyMatrix
        for i in range(1, len(snake)-1):
            for j in range(len(am[self.Grid.index(snake[i])])):
                if am[self.Grid.index(snake[i])][j]==1:
                    if not (self.Grid[j]==snake[i-1] or self.Grid[j]==snake[i+1]):
                        am[self.Grid.index(snake[i])][j]=0
        am[self.Grid.index(snake[len(snake)-1])][self.Grid.index(snake[len(snake)-2])] = 0
        self.ModifiedAjecencyMatrix = am
        self.printlistasboxesfor1andzero(self.ModifiedAjecencyMatrix)
    
    def FindFastestHamiltonianCycle(self, apple):
        index = (self.GridSize**2)-1
        hcnumber = 0
        for (i, hc) in enumerate(self.HamiltonianCycles):
            if hc.index(self.Grid.index(apple))<index:
                index = hc.index(self.Grid.index(apple))
                hcnumber=i
        print(self.HamiltonianCycles)
        self.HamiltonianCycleToUse = self.HamiltonianCycles[hcnumber]
    
    def CalculateMovement(self, snake):
        pos1 = snake[len(snake)-1]
        pos2 = self.Grid[self.HamiltonianCycleToUse[1]]
        print(self.HamiltonianCycleToUse)
        if pos1[0]+1==pos2[0]:
            self.DirectionToTravel=1
            print("right")
        elif pos1[0]-1==pos2[0]:
            self.DirectionToTravel=3
            print("left")
        elif pos1[1]+1==pos2[1]:
            self.DirectionToTravel=2
            print("down")
        elif pos1[1]-1==pos2[1]:
            self.DirectionToTravel=0
            print("up")
        else:
            print("wtf")
            x = input("")
    def solve(self, snake, apple):
        self.FindHamiltonianCycle(snake)
        self.FindFastestHamiltonianCycle(apple)
        self.CalculateMovement(snake)
    
    def isneighbour(self, x, y):
        if [x[0], x[1]+1]==y or [x[0], x[1]-1]==y or [x[0]+1, x[1]]==y or [x[0]-1, x[1]]==y:
            return 1
        return 0
    
    def printlistasboxesfor1andzero(self, list):
        num = "  "
        for i in range(len(list[0])):
            num+=self.getcirclenumber(i)

        print(num)
        for y in range(len(list)):
            if len(list[y])<200:

                print(self.getcirclenumber(y), end="")

                for x in range(len(list[y])):
                    if list[y][x]==1:
                        print("██", end="")
                    elif list[y][x]==0:
                        if x%2==0:
                            print("  ", end="")
                        else:
                            print("┊┊", end="")
                    elif list[y][x]==-1:
                        print("╳╳", end="")
                    else:
                        print(list[y][x], end="")
                print("\n", end="")
        print("\n")

    def getcirclenumber(self, num):
        nums="⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚㉛㉜㉝㉞㉟㊱㊲㊳㊴㊵㊶㊷㊸㊹㊺㊻㊼㊽㊾㊿"
        n = nums[num] if num<=49 else str(num)
        if num<20:
            n+=" "
        return n