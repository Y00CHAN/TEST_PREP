'''
문제 15: 숫자 정렬 후 이어붙이기 (가장 큰 수 만들기)

양의 정수 리스트를 받아, 숫자를 이어 붙여 가장 큰 수를 만드는 함수를 작성하시오.
'''

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def largest_concatenated_number(numbers):
    # 비교 함수 없이 커스텀 정렬을 람다로 처리
    numbers = list(map(str, numbers))

    # 정렬: 두 문자열을 이어붙였을 때 큰 수가 앞으로 오도록 정렬
    numbers.sort(key=lambda x: x*10, reverse=True)  # 문자열을 10배 반복하여 비교

    # 모두 0으로만 이루어진 경우 "0" 반환
    if numbers[0] == '0':
        return '0'

    # 리스트를 이어붙여 최종 결과 반환
    return ''.join(numbers)

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(largest_concatenated_number([3, 30, 34, 5, 9]))  # "9534330"
print(largest_concatenated_number([10, 2]))            # "210"
print(largest_concatenated_number([1, 1, 1]))          # "111"
#####################################################