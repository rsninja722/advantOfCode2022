
def main():
    # iterate through file lines
    out=0
    v = []
    t = []
    with open('day8.txt') as f:
        for i,line in enumerate(f):
            t.append([])
            v.append([])
            for j in range(len(line.strip())):
                t[i].append(int(line[j]))
                v[i].append(False)

    for i in range(len(t[0])):
        h = -1
        for j in range(len(t)):
            if(t[j][i] > h):
                v[j][i] = True
                h= t[j][i]
        # iterate backwards through t
        h = -1
        for j in range(len(t)-1, -1, -1):
            if(t[j][i] > h):
                v[j][i] = True
                h= t[j][i]
    # iterate horizontally
    for i in range(len(t)):
        h = -1
        for j in range(len(t[0])):
            if(t[i][j] > h):
                v[i][j] = True
                h= t[i][j]
        # iterate backwards through t
        h = -1
        for j in range(len(t[0])-1, -1, -1):
            if(t[i][j] > h):
                v[i][j] = True
                h= t[i][j]

    for i in range(len(t)):
        for j in range(len(t[0])):
            if(v[i][j]):
                out += 1

    print(out)

main()