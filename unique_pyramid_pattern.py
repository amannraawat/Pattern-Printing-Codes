rows = int(input('Enter in how many rows you want to print your pattern: '))

m=0
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end='')
    for k in range(m,0,-1):
        print(k,end='')
    m=m+1
    print()
        
    