
def main():
    # iterate through file lines
    stacks = [[],[],[],[],[],[],[],[],[]]
    with open('day5.txt') as f:
        moves = False
        for line in f:
            if (line == "\n"):
                continue
            if moves:
                move = line.strip().split()
                temp = []
                for i in range(int(move[1])):
                    temp.append(stacks[int(move[3])-1].pop())
                temp.reverse()
                for i in temp:
                    stacks[int(move[5])-1].append(i)
            else:
                if(line[1] == '1'):
                    moves = True
                    for i in stacks:
                        i.reverse()
                        print(i)
                    continue
                for i in range(0, len(line), 4):
                    if(line[i+1] != ' '):
                        stacks[int(i/4)].append(line[i+1])

    out = ""
    for i in stacks:
        out += i[-1]
    print(out)

main()