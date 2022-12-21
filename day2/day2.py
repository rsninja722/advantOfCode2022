# a x rock 1
# b y paper 2
# c z scissors 3



def main():
    # iterate through file lines
    with open('day2.txt') as f:
        sum = 0
        for line in f:
            a,c = line.strip().split()
            b = ""

            if (c == "X"):
                if(a=="A"):
                    b = "Z"
                elif(a=="B"):
                    b = "X"
                elif(a=="C"):
                    b = "Y"
            elif (c == "Y"):
                if(a=="A"):
                    b = "X"
                elif(a=="B"):
                    b = "Y"
                elif(a=="C"):
                    b = "Z"
            elif (c == "Z"):
                if(a=="A"):
                    b = "Y"
                elif(a=="B"):
                    b = "Z"
                elif(a=="C"):
                    b = "X"

            if(a == "A" and b == "X"):
                sum += 4
            elif(a == "A" and b == "Y"):
                sum += 8
            elif(a == "A" and b == "Z"):
                sum += 3
            elif(a == "B" and b == "X"):
                sum += 1
            elif(a == "B" and b == "Y"):
                sum += 5
            elif(a == "B" and b == "Z"):
                sum += 9
            elif(a == "C" and b == "X"):
                sum += 7
            elif(a == "C" and b == "Y"):
                sum += 2
            elif(a == "C" and b == "Z"):
                sum += 6
    print(sum)

main()