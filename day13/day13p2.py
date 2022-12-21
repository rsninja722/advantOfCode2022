from functools import cmp_to_key

def main():
    out = 1
    left = 0
    right = 0
    index = 1
    signals = []
    with open('day13p2.txt') as f:
        for i,line in enumerate(f):
            if (line == "\n"):
                continue
            signals.append(eval(line))

    compare_cmp_key = cmp_to_key(between)
    signals.sort(key=compare_cmp_key)
    
    for index,i in enumerate(signals):
        if(len(i) == 1):
            if(len(i[0]) == 1):
                if(i[0][0] == 2 or i[0][0] == 6):
                    out *= index+1

    print(out)

def between(a, b):
    val = compare(a, b)
    if(val == 2 or val == 1):
        return -1
    else:
        return 1

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