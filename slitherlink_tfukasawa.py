#スリザーリンク4*4のmaster
N=4
M=4
col=[[0 for i in range(N)] for j in range(M+1)]
row=[[0 for i in range(N+1)] for j in range(M)]

judge_col = {}
judge_row = {}


numbers = {}    #DICTIONARY

for n in range(4):  #DEFINE NUMBERS 0~3

    while True:     
        print('Please enter the x-coordinate of a figure "',n,'". Or enter "q" to go next step.')
    
        i = input("")
    
        if i == "q":
            break
    
        elif 0 <= int(i) <= M:
        
            x = int(i)
        
            print('Please enter the y-coordinate of the figure.')
        
            i = int(input())
        
            if 0 <= i <=  N:

                y = i

                numbers[(x,y)] = n

                print('(',x,',',y,') = ',n)

            else:
                print('You entered a wrong number.It must be 0 to ',N,'.')

        else:
            print('You entered a wrong number.It must be 0 to ',M,'.')

#DEFINITION END

keys = list(numbers.keys())

values = list(numbers.values())

def judge_zero(tuple):
    s = tuple[0]
    t = tuple[1]
    judge_col[(s,t)] = False
    judge_col[(s,t+1)] = False
    judge_row[(s,t)] = False
    judge_row[(s+1,t)] = False

for i in range(len(values)):
    if values[i] == 0:
        judge_zero(keys[i])

    elif values[i] == max(values):
        P = keys[i]

print(P)



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
