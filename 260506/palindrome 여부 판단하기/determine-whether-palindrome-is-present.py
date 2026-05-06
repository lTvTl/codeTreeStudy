A = input()

# Please write your code here.
def start(A):
    setlist = []
    setlist = list(A)
    setlistt = list(A)
    n = len(A)
    for i in range(0, n):
        if setlist.pop() == setlistt.pop(0):
            continue
        else:
            return print("No")
    return print("Yes")

start(A)