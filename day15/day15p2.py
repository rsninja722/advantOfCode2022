
def main():
    pairs = []
    row = 0
    height = 4000000
    with open('day15.txt') as f:
        for i,line in enumerate(f):
            sx,sy,bx,by = (int(x) for x in line.strip().split(","))
            pairs.append([[sx,sy],[bx,by]])
    found = False
    for i in range(0,height):
        row = i
        ranges = []
        for p in pairs:

            start = max(0,(p[0][0] - md(p[0], p[1])) + abs(p[0][1] - row))
            end = min(height,(p[0][0] + md(p[0], p[1])) - abs(p[0][1] - row))

            if start <= end and md(p[0],[p[0][0],row]) <= md(p[0],p[1]):
                ranges.append([start,end])
        

        ranges.sort(key=lambda x: x[0])
        if(ranges[0][0] != 0):
            print(ranges[0][0], row)
            break
        start = ranges[0][1]
        for r in range(1,len(ranges)):
            if(start+1 >= ranges[r][0]):
                start = max(ranges[r][1], start)
            else:
                print(start+1, row)
                found = True
                break
        if(found):
            break
        if(start != height):
            print(start+1, row)
            break


# manhattan distance
def md(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
main()