
def main():
    blocks = [[(0,0),(1,0),(2,0),(3,0)],[(1,0),(0,1),(1,1),(2,1),(1,2)],[(2,0),(2,1),(2,2),(1,0),(0,0)],[(0,0),(0,1),(0,2),(0,3)],[(0,0),(0,1),(1,0),(1,1)]]
    minoPos = 0
    top = -1
    board = []
    air = []
    airPos = 0

    with open('day17.txt') as f:
        for i,line in enumerate(f):
            air = [1 if x == ">" else -1 for x in line.strip()]

    for i in range(1000000):
        board.append([False,False,False,False,False,False,False])


    placedd = 0
    lastPlacedd = 0
    dif = 0
    lastDiff = 0
    notFound = True

    remaining = 1000000000000

    height = 0
    while(remaining > 0):
        placedd += 1
        remaining -= 1
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
                    board[j[1]][j[0]] = True
                minoPos += 1
                if(minoPos >= len(blocks)):
                    minoPos = 0
                top = max(top,highest(mino))
            if(airPos == 1 and minoPos == 1 and notFound):
                if(top-dif == lastDiff):
                    repeatPlace = placedd-lastPlacedd
                    repeatHeight = (top - dif)
                    height += (remaining // repeatPlace) * repeatHeight
                    remaining -= (remaining // repeatPlace) * repeatPlace
                    remaining -= 1
                    print(height)
                    notFound = False
                    break
                lastDiff = top-dif
                dif = top
                lastPlacedd = placedd

    print(top+1)
    print(height+ top+1)

    # left = 1000000000000
    # left -= placedd
    # height = top

    # print(height)
    # height += (left //repeatPlace) * repeatHeight

    # print(repeatPlace)
    # print(repeatHeight)

    # print(height)
    # print(left%repeatPlace)

    


    # minoPos = 1
    # top = -1
    # board = []
    # airPos = 1
    # for i in range(1000000):
    #         board.append([False,False,False,False,False,False,False])

    # for i in range(left%repeatPlace):
    #     mino = [(x[0],x[1]) for x in blocks[minoPos]]
    #     for j in range(len(mino)):
    #         mino[j] = (mino[j][0]+2,mino[j][1]+top+4)
            
    #     placed = False
    #     while (not placed):
    #         mino = move(mino,air[airPos],0)
    #         if(colliding(mino,board)):
    #             mino = move(mino,-air[airPos],0)
    #         airPos += 1
    #         if(airPos >= len(air)):
    #             airPos = 0

    #         mino = move(mino,0,-1)
    #         if(colliding(mino,board)):
    #             mino = move(mino,0,1)
    #             placed = True
    #             for j in mino:
    #                 board[j[1]][j[0]] = True
    #             minoPos += 1
    #             if(minoPos >= len(blocks)):
    #                 minoPos = 0
    #             top = max(top,highest(mino))

    

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
        if(i[0] < 0 or i[0] > 6 or i[1] < 0):
            return True
        if board[i[1]][i[0]]:
            return True
    return False

main()