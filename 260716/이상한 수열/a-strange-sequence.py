N = int(input())

# Please write your code here.

def gegui(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    return gegui(int(N/3)) + gegui(N - 1)

print(gegui(N))