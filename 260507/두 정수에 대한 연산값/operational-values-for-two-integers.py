a, b = map(int, input().split())

# Pleas write your code here.
def start(x, y):
    if x > y:
        x += 25
        y *= 2
    else:
        x *= 2
        y += 25
    print('{0} {1}'.format(x, y))

start(a,b)