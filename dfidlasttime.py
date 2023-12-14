graph={0:[1,2],
       1:[3,4,0],
       2:[0,5,6],
       3:[1,7,8],
       4:[1],
       5:[2],
       6:[2,9],
       7:[3],
       8:[3],
       9:[6]
       }
flag=0

def dfif(graph,current,end,visited):
    global flag 
    if(flag==1):
        return
    if(current==end):
        print(current)
        flag=1
        return
    if current not in visited and flag==0:
        print("\n",current,end=' ->')
        visited.add(current)
        for neb in graph[current]:
            print("[",neb,end='] ')
            if neb not in visited and flag==0:
                dfif(graph,neb,end,visited)


start=0
end=9
visites=set()




dfif(graph,start,end,visites)