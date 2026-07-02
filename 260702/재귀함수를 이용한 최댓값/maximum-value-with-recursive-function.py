n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
#n개 들어옴 -> n-1번 반복해서 리스트값 비교, 그 중 최대값만 기억, 근데 재귀함수
str = 1
hi = arr[0]
def zegui(n):
    #전역변수 불러오기
    global hi
    global str

    #종료시점
    if str >= n:
        return print(hi)

    #최대값 비교
    if arr[str] > hi:
        hi = arr[str]
        str += 1
        zegui(n)
    else:
        str += 1
        zegui(n)

zegui(n)