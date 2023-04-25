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

    def Heuristicofy(self, snake, apple, stepno, totalsteps):
        # use dfs
        visited={}
        visited["snake"] = snake
        sneks=self.PredictEveryMove(snake, apple)
        stepno+=1
        for i in range(len(sneks)):
            if stepno<=totalsteps:
                visited[str(i)]=self.Heuristicofy(sneks[i], apple, stepno, totalsteps)
        return visited

    def PredictEveryMove(self, snek, apple):
        if snek==None:
            return []
        snake=list([snek[:], snek[:], snek[:], snek[:]])
        new_blocks = list([self.movecalc(snek[len(snek)-1], 0), self.movecalc(snek[len(snek)-1], 1), self.movecalc(snek[len(snek)-1], 2), self.movecalc(snek[len(snek)-1], 3)])

        for i in range(len(new_blocks)):
            if new_blocks[i]!=apple:
                snake[i].pop(0)
            if new_blocks[i] in snek or -1 in new_blocks or self.GridSize in new_blocks:
                snake[i]=None
                new_blocks[i]=None
            else:
                snake[i].append(new_blocks[i])
        return snake

    def movecalc(self, block, dir):
        if dir==0:
            return [block[0], block[1]-1]
        elif dir==1:
            return [block[0]+1, block[1]]
        elif dir==2:
            return [block[0], block[1]+1]
        elif dir==3:
            return [block[0]-1, block[1]]

    def solve(self, snake, apple):
        self.ModifyAdjecencyMatrix(snake)
        self.printdict(self.Heuristicofy(snake, apple, 0, 5), 0)
        self.CalculateMovement(snake)
    
    def printdict(self, dictionary, level):
        lev=level
        for key in dictionary:
            if type(dictionary[key]) is dict:
                print("    "*level + str(key))
                self.printdict(dictionary[key], (level+1))
            else:
                print("    "*level + str(key)+":"+str(dictionary[key]))
    
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