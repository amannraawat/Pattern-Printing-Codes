rows = int(input('Enter in how many rows you want to print your pattern: '))

for i in range(rows,0,-1):
    for j in range(0,i):
        print(i,end='')
    print()