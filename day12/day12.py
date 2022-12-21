
def main():
    out = 0
    ter = []
    start = []
    end = []
    with open('day12.txt') as f:
        for r,line in enumerate(f):
            ter.append([])
            for c in range(len(line.strip())):
                if(line[c] == 'S'):
                    ter[r].append(1)
                    start = [r,c]
                elif(line[c] == 'E'):
                    ter[r].append(26)
                    end = [r,c]
                else:
                    ter[r].append(ord(line[c])-96)
    # then I gave up and did it manually
    print(ter)
    print(out)

main()