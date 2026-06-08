N = int(input())

# Please write your code here.
def gegui(N):
    if N % 2 == 0:
        if N <= 2:
            return 2
        return gegui(N-2) + N
    else:
        if N <= 1:
            return 1
        return gegui(N-2) + N

print(gegui(N))