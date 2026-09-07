n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.

#1. nums list를 정렬
nums.sort()
#2. list의 k번째 수 출력
print(nums[k-1])