def prime(n):
    for n in range(2,n+1):
        if all(n%i!=0 for i in range(2,int(n**0.5)+1)):
            print(n,end=" ")
n=int(input("enter n value:"))
print("prime numbers are:",end=" ")
prime(n)