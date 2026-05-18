n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

sum = 0

def hollAndZak(m):
    if m % 2 == 0:
        return True
    else:
        return False

def hap(m):
    global sum
    sum += A[m-1]
    
def start(n, m):
    global sum
    hap(m)
    while True:
        if m <= 1:
            return print(sum)
        if hollAndZak(m):
            m //= 2
            hap(m)
        else:
            m -= 1
            hap(m)

start(n, m)


    
