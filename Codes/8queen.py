def frontcheck(x,y):
    global Matrix
    global count
    for a in range(y+1,8):
        if(Matrix[x][a]==1):
            count=count+1;
    print(count)
def didowncheck(x,y):
    global Matrix
    global count
    i=x+1
    j=y-1
    for c in range(8):
        if((i<8) & (j>=0)):
            if(Matrix[i][j]==1):
                count=count+1;
        i=i+1
        j=j-1
    print(count)
def diupcheck(x,y):
    global Matrix
    global count
    i=x+1
    j=y+1
    for c in range(8):
        if((i<8) & (j<8)):
            if(Matrix[i][j]==1):
                count=count+1;
        i=i+1
        j=j+1
    print(count)

# 
p=0;
count=0;
Matrix = [[0 for x in range(8)] for y in range(8)] 
for i in range(0,8): 
    ele = int(input()) 
    Matrix[8-ele][p]=1;
    p=p+1
for j in range(8):
    for i in range(8):
        if(Matrix[i][j]==1):
             frontcheck(i,j)
             diupcheck(i,j)
             didowncheck(i,j)
             continue
print("Attacking: ",end='')
print(count)

