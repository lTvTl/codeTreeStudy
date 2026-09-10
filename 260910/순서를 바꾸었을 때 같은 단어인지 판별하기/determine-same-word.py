word1 = input()
word2 = input()

# Please write your code here.
#정렬해서 동일한 list이면 참, 아니면 거짓
#1단계 Str을 list화
li1 = list(word1)
li2 = list(word2)
#2단계 list 정렬
li1.sort()
li2.sort()

#3단계 비교
if len(li1) != len(li2):
    print("No")
    exit()

while len(li1) > 0:
    w1 = li1.pop()
    w2 = li2.pop()
    if w1 != w2:
        print("No")
        exit()
print("Yes")