a, b, c = map(int, input().split())

# Please write your code here.
gup = a * b * c

def gegui(gup):
    #종료조건
    if gup < 10:
        return gup
    #각 자리수 합 구하기
    return gegui(gup // 10) + gup % 10

print(gegui(gup))
    