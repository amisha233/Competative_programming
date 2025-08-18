num=int(input("enter no:"))
rev=0
while(num>0):
    digit=num%10
    num=num//10
    rev=rev*10+digit
print(rev)