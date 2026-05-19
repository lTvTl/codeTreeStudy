n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

#해당하는 값 출력
def biguo(x, y):
    global arr
    hap = 0
    for i in arr[x-1 : y]:
        hap += i
    return print(hap)

#해당하는 값 파악
def cucull(a,b):
    global queries
    return queries[a][b]

#반복문 실행
def start(m):
    for i in range(m):
        x = cucull(i, 0)
        y = cucull(i, 1)
        biguo(x,y)

start(m)