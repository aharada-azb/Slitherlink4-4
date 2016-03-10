N=4
M=4

col=[[0 for i in range(N)] for j in range(M+1)]
row=[[0 for i in range(N+1)] for j in range(M)]
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

for a in range(M):
    for b in range(N):
        if col[a][b]+row[a][b]+col[a+1][b]+row[a][b+1]==4:
            svg+='<text x="{0}" y="{1}" fill="black" font-size="4.5" >４</text>'.format(5*b+1,-5*a-1)
        elif col[a][b]+row[a][b]+col[a+1][b]+row[a][b+1]==3:
            svg+='<text x="{0}" y="{1}" fill="black" font-size="4.5" >３</text>'.format(5*b+1,-5*a-1)    
        elif col[a][b]+row[a][b]+col[a+1][b]+row[a][b+1]==2:
            svg+='<text x="{0}" y="{1}" fill="black" font-size="4.5" >２</text>'.format(5*b+1,-5*a-1)
        elif col[a][b]+row[a][b]+col[a+1][b]+row[a][b+1]==1:
            svg+='<text x="{0}" y="{1}" fill="black" font-size="4.5" >１</text>'.format(5*b+1,-5*a-1)
        else :
            svg+='<text x="{0}" y="{1}" fill="black" font-size="4.5" >０</text>'.format(5*b+1,-5*a-1)

svg+='</svg>'

f=open("graphic_ver3.svg", "w", encoding="UTF-8")
f.write(svg)
f.close()
