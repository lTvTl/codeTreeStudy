N = int(input())

# Please write your code here.
def gegui(N):
    if N < 10:
        return N**2
    return gegui(N // 10) + ((N % 10)**2)

print(gegui(N))