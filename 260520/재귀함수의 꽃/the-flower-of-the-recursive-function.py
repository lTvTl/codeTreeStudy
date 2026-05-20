N = int(input())

# Please write your code here.

def chu(N):
    if N == 0:
        return 
    print(N, end=" ")
    chu(N-1)
    print(N, end=" ")

chu(N)