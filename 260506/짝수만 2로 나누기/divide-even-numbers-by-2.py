n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def thisZeak(a):
    if a % 2 == 0:
        return True

for n in arr:
    if thisZeak(n) == True:
        print(n // 2, end = " ")
    else:
        print(n, end = " ")