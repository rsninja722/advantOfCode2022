rooms = {}
good = []
def main():
    with open('day16.txt') as f:
        for i,line in enumerate(f):
            parts = line.strip().split(" ")
            key = parts[1]
            flow = int(parts[4].replace("rate=","").replace(";",""))
            links = [x.replace(",","") for x in parts[9:]]
            rooms[key] = {"f":flow,"l":links}
            if(flow > 0):
                good.append(key)


    # time = 0
    # flow = 0
    # totalFlow = 0
    # cur = "AA"
    # while time < 30:
    #     if len(good) == 0:
    #         time += 1
    #         totalFlow += flow
    #     else:
    #         weights = []
    #         for i in good:
    #             if(i != cur):
    #                 weights.append([i,(29-time-bfs(cur,i))*rooms[i]["f"]])
    #         weights.sort(key=lambda x: x[1], reverse=True)

    #         print(weights)
    #         best = weights[0]
    #         for i in range(1+bfs(cur,best[0])):
    #             time += 1
    #             totalFlow += flow
    #             if(time == 30):
    #                 break
    #         cur = best[0]
    #         flow += rooms[cur]["f"]
    #         good.remove(cur)

    # print(totalFlow)


    paths = []
    # used, time, flow, total, cur
    paths.append([[],0,0,0,"AA",[]])
    done = False
    while not done:
        done = True
        newPaths = []
        for i in paths:
            if(i[1] < 30):
                done = False
                weights = []
                for j in good:
                    if(j != i[4] and j not in i[0]):
                        weights.append([j,bfs(i[4],j)])
                weights.sort(key=lambda x: x[1], reverse=True)

                if (len(weights) == 0):
                    i[1] = 30
                    newPaths.append(i)
                    continue
                j = 0
                while j < 15 and j < len(weights):
                    newPaths.append([i[0] + [weights[j][0]], i[1]+weights[j][1]+1, 0,0, weights[j][0]])
                    j += 1
            else:
                newPaths.append(i)
        paths = newPaths

    flows = []
    for i in paths:
        i[1] = 0
        cur = "AA"
        for j in i[0]:
            delta = bfs(cur,j)+1
            cur = j
            if(delta + i[1] > 29):
                delta = 30 - i[1]
            i[1] += delta
            i[3] += i[2] * delta
            i[2] += rooms[j]["f"]
        delta = 30 - i[1]
        i[3] += i[2] * delta
        flows.append(i[3])
    print(max(flows))
        


def bfs(start,end):
    visited = [start]
    dists = {start:0}
    queue = []
    queue.append(start)
    while queue:
        key = queue.pop(0)
        node = rooms[key]
        if key == end:
            return dists[end]
        for x in node["l"]:
            if x not in visited:
                queue.append(x)
                visited.append(x)
                dists[x] = dists[key] + 1


main()