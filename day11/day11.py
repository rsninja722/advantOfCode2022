
def main():
    monkeys = []
    inspections = []
    with open('day11.txt') as f:
        monk = -1
        for i,line in enumerate(f):
            split = line.strip().split()
            if(split[0] == "Monkey"):
                monkeys.append({"items":[],"operation":{"left":"","op":"","right":""},"test":0,"true":0,"false":0})
                inspections.append(0)
                monk += 1
            elif(split[0] == "Starting"):
                for j in range(2,len(split)):
                    monkeys[monk]["items"].append(int(split[j].replace(",","")))
            elif(split[0] == "Operation:"):
                monkeys[monk]["operation"]["left"] = split[3]
                monkeys[monk]["operation"]["op"] = split[4]
                monkeys[monk]["operation"]["right"] = split[5]

                if(monkeys[monk]["operation"]["right"] != "old"):
                    monkeys[monk]["operation"]["right"] = int(monkeys[monk]["operation"]["right"])
            elif(split[0] == "Test:"):
                monkeys[monk]["test"] = int(split[3])
            elif(split[1] == "true:"):
                monkeys[monk]["true"] = int(split[5])
            elif(split[1] == "false:"):
                monkeys[monk]["false"] = int(split[5])
    
    for j in range(20):
        for i,m in enumerate(monkeys):
            o = m["operation"]
            for item in range(len(m["items"])):
                right = 0
                if(o["right"] == "old"):
                    right = m["items"][item]
                else:
                    right = m["operation"]["right"]
                if(o["op"] == "*"):
                    m["items"][item] = m["items"][item] * right
                else:
                    m["items"][item] = m["items"][item] + right

                m["items"][item] = m["items"][item] // 3

                if(m["items"][item] % m["test"] == 0):
                    monkeys[m["true"]]["items"].append(m["items"][item])
                else:
                    monkeys[m["false"]]["items"].append(m["items"][item])
                
                inspections[i] += 1
            m["items"] = []

    inspections.sort()
    print(inspections[-1] * inspections[-2])
    print(inspections)

main()