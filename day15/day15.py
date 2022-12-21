
def main():
    out = 0
    pairs = []
    found = set()
    row = 2000000
    with open('day15.txt') as f:
        for i,line in enumerate(f):
            sx,sy,bx,by = (int(x) for x in line.strip().split(","))
            pairs.append([[sx,sy],[bx,by]])
    
    for p in pairs:

        start = (p[0][0] - md(p[0], p[1])) - abs(p[0][1] - row)
        end = (p[0][0] + md(p[0], p[1])) - abs(p[0][1] - row)

        if start <= end:
            for i in range(start-1, end+2):
                if(p[1][0] == i and p[1][1] == row):
                    continue
                if(md(p[0],p[1]) >= md(p[0], [i,row])):
                    found.add(i)

    print(len(found))


# manhattan distance
def md(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
main()