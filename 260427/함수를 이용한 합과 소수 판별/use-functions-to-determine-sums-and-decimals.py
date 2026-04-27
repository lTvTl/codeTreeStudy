a, b = map(int, input().split())

# n-1까지 자신을 나누었을때 나누어 떨어지지 않는 수
def decimal(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def zogun(x):
    xy = sum(map(int, str(x)))
    if xy % 2 == 0:
        return True

def panvul(a, b):
    count = 0
    for i in range(a, b+1):
        if decimal(i) == True:
            if zogun(i) == True:
                count += 1
    print(count)

panvul(a,b)