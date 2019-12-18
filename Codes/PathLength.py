neighbour=[('i','a',35),('i','b',45),('a','c',20),('a','d',30),('b','d',25),
           ('b','e',35),('b','f',27),('c','g',47),('c','d',30),('d','g',30),('e','g',25)]
def path(X):
    global Y
    global F
    for i in range(11):
        if((neighbour[i][0]==X) & (neighbour[i][1]==Y)):
            return neighbour[i][2]
        elif((neighbour[i][0]==X) & (neighbour[i][1]!=Y)):
            return path(neighbour[i][1])+neighbour[i][2]
                           
# Main
F=0
S=str(input('First Node? '))
Y=str(input('Last Node? '))
print('L:', path(S))
