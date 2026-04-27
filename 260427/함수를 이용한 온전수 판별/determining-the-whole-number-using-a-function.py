a, b = map(int, input().split())

# Please write your code here.
def panvel(x):
    if x % 2 == 0:
        return False
    elif x % 10 == 5:
        return False
    elif x % 3 == 0 and x % 9 != 0:
        return False
    else:
        return True

def sai(a, b):
    count = 0
    for i in range(a+1, b):
        if panvel(i) == True:
            count += 1
    print(count)

sai(a, b)

