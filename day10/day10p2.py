
def main():
    # iterate through file lines
    out=""
    x = 1
    cycle = 0
    rowPos = 0
    
    with open('day10.txt') as f:
        for i,line in enumerate(f):
            if line.startswith("noop"):
                cycle += 1
                if(abs(rowPos - x) < 2):
                    out += "#"
                else:
                    out += "."
                rowPos += 1
                if(cycle %40 == 0):
                    rowPos = 0
                    out += "\n"
            else:
                y = int(line.strip().split()[1])
                cycle += 1
                if(abs(rowPos - x) < 2):
                    out += "#"
                else:
                    out += "."
                rowPos += 1
                if( cycle %40 == 0):
                    rowPos = 0
                    out += "\n"
                cycle += 1
                if(abs(rowPos - x) < 2):
                    out += "#"
                else:
                    out += "."
                rowPos += 1
                if( cycle%40 == 0):
                    rowPos = 0
                    out += "\n"
                x += y
    print(out)

main()