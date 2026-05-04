M, D = map(int, input().split())

# Please write your code here.
date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if M > 0 and M < 13:
    if D <= date[M-1] and D > 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")