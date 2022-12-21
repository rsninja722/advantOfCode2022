
def main():
    grid = []
    out = 0
    floor = 0

    for y in range(1000):
        grid.append([])
        for x in range(1000):
            grid[y].append(".")

    with open('day14.txt') as f:
        for i,line in enumerate(f):
            points = line.split(" -> ")
            path = []
            for p in points:
                x,y = [int(j) for j in p.split(",")]
                path.append((x,y))
            x = path[0][0]
            y = path[0][1]
            floor = max(floor,y)
            for p in path:
                if x > p[0]:
                    for j in range(x,p[0]-1,-1):
                        grid[y][j] = "#"
                elif x < p[0]:
                    for j in range(x,p[0]+1):
                        grid[y][j] = "#"
                elif y > p[1]:
                    for j in range(y,p[1]-1,-1):
                        grid[j][x] = "#"
                elif y < p[1]:
                    for j in range(y,p[1]+1):
                        grid[j][x] = "#"
                x = p[0]
                y = p[1]
                floor = max(floor,y)

    for x in range(1000):
        grid[floor+2][x] = "#"
                
    end = False
    while not end:
        sand = (500,0)
        while sand[1] < 999:
            if(grid[sand[1]+1][sand[0]] == "."):
                sand = (sand[0],sand[1]+1)
            elif(grid[sand[1]+1][sand[0]-1] == "."):
                sand = (sand[0]-1,sand[1]+1)
            elif(grid[sand[1]+1][sand[0]+1] == "."):
                sand = (sand[0]+1,sand[1]+1)
            else:
                grid[sand[1]][sand[0]] = "O"
                out += 1
                if(sand[1] == 0):
                    end = True
                break
            
    print(out)

    # write grid to file
    with open('day14Out.txt', 'w') as f:
        for y in range(1000):
            for x in range(1000):
                f.write(grid[y][x])
            f.write("\n")


main()