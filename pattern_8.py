n=int(input("enter no:"))
for i in range(n):
        for j in range(i+1):
            print(" ",end="")
        for j in range(1,n-i):
            print("*",end="")
        print()