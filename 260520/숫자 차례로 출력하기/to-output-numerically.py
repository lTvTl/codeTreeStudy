n = int(input())

# Please write your code here.
#내려가는
def mi(n):
    if n == 0:
        return
    print(n, end=" ")
    mi(n-1)

#올라가는
def hi(n):
    if n == 0:
        return
    hi(n-1)
    print(n, end=" ")

hi(n)
print("")
mi(n)