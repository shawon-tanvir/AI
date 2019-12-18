initial=[(1,1,2),(2,1,3),(3,2,1),(4,2,3),(5,3,3),(6,2,2),(7,3,2),(8,1,1)]
goal=[(1,1,1),(2,1,2),(3,1,3),(4,2,3),(5,3,3),(6,3,2),(7,3,1),(8,2,1)]
T=1
ssum=0;
for i in range(8):
    if(initial[i][0]==T & goal[i][0]==T ):      
      ssum=ssum+abs(initial[i][1]-goal[i][1])+abs(initial[i][2]-goal[i][2])
    T=T+1
print('Heuristics =',end=' ')
print(ssum)
    
