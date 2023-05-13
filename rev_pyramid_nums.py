rows=int(input('Enter in how many rows you want to print your pattern: '))

m=1
for i in range(1,rows+1):
    for j in range(m,0,-1):
        print(j,end='')
    m=m+1
    print()