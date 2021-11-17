# Fast Exponentian
# Time Complexity - O(logn)

def myPow(x, n):
    mod=1000000009
    if n==0:
        return 1
    if (n%2)==0:
        half=myPow(x,n//2)
        return (half*half)%mod
    else:
        half=myPow(x,n//2)
        # in case of odd we take the floor value
        return (half*half*x)%mod

print(myPow(2,4))
