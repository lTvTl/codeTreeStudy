n = int(input())

# Please write your code here.
def start(n):
    if n == 0:
        return 
    start(n-1)
    print("HelloWorld")

start(n)