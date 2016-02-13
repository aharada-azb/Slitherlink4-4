#スリザーリンク4*4のmaster
N=4
M=4
col=[[0 for i in range(N)] for j in range(M+1)]
row=[[0 for i in range(N+1)] for j in range(M)]

judge_col = {}
judge_row = {}

for i in range(5):
    for j in range(5):
        judge_col[(i,j)] = True
        judge_row[(i,j)] = False

def line_up(s,t):
    if (judge_row[(s,t)] == True) and (row[s][t] == 0):
        row[s][t] = 1
        return True
    else:
        return False

def line_right(s,t):
    if (judge_col[(s,t)] == True) and (col[s][t] == 0):
        col[s][t] = 1
        return True
    else:
        return False

def line_down(s,t):
    if (judge_row[(s-1,t)] == True) and (row[s-1][t] == 0):
        row[s-1][t] = 1
        return True
    else:
        return False

def line_left(s,t):
    if (judge_col[(s,t-1)] == True) and (col[s][t-1] ==　0):
        col[s][t-1] = 1
        return True
    else:
        return False

def line_pre_false(s,t):
    if col[s][t] == 1:
        judge_col[(s,t)] = False
    elif col[s][t-1] == 1:
        judge_col[(s,t-1)] = False
    elif row[s][t] == 1:
        judge_row[(s,t)] = False
    elif row[s-1][t] ==1:
        judge_row[(s-1,t)] = False
    else:
        print("error")
    

def line_main(x,y):
    if line_up(x,y):
        return (x,y+1)
    if line_right(x,y):
        return (x+1,y)
    if line_down(x,y):
        return (x,y-1)
    if line_left(x,y):
        return (x-1,y)
    
                    
def line_all(x,y):
    (x1,y1) = line_main(x,y)
    line_all(x1,y1)
    

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
