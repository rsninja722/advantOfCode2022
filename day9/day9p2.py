chain = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
visited = set()

def main():
    out=0
    visited = set()
    with open('day9.txt') as f:
        for i,line in enumerate(f):
            d,v = line.strip().split(' ')
            v = int(v)

            for j in range(v):
                if(d == 'U'):
                    chain[0][1] -= 1
                elif(d == 'D'):
                    chain[0][1] += 1
                elif(d == 'L'):
                    chain[0][0] -= 1
                elif(d == 'R'):
                    chain[0][0] += 1

                for k in range(1,10):
                    adjust(k)

                visited.add((chain[9][0],chain[9][1]))


    strr = ""
    for y in range(-100,100):
        for x in range(-100,100):
            # char = "."
            # for i,v in enumerate(chain):
            #     if(v[0] == x and v[1] == y):
            #         char = str(i)
            #         break
            
            # strr += char
            if((x,y) in visited):
                strr += "#"
                out += 1
            else:
                strr += "."
        strr += "\n"

    with open('day9p2txt', 'w') as f:
        f.write(strr)

    print(len(visited))



def adjust(pos):
    h = chain[pos-1]
    t = chain[pos]
    xDif = (-1 if h[0] > t[0] else 1)
    yDif = (-1 if h[1] > t[1] else 1)
    xDist = abs(t[0]-h[0])
    yDist = abs(t[1]-h[1])
    
    if(xDist == 2 and yDist == 2):
        chain[pos][0] = h[0] + xDif
        chain[pos][1] = h[1] + yDif
    elif(xDist == 2 and yDist == 1):
        chain[pos][0] = h[0] + xDif
        chain[pos][1] = h[1]
    elif(xDist == 1 and yDist == 2):
        chain[pos][0] = h[0]
        chain[pos][1] = h[1] + yDif
    elif(t[0] == h[0]):
        if(yDist > 1):
            chain[pos][1] = h[1] + yDif
    elif(t[1] == h[1]):
        if(xDist > 1):
            chain[pos][0] = h[0] + xDif
main()