n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

nums.sort()
#list 앞 부터 하나씩 출력
print(*nums)
nums.sort(reverse=True)
print(*nums)