rows=int(input('Enter in how many rows you want to print your pattern: '))

for i in range(1,rows+1):
    for j in range(1,i+1,1):
        print(i,end='')
    print()