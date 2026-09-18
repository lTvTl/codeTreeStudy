n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# 홀수번째마다 계산 시작, 계산 후 해당하는 리스트의 중앙값을 출력
# list의 홀수 번째인지 확인하는 코드
# list의 중앙값을 출력하는 코드
# list구분(기본 list, 중간 list, 최종 list)
# 주어진 list를 순서대로 하나씩 확인하고 해당하는 값을 다른 list에 출력
# if 홀수칸이면 list정렬 후, 중앙값 확인 후, 최종 list에 삽입

B_list = [] #중간 list
C_list = [] #최종 list
a_len = len(arr)

for i in range(a_len):
    # arr 홀수값 확인
    if i % 2 == 0: #홀수값이면
        B_list.append(arr[i]) #중간 list에 값 추가
        B_list.sort() #정렬
        
        # 중간 list의 중앙값 위치 찾기
        b_len = len(B_list)
        b = b_len // 2
        if b_len % 2 == 1: #중앙값이 홀수라면
            C_list.append(B_list[b])
        else:   #짝수면 둘 더해서 나누기 2
            C_list.append((B_list[b-1] + B_list[b]) // 2)
    else:
        B_list.append(arr[i])


print(*C_list)
