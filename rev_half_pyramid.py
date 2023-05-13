rows=int(input('Enter in how many rows you want to print your pattern: '))

k=rows
for i in range(1,rows+1):
    for j in range(1,k):
        print(end=" ")
    k=k-1
    for l in range(1,i+1):
        print('*',end="")
    print()