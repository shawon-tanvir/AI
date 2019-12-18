def sum1(N,I,F):
    if (N==0):
        return 0
    elif (N>=1):
        return sum1(N-1,I,F)+F+(N-1)*I
# Main
f=int(input('First element:'))
d=int(input('Interval:'))
n=int(input('n:'))
print('Series sum:', sum1(n,d,f))
