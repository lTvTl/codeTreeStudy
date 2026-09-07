str = input()

# Please write your code here.
#1.리스트화
sort1_list = list(str)
#2.정렬
sort1_list.sort()
#3.다시 문자화
sort2_list = ''.join(sort1_list)
print(sort2_list)