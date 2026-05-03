n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
#a를 반복하면서 b의 첫번째 원소가 나올때까지 반복,
#나왔을때 if문 실행 -> b의 두번재 원소랑 a의 첫번재 원소 쭉 비교

#전체 통으로 비교
def aListNew(a,b):
    for i in range(0, n1 - n2 +1):
        if a[i] == b[0]:
            if a[i:i+n2]==b:
                return True
    return False

  
if aListNew(a, b):
    print("Yes")
else:
    print("No")
    