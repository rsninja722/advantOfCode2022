
def main():
    out = 0
    cubes = set()

    xlow = 0
    xhigh = 0
    ylow = 0
    yhigh = 0
    zlow = 0
    zhigh = 0


    with open('day18.txt') as f:
        for i,line in enumerate(f):
            x,y,z = [int(x) for x in line.strip().split(',')]
            cubes.add((x,y,z))
            if x < xlow:
                xlow = x
            if x > xhigh:
                xhigh = x
            if y < ylow:
                ylow = y
            if y > yhigh:
                yhigh = y
            if z < zlow:
                zlow = z
            if z > zhigh:
                zhigh = z

    
    visited = set()
    contained = set()
    air = False

    
    print(xlow,xhigh,ylow,yhigh,zlow,zhigh)
    for x in range(xlow,xhigh):
        for y in range(ylow,yhigh):
            for z in range(zlow,zhigh):
                if (x,y,z) not in visited and (x,y,z) not in cubes:
                    air = False
                    visited = set()
                    queue = [(x,y,z)]
                    while len(queue) > 0:
                        i = queue.pop()
                        visited.add((i[0],i[1],i[2]))
                        for j in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
                            check = (i[0]+j[0],i[1]+j[1],i[2]+j[2])
                            if not air:
                                if i[0]+j[0] < xlow or i[0]+j[0] > xhigh or i[1]+j[1] < ylow or i[1]+j[1] > yhigh or i[2]+j[2] < zlow or i[2]+j[2] > zhigh:
                                    air = True
                                    queue = []
                                    break

                            if check not in visited and check not in cubes:
                                queue.append((i[0]+j[0],i[1]+j[1],i[2]+j[2]))
                    if not air:
                        contained = contained.union(visited)

    cubes = cubes.union(contained)

    for i in cubes:
        for j in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            if (i[0]+j[0],i[1]+j[1],i[2]+j[2]) not in cubes:
                out += 1

    print(out)

main()