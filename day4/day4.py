
def main():
    # iterate through file lines
    with open('day4.txt') as f:
        sum = 0
        for line in f:
            x,y = line.split(',')
            a,b = x.split('-')
            c,d = y.split('-')
            # if( (int(a) >= int(c) and int(b) <= int(d)) or (int(c) >= int(a) and int(d) <= int(b))):
            found = False
            for i in range(int(a),int(b)+1):
                for j in range(int(c),int(d)+1):
                    if(i == j):
                        sum += 1
                        found = True
                        break
                if(found):
                    break
    print(sum)

main()