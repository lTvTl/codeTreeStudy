n = int(input())

# Please write your code here.

count = 0

def result(n):
    global count
    # 종료조건
    if n == 1:
        return print(count)
    #계산식
    if n % 2 == 0:
        n = n / 2
        count += 1
        result(n)
    else:
        n = n * 3 + 1
        count += 1
        result(n)

result(n)