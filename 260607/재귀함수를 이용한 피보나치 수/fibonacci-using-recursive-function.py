N = int(input())

# Please write your code here.
def pi(N):
    if N == 1:
        return 1
    if N == 2:
        return 1
    return pi(N-2) + pi(N-1)

print(pi(N))