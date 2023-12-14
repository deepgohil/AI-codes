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
queue=set()
def dfif(graph,start,end,visited,i):
    if(start==end):
        print(start)
        print("found :")
        return
    if(i==0):
        return 
    if start not in visited:
        print(start)
        visited.add(start)
        for n in graph[start]:
            print("open list",n)
            if n not in visited:
                dfif(graph,n,end,visited,i-1)   
    return

start=0
end=4
visites=set()




dfif(graph,start,end,visites,3)
