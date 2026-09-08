n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

#각 list정렬
A.sort()
B.sort()
#리스트 비교(for문 n번 반복)-참,거짓으로 값 출력
a = 0
for i in range(n):
    if A[i] != B[i]:
        a += 1

if a == 0:
    print("Yes")
else:
    print("No")

