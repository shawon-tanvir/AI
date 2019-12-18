touplelist1 =[('P','Q'),('S','T')];
clause =[("C","L","P"),("D","M","P"),("B","L","M"),("A","P","L"),("A","B","L"),("A","D","G"),("G","B","C"),("!S","A","Z")];
fact=['A','B','C','D','!T'];
f1=open("fn.txt", "w");
def modpon():
    global loop1;
    global result;
    print(len(fact));
    for j in range(len(fact)):       
        if(loop1==1):
            break;    
        for l in range(len(touplelist1)):        
            if(fact[j]==touplelist1[l][0]):      
                if(touplelist1[l][1] not in fact):
                    fact.append(touplelist1[l][1]);
                    print(fact, end="\n", file=f1);
                    if(touplelist1[l][1]==x):
                        
                        loop1=1;
                        result=x;
                        break;
def modtol():
    global loop1;
    global result;
    for j in range(len(fact)):
        if(loop1==1):
            break;    
        for l in range(len(touplelist1)):         
            if(fact[j]=='!'+touplelist1[l][1]):
                if('!'+touplelist1[l][0] not in fact):
                    fact.append('!'+touplelist1[l][0]);
                    print(fact, end="\n", file=f1);
                    if('!'+touplelist1[l][0]==x):
                        loop1=1;
                        result=x;
                        break;
                        
def simplification():
    global loop1;
    global loop2;
    global result;
    j=0;
    index=len(fact)-1;
    index2=len(fact);
    while j<index:
        print('check '+fact[j]);
        if(loop1==1):
            break;
        k=0;
        while k<index2:
            
            if(loop2==1):
                loop1=1;
                break;
            for l in range(len(clause)):                
                if((fact[j]==clause[l][0]) & (fact[k]==clause[l][1])):
                    if(clause[l][2] not in fact):                   
                        fact.append(clause[l][2]);
                        index=index+1;
                        index2=index2+1;
                        #print(index2);
                        print(fact, end="\n", file=f1);
                        if(clause[l][2]==x):                            
                            loop2=1;
                            print(clause[l][2]);
                            result=x;
                            print(x)
                            break;
                else:
                    continue;
            k=k+1;
        j=j+1;

#Main
loop1=0;
loop2=0;
result='a';
x=input("Enter a query: ");

for j in range(len(fact)):    
    if(fact[j]==x):
        result=x;
if(result!=x):
    modpon();
    
if(result!=x):
    modtol();

if(result!=x):
    simplification();
if(result!=x):
    modpon();
f1.close
if(result==x):
    print(x +' can be derived');
else:
    print(x +' can not be derived');
