n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

#과정
#최대공약수 이용 -> 최소공배수 구하기
#유클리드 호제법(GCD) : if A%B == 0, GCD(b, r)
#최소공배수(LCM) : (a*b)//GCD(a,b)
#3개 이상일때? => LCM(a,LCM(b,c))

#즉, n개 만큼 lcm반복

def GCD(a,b):
    if a%b == 0:
        return b
    else:
        return GCD(b, a%b)
# print(GCD(3,4))

def LCM(a,b):
    return (a*b)//GCD(a,b)

#list에서 하나씩 빼서 lcm의 매개변수로 삽입
def multiful_LCM(n, arr):
    current = arr[0]  #시작점
    for i in range(1, n):   #갯수만큼 반복
        current = LCM(current, arr[i])  #chain방식으로 연결해서 리스트 다음 위치값 뽑아오기
    return current

print(multiful_LCM(n,arr))
