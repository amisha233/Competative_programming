num=int(input("enter no:"))
sum=0
while(num>0):
    digit=num%10
    num=num//10
    sum=sum+digit
print(sum)