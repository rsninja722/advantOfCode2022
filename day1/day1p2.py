def main():
    scores = []
    # iterate through file lines
    with open('day1.txt') as f:
        sum = 0
        for line in f:
            if not line.strip() == "":
                sum += int(line)
            else:
                scores.append(sum)
                sum = 0
        scores.append(sum)
    scores.sort()
    print(scores[-1]+scores[-2]+scores[-3])

main()