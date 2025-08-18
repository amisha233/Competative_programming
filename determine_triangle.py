a=int(input("enter angle 1 :"))
b=int(input("enter angle 2 :"))
c=int(input("enter angle 3 :"))
if a==90 or b==90 or c==90:
    print("this is a right triangle")
elif a>90 or b>90 or c>90:
    print("this is obtuse triangle")
elif a<90 or b<90 or c<90:
    print("this is acute triangle")
