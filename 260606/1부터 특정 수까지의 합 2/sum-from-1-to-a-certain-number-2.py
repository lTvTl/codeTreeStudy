N = int(input())

# Please write your code here.
def gegui(x):
    if x == 1:
        return 1
    return gegui(x-1) + x

print(gegui(N))
