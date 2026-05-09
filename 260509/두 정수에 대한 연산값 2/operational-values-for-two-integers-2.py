a, b = map(int, input().split())

# Please write your code here.

def pandan(a, b):
    if a > b:
        b += 10
        a *= 2
    else:
        b *= 2
        a += 10
    return print(a, b)

pandan(a, b)
