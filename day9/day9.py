def main():
    out=0
    visited = set()
    h = [0,0]
    t = [0,0]
    with open('day9.txt') as f:
        for i,line in enumerate(f):
            d,v = line.strip().split(' ')
            v = int(v)

            for j in range(v):
                if(d == 'U'):
                    h[1] -= 1
                    if(abs(h[1]-t[1]) > 1):
                        t[1] = h[1]+1
                        t[0] = h[0]
                elif(d == 'D'):
                    h[1] += 1
                    if(abs(h[1]-t[1]) > 1):
                        t[1] = h[1]-1
                        t[0] = h[0]
                elif(d == 'L'):
                    h[0] -= 1
                    if(abs(h[0]-t[0]) > 1):
                        t[0] = h[0]+1
                        t[1] = h[1]
                elif(d == 'R'):
                    h[0] += 1
                    if(abs(h[0]-t[0]) > 1):
                        t[0] = h[0]-1
                        t[1] = h[1]
                visited.add((t[0],t[1]))


    

    print(len(visited))

main()