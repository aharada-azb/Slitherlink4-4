#スリザーリンク4*4のmaster
N=4
M=4
col=[[1 for i in range(N)] for j in range(M+1)]
row=[[1 for i in range(N+1)] for j in range(M)]

def link(s,t):
    if s<N and t<M:
        c=col[s][t]+col[s][t-1]+row[s][t]+row[s-1][t]
    elif s==N and t!=M:
        c=col[s][t]+col[s][t-1]+row[s-1][t]
    elif s!=N and t==M:
        c=col[s][t-1]+row[s][t]+row[s-1][t]
    else:
        c=col[s][t-1]+row[s-1][t]
    
    if c==0 or c==2:
        return True
    else:
        return False
        
def allink(s,t):
    for i in range(s):
        for j in range(t):
            if link(i,j)==False:
                return False

def solved(a):
    if a==None:
        print(col)
        print(row)
    else:
        print("unsolved")

solved(allink(N+1,M+1))
