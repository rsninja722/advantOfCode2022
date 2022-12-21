def main():
    max = 0
    # iterate through file lines
    with open('day1.txt') as f:
        sum = 0
        for line in f:
            if not line.strip() == "":
                sum += int(line)
                if sum > max:
                    max = sum
            else:
                sum = 0 
    print(max)

main()