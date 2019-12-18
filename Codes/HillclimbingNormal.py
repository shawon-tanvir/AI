from random import randint
from random import randrange
def frontcheck(Matrix,x,y):
    p=0
    for a in range(y+1,8):
        if(Matrix[x][a]==1):
            p=p+1;
    return p
def didowncheck(Matrix,x,y):
    q=0
    i=x+1
    j=y-1
    for c in range(8):
        if((i<8) & (j>=0)):
            if(Matrix[i][j]==1):
                q=q+1;
        i=i+1
        j=j-1
    
    return q
def diupcheck(Matrix,x,y):
    r=0
    i=x+1
    j=y+1
    for c in range(8):
        if((i<8) & (j<8)):
            if(Matrix[i][j]==1):
                r=r+1;
        i=i+1
        j=j+1
    
    return r
def queen(L):
    p=0;
    Matrix = [[0 for x in range(8)] for y in range(8)] 
    d=0
    for i in range(0,8): 
        ele = L[i]
        Matrix[8-ele][p]=1;
        p=p+1
    
    for j in range(8):
        for i in range(8):
            if(Matrix[i][j]==1 ):
                d=d+frontcheck(Matrix,i,j)+diupcheck(Matrix,i,j)+didowncheck(Matrix,i,j)
                continue
   
    return d
    



count=0

def start(res):
    mid=[None] * 8
    maximumarray=[None]*8
    maximum=0
    for i in range(8):
        
        for t in range(8):
            mid[t]=res[t]
        for j in range(1,9):
           if(res[i]!=j):
               mid[i]=j
               #del count
               count=0
               h=0
               #print(mid)
               count=queen(mid)
               h=28-count
               #print(h)
               if(h>maximum):
                   maximum=h
                   for t in range(8):
                       maximumarray[t]=mid[t]
       
    return(maximum,maximumarray)
          
s=input();
res = [int(sub) for sub in s]  
threshold=int(input()); 

  
while(1):
    (maximum,maximumarray)=start(res) 
    print(maximum)
    print(maximumarray)
    res=maximumarray
    if(maximum<threshold):  
        continue;
    elif(maximum==threshold):
        break

