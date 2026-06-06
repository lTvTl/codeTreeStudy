N = int(input())
count = 0
# Please write your code here.
def gegui(N):
    global count
    if N <= 1:
        return print(count)

    x = N % 2
    count += 1

    if x % 2 == 0:
        return gegui(N//2)
    else :
        return gegui(N//3)
        

gegui(N)