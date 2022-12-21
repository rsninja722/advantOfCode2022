
def main():
    out = 0
    cubes = []

    with open('day18.txt') as f:
        for i,line in enumerate(f):
            x,y,z = [int(x) for x in line.strip().split(',')]
            cubes.append((x,y,z))

    for i in cubes:
        for j in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            if (i[0]+j[0],i[1]+j[1],i[2]+j[2]) not in cubes:
                out += 1
    
    print(out)

main()