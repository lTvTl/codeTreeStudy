n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

#1단계 정렬
nums.sort()
#2단계 양 끝 끼리 조합, 합 계산 => 더 큰 값 나오면 최신화
big = 0
for i in range(n):
    r = nums.pop(0)
    s = nums.pop(-1)
    if big < s + r:
        big = s+r
#결과값 출력
print(big)