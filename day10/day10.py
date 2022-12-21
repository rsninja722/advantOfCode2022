
def main():
    # iterate through file lines
    out=0
    x = 1
    cycle = 0
    with open('day10.txt') as f:
        for i,line in enumerate(f):
            if line.startswith("noop"):
                cycle += 1
                if( (cycle + 20) %40 == 0):
                    out += x*cycle
            else:
                y = int(line.strip().split()[1])
                cycle += 1
                if( (cycle + 20) %40 == 0):
                    out += x*cycle
                cycle += 1
                if( (cycle + 20) %40 == 0):
                    out += x*cycle
                x += y
    print(out)

main()