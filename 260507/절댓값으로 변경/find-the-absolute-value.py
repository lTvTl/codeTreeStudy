n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# 리스트 0번째 값 받아서 절대값 만들고 출력
for i in range(n):
    a = arr.pop(0)
    a = int((a**2)**0.5)
    print(a, end =" ")