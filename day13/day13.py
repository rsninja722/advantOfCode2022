
def main():
    out = 0
    left = 0
    right = 0
    index = 1
    with open('day13.txt') as f:
        for i,line in enumerate(f):
            if (line == "\n"):
                left = 0
                right = 0
                index += 1
                continue
            if(left == 0):
                left = eval(line)
            else:
                right = eval(line)
                val = compare(left, right)
                print(val)
                if(val == 2 or val == 1):
                    out += index
    print(out)

def compare(left, right):
    for i in range(len(left)):
        if(i == len(right)):
            return 0
        leftIsList = isinstance(left[i], list)
        rightIsList = isinstance(right[i], list)
        if(leftIsList and rightIsList):
            val = compare(left[i], right[i])
            if(val != 2):
                return val
        elif(leftIsList):
            val = compare(left[i], [right[i]])
            if(val != 2):
                return val
        elif(rightIsList):
            val = compare([left[i]], right[i])
            if(val != 2):
                return val
        else:
            if(left[i] > right[i]):
                return 0
            elif(left[i] < right[i]):
                return 1
            else:
                continue
    return 2 if len(left) == len(right) else 1
main()