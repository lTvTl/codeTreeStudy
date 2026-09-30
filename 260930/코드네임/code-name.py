MAX_N = 5

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append((codename, int(score)))

# Please write your code here.
#2차원 배열 출력하는 것처럼 하면 될듯
#인원수 만큼 반복, 점수 저장, if 더 낮은 점수 나오면 비교후 해당 name으로 저장
i = 1
min = users[0]
for i in range(MAX_N):
    num = users[i]
    if num[1] < min[1]:
        min = users[i]
codename, score = min   #튜플 min값으로 입력
print(codename, score)  #튜플 출력