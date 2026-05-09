A = input()

# Please write your code here.
arr = list(A)

def pandan(arr):
    l = len(arr)
    list = []
    for i in range(1, l):
        if arr[i-1] != arr[i]:
            return print("Yes")
        else:
            continue
    return print("No")
pandan(arr)