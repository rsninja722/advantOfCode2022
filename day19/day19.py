
def main():
    out = 0
    blueprints = []

    with open('test.txt') as f:
        for i,line in enumerate(f):
            x = line.strip().split()
            blueprints.append([[int(x[6]),0,0],[int(x[12]),0,0],[int(x[18]),int(x[21]),0],[int(x[27]),0,int(x[30])]])
    
    for i in blueprints:
        print(i)
    for x,blueprint in enumerate(blueprints):
        # oreBots clayBots obsidianBots geodeBots ore clay obsidian geode
        queue = [[1,0,0,0,0,0,0,0]]

        oreFound = False
        obsidianFound = False
        highestOreCost = 0
        highestClayCost = 0
        highestObsidianCost = 0
        for i in blueprint:
            if(i[0] > highestOreCost):
                highestOreCost = i[0]
            if(i[1] > highestClayCost):
                highestClayCost = i[1]
            if(i[2] > highestObsidianCost):
                highestObsidianCost = i[2]
        for i in range(24):
            newQueue = []
            print(len(queue))
            for j in queue:
                if(not oreFound):
                    if(j[3] > 0):
                        oreFound = True
                elif(j[2] < 1):
                    continue
                
                if(j[4] >= blueprint[3][0] and j[6] > blueprint[3][2]):
                    newQueue.append([j[0],j[1],j[2],j[3]+1,j[4]+j[0]-blueprint[3][0],j[5]+j[1],j[6]+j[2]-blueprint[3][2],j[7]+j[3]])
                    continue
                else:
                    newQueue.append([j[0],j[1],j[2],j[3],j[4]+j[0],j[5]+j[1],j[6]+j[2],j[7]+j[3]])
                if(j[4] >= blueprint[0][0] and j[0] < highestOreCost):
                    newQueue.append([j[0]+1,j[1],j[2],j[3],j[4]+j[0]-blueprint[0][0],j[5]+j[1],j[6]+j[2],j[7]+j[3]])
                if(j[4] >= blueprint[1][0] and j[1] < highestClayCost):
                    newQueue.append([j[0],j[1]+1,j[2],j[3],j[4]+j[0]-blueprint[1][0],j[5]+j[1],j[6]+j[2],j[7]+j[3]])
                if(j[4] >= blueprint[2][0] and j[5] > blueprint[2][1] and j[3] < highestObsidianCost):
                    newQueue.append([j[0],j[1],j[2]+1,j[3],j[4]+j[0]-blueprint[2][0],j[5]+j[1]-blueprint[2][1],j[6]+j[2],j[7]+j[3]])
            queue = newQueue
        most = 0
        for i in queue:
            most = max(most, i[7])
        print(most)
        out += (most)*(x+1)
    print(out)

main()