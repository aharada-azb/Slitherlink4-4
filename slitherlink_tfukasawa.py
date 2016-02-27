#slitherlinkのmaster
N=4
M=4
col=[[0 for i in range(N)] for j in range(M+1)]
row=[[0 for i in range(N+1)] for j in range(M)]

judge_col = {}
judge_row = {}

#引けないところの線の座標を辞書に加える
for i in range(-1,N+2):
    for j in range(-1,M+2):
        judge_col[(i,j)] = 0
        judge_row[(i,j)] = 0

numbers = {}    #中の数字の辞書を定義

for s in range(M):
    for t in range(N):
        numbers[(s,t)] = True

#0~3の数字の座標を入力させる
for n in range(4):

    while True:     
        print(n,'のX座標を入力して下さい。無い場合はQキーを入力して下さい。')
    
        i = input("")
    
        if i == "q":
            break
    
        elif 0 <= int(i) <= M-1:
        
            x = int(i)
        
            print('Y座標を入力して下さい。')
        
            i = int(input())
        
            if 0 <= i <=  N-1:

                y = i

                numbers[(x,y)] = n

                print('(',x,',',y,') = ',n)

            else:
                print('数値が正しくありません。')

        else:
            print('数値が正しくありません。')

keys = list(numbers.keys())     #座標のリスト

values = list(numbers.values())     #数字のリスト

#0の周りをFalseにする関数
def judge_zero(tuple):

    s = tuple[0]
    t = tuple[1]

    judge_col[(s,t)] +=1
    judge_col[(s,t+1)] +=1
    judge_row[(s,t)] +=1
    judge_row[(s+1,t)] +=1

#すべての0について判定し辺にFalseを代入
for i in range(len(values)):

    if values[i] == 0:
        judge_zero(keys[i])


#線を上下左右に引く関数を生成
def line_up(s,t):
    if s>N-1 or t>M:
        return False
    if (judge_row[(s,t)] == 0) and (row[s][t] == 0):
        row[s][t] = 1
        judge_col[(s,t)] += 1
        judge_col[(s,t-1)] +=1
        return True
    else:
        return False

def line_right(s,t):
    if s>N or t>M-1:
        return False
    if (judge_col[(s,t)] == 0) and (col[s][t] == 0):
        col[s][t] = 1
        judge_row[(s,t)] += 1
        judge_row[(s-1,t)] +=1
        return True
    else:
        return False

def line_down(s,t):
    if s<1 or t<0 or s>N or t>M:
        return False
    if (judge_row[(s-1,t)] == 0) and (row[s-1][t] == 0):
        row[s-1][t] = 1
        judge_col[(s,t)] +=1
        if t>0:
            judge_col[(s,t-1)] +=1
        return True
    else:
        return False

def line_left(s,t):
    if t<1 or s<0 or s>N or t>M:
        return False
    if (judge_col[(s,t-1)] == 0) and (col[s][t-1] == 0):
        col[s][t-1] = 1
        judge_row[(s,t)] += 1
        if s>0:
            judge_row[(s-1,t)] +=1
        return True
    else:
        return False


#どこの点にもすすめなくなった時に１つ前の点の座標を返す関数
def line_pre_false(x,y):
    if row[x][y] == 1:
        judge_row[(x,y)] += 1
        if judge_col[(x+1,y)] >0:
            judge_col[(x+1,y)] -= 1
        if judge_col[(x+1,y-1)] >0:
            judge_col[(x+1,y-1)] -= 1
        row[x][y] = 0
        return (x+1,y)
    elif col[x][y] == 1:
        judge_col[(x,y)] += 1
        if judge_row[(x,y+1)] >0:
            judge_row[(x,y+1)] -= 1
        if judge_row[(x-1,y+1)] >0:
            judge_row[(x-1,y+1)] -= 1
        col[x][y] = 0
        return (x,y+1)
    elif row[x-1][y] == 1:
        judge_row[(x-1,y)] += 1
        if judge_col[(x-1,y)] >0:
            judge_col[(x-1,y)] -= 1
        if judge_col[(x-1,y-1)] >0:
            judge_col[(x-1,y-1)] -= 1
        row[x-1][y] = 0
        return (x-1,y)
    elif col[x][y-1] == 1:
        judge_col[(x,y-1)] += 1
        if judge_row[(x,y-1)] >0:
            judge_row[(x,y-1)] -= 1
        if judge_row[(x-1,y-1)] >0:
            judge_row[(x-1,y-1)] -= 1
        col[x][y-1]
        return (x,y-1)

    
#ある点について線を上、右、下、左の順に引けるか試していく関数
def line_main(x,y):
    if line_up(x,y):
        return (x+1,y)
    if line_right(x,y):
        return (x,y+1)
    if line_down(x,y):
        return (x-1,y)
    if line_left(x,y):
        return (x,y-1)
    else:
        return False
        
    
#再帰定義によって次々に線を引いていく関数
def line_all(x,y):
    global tmp
    tmp = line_main(x,y)
    if allink(N,M) != False:
            return
    if tmp == False:
        (x1,y1) = line_pre_false(x,y)
        line_all(x1,y1)
    else:
        (x2,y2) = tmp
        line_all(x2,y2)


#全部の線がつながっているか確認（再帰関数の終了条件）        
def link(s,t):
    global c
    if 0<s<N and 0<t<M:
        c=col[s][t]+col[s][t-1]+row[s][t]+row[s-1][t]
    elif s==0 and t==0:
        c=col[s][t]+row[s][t]
    elif s==0:
        c=col[s][t]+col[s][t-1]+row[s][t]
    elif t==0:
        c=col[s][t]+row[s][t]+row[s-1][t]
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
row[0][0]=1

line_all(1,0)

svg='<?xml version="1.0" encoding="utf-8"?>'
svg +='''
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'''
svg +='''
<svg xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    width="1000" height="1000" viewBox="-5 -55 55 60" >
'''


for a in range(M+1):
    for b in range(N+1):
        svg+='<rect x="{0}" y="{1}" width="0.5" height="0.5" fill="black" />'.format(5*a-0.25,-5*b-0.25)

for b in range(N+1):
    for a in range(M):
        if col[b][a]==1:
            svg+='<line x1="{0}" y1="{1}" x2="{2}" y2="{1}" stroke="black" stroke-width="0.2" />'.format(5*a,-5*b,5*(a+1))
        
        else :
            svg+='<line x1="{0}" y1="{1}" x2="{2}" y2="{3}" stroke="black" stroke-width="0.2"  />'.format(5*a+2,-5*b+0.5,5*(a+1)-2,-5*b-0.5)
            svg+='<line x1="{0}" y1="{1}" x2="{2}" y2="{3}" stroke="black" stroke-width="0.2"  />'.format(5*a+2,-5*b-0.5,5*(a+1)-2,-5*b+0.5)
for b in range(N):
    for a in range(M+1):
        if row[b][a]==1:
            svg+='<line x1="{0}" y1="{1}" x2="{0}" y2="{2}" stroke="black" stroke-width="0.2" />'.format(5*a,-5*b,-5*(b+1))
        
        else :
            svg+='<line x1="{0}" y1="{1}" x2="{2}" y2="{3}" stroke="black" stroke-width="0.2" />'.format(5*a-0.5,-5*b-2,5*a+0.5,-5*(b+1)+2)
            svg+='<line x1="{0}" y1="{1}" x2="{2}" y2="{3}" stroke="black" stroke-width="0.2" />'.format(5*a+0.5,-5*b-2,5*a-0.5,-5*(b+1)+2)

svg+='</svg>'

f=open("graphic_ver2.svg", "w", encoding="UTF-8")
f.write(svg)
f.close()
