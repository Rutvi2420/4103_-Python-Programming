#write a program for to create fabonacci series upto entered term.

A =0
B =1
n = int(input("Enter No of terms :" ))
print(A,B,sep="\n")

for i in range(3,n+1):
    C = A+B
    A =B
    B =C
    print(C)
    
