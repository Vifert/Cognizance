#Question-4
n=int(input("Number: "))
t=n
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(t==r):
    print("True")
else:
    print("False")
    