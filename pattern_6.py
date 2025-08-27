n=int(input("enter no:"))
for i in range(n):
        print("*",end="")
        for j in range(n-i):
            print(" ",end="")
        print("*")