
def main():
    # iterate through file lines
    biggest=0
    v = []
    t = []
    with open('day8.txt') as f:
        for i,line in enumerate(f):
            t.append([])
            v.append([])
            for j in range(len(line.strip())):
                t[i].append(int(line[j]))
                v[i].append(False)

    for i in range(len(t)):
        for j in range(len(t[0])):
            # up from i,j
            h = t[i][j]
            d1 = 0
            for k in range(i-1, -1, -1):
                if(h > t[k][j]):
                    d1 += 1
                else:
                    d1 += 1
                    break
            # down from i,j
            d2 = 0
            for k in range(i+1, len(t)):
                if(h > t[k][j]):
                    d2 += 1
                else:
                    d2 += 1
                    break
            # left from i,j
            d3 = 0
            for k in range(j-1, -1, -1):
                if(h > t[i][k]):
                    d3 += 1
                else:
                    d3 += 1
                    break
            # right from i,j
            d4 = 0
            for k in range(j+1, len(t[0])):
                if(h > t[i][k]):
                    d4 += 1
                else:
                    d4 += 1
                    break

            if(d1*d2*d3*d4 > biggest):
                biggest = d1*d2*d3*d4

    print(biggest)

main()