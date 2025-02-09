'''
문제 7: 중복 제거 후 오름차순 정렬

정수 리스트에서 중복을 제거하고 오름차순으로 정렬하는 함수를 작성하시오.
'''

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def unique_sorted_list(lst):
    # 여기에 코드를 작성하세요.
    # new_list = []
    # for num in lst:
    #     if num not in new_list:
    #         new_list.append(num)
    # new_list.sort()
    # return new_list
 
    return list(set(lst))


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(unique_sorted_list([4, 2, 5, 2, 3, 4, 1]))  # [1, 2, 3, 4, 5]
#####################################################