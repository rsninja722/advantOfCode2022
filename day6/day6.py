
def main():
    # iterate through file lines
    out=0
    buff = []
    with open('day6.txt') as f:
        for line in f:
            for i in range(len(line)):
                print(buff)
                if(len(buff) == 14):
                    if(len(set(buff)) == 14):
                        out = i
                        break
                    buff.pop(0)
                buff.append(line[i])

    print(out)

main()