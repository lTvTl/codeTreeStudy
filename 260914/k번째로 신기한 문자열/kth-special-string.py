n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
#list형태로 단어 들어옴
#비교하려는 문자(T)와 list값 비교 후, 동일한 문자들만 list에 추가
#K번째 문자 출력(list k번째 출력)

#1단계 기존 list와 T값 비교, ture -> 유지, false -> 제거
newList = []
for i in range(n):
    word = "".join(str[i])
    if word.startswith(t):
        newList.append(word)
#2단계 정렬
newList.sort()

#3단계 원하는 단어 출력
print(newList[k-1])