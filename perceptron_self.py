w=[1,-1,0,0.5]

x1=[1,-2,0,-1]
x2=[0,1.5,-0.5,-1]
x3=[-1,1,0.5,-1]

X=[x1,x2,x3]
c=0.1
d=[-1,-1,1]

for i in range(len(d)):
    res=0
    for x in range(len(w)):
        res+=w[x]*X[i][x]
    oi=-1
    if res>0:
        oi=1
    mWithx=c*(d[i]-oi)
    print(oi)
    if mWithx>=0:
        mMatrix=[]
        for p in range(len(x1)):
            mMatrix.append(mWithx*X[i][p])
        for wi in range(len(w)):
            w[wi]=w[wi]+mMatrix[wi]
    if mWithx<0:
        mWithx=abs(mWithx)
        mMatrix=[]
        for p in range(len(x1)):
            mMatrix.append(mWithx*X[i][p])  
        for wi in range(len(w)):
            w[wi]=w[wi]-mMatrix[wi]
    print(f"W{i+1} =")        
    print(w)        




