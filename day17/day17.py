
def main():
    out = 0
    blocks = [[(0,0),(1,0),(2,0),(3,0)],[(1,0),(0,1),(1,1),(2,1),(1,2)],[(2,0),(2,1),(2,2),(1,0),(0,0)],[(0,0),(0,1),(0,2),(0,3)],[(0,0),(0,1),(1,0),(1,1)]]
    minoPos = 0
    top = -1
    board = []
    air = []
    airPos = 0

    with open('day17.txt') as f:
        for i,line in enumerate(f):
            air = [1 if x == ">" else -1 for x in line.strip()]
            print(len(air))

    
    for i in range(1068):
        mino = [(x[0],x[1]) for x in blocks[minoPos]]
        for j in range(len(mino)):
            mino[j] = (mino[j][0]+2,mino[j][1]+top+4)
            
        placed = False
        while (not placed):
            mino = move(mino,air[airPos],0)
            if(colliding(mino,board)):
                mino = move(mino,-air[airPos],0)
            airPos += 1
            if(airPos >= len(air)):
                airPos = 0

            mino = move(mino,0,-1)
            if(colliding(mino,board)):
                mino = move(mino,0,1)
                placed = True
                for j in mino:
                    board.append((j[0],j[1]))
                minoPos += 1
                if(minoPos >= len(blocks)):
                    minoPos = 0
                top = max(top,highest(mino))
            
    print(top+1)
    # st = ""
    # for i in range(3070):
    #     st += "|"
    #     for j in range(7):
    #         if((j,3069-i) in board):
    #             st += "#"
    #         else:
    #             st += "."
    #     st += "|\n"
    # st+="+-------+"
    # with open('day17Out.txt', 'w') as f:
    #     f.write(st)

def highest(mino):
    highest = 0
    for i in mino:
        if(i[1] > highest):
            highest = i[1]
    return highest

def move(mino,x,y):
    for i in range(len(mino)):
        mino[i] = (mino[i][0]+x,mino[i][1]+y)
    return mino

def colliding(mino,board):
    for i in mino:
        if i in board:
            return True
        if(i[0] < 0 or i[0] > 6 or i[1] < 0):
            return True
    return False

main()