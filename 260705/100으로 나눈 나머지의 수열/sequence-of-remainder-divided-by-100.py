N = int(input())

# Please write your code here.

def su(N):
    if N == 1 :
        return 2
    elif N == 2:
        return 4
    else:
        return (su(N-2) * su(N-1)) % 100

print(su(N))