#スリザーリンク4*4のmaster
N=4
M=4
col=[[0 for i in range(N)] for j in range(M+1)]
row=[[0 for i in range(N+1)] for j in range(M)]

judge_col = {}
judge_row = {}

#引けないところの線の座標を辞書に加える
for i in range(5):
    for j in range(5):
        judge_col[(i,j)] = True
        judge_row[(i,j)] = True

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


#線を上下左右に引く関数を生成
def line_up(s,t):
    if s>N-1 or t>M:
        return False
    if (judge_row[(s,t)] == True) and (row[s][t] == 0):
        row[s][t] = 1
        judge_col[(s,t)] = False
        judge_col[(s,t-1)] = False
        return True
    else:
        return False

def line_right(s,t):
    if s>N or t>M-1:
        return False
    if (judge_col[(s,t)] == True) and (col[s][t] == 0):
        col[s][t] = 1
        judge_row[(s,t)] = False
        judge_row[(s-1,t)] = False
        return True
    else:
        return False

def line_down(s,t):
    if s<1 or t<0 or s>N or t>M:
        return False
    if (judge_row[(s-1,t)] == True) and (row[s-1][t] == 0):
        row[s-1][t] = 1
        judge_col[(s,t)] = False
        if t>0:
            judge_col[(s,t-1)] = False
        return True
    else:
        return False

def line_left(s,t):
    if t<1 or s<0 or s>N or t>M:
        return False
    if (judge_col[(s,t-1)] == True) and (col[s][t-1] == 0):
        col[s][t-1] = 1
        judge_row[(s,t)] = False
        if s>0:
            judge_row[(s-1,t)] = False
        return True
    else:
        return False


#どこの点にもすすめなくなった時に１つ前の点の座標を返す関数
def line_pre_false(x,y):
    if row[x][y] == 1:
        judge_row[(x,y)] = False
        row[x][y] = 0
        return (x+1,y)
    elif col[x][y] == 1:
        judge_col[(x,y)] = False
        col[x][y] = 0
        return (x,y+1)
    elif row[x-1][y] == 1:
        judge_row[(x-1,y)] = False
        row[x-1][y] = 0
        return (x-1,y)
    elif col[x][y-1] == 1:
        judge_col[(x,y-1)] = False
        col[x][y-1]
        return (x,y-1)
    else:
        print("error")

    
#ある点について線を上、右、下、左の順に引けるか試していく関数
def line_main(x,y):
    if line_up(x,y):
        print(col,row)
        print()
        return (x+1,y)
    if line_right(x,y):
        print(col,row)
        print()
        return (x,y+1)
    if line_down(x,y):
        print(col,row)
        print()
        return (x-1,y)
    if line_left(x,y):
        print(col,row)
        print()
        return (x,y-1)
    else:
        return False
        
    
#再帰定義によって次々に線を引いていく関数
def line_all(x,y):
    global tmp
    tmp = line_main(x,y)
    if allink(N,M):
            return
    if tmp == False:
        (x1,y1) = line_pre_false(x,y)
        line_all(x1,y1)
    else:
        (x2,y2) = tmp
        line_all(x2,y2)


#全部の線がつながっているか確認（再帰関数の終了条件）        
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


#
print(col,row)
print()
line_all(0,0)


def solved(a):
    if a==None:
        print(col)
        print(row)
    else:
        print("unsolved")

solved(allink(N+1,M+1))
