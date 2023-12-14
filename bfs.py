graph={0:[1,2],
       1:[3,4,0],
       2:[0,5,6],
       3:[],
       4:[],
       5:[],
       6:[]}
visited=[]
queue=[]

start=0
stop=4
queue.append(start)

while queue:
    lme=queue.pop(0)
    visited.append(lme)
    if lme==stop:
        break
    for n in graph[lme]:
        if n not in visited and n not in queue:
            queue.append(n)

print(visited)