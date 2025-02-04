'''
문제 11: 문자열 압축 (Run-Length Encoding)

주어진 문자열을 압축하는 함수를 작성하시오.
연속된 문자는 그 개수로 표시하며, 개수가 1인 경우 생략합니다.
'''

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def compress_string(stn):
    if not stn:
        return ""  # 빈 문자열 처리

    result = ""      # 결과를 저장할 문자열
    count = 1         # 연속된 문자 개수 초기화

    for i in range(1, len(stn)):
        if stn[i] == stn[i - 1]:  # 이전 문자와 같으면 개수 증가
            count += 1
        else:
            result += stn[i - 1]  # 이전 문자 추가
            if count > 1:
                result += str(count)  # 개수가 1보다 크면 숫자 추가
            count = 1  # 개수 초기화

    # 마지막 문자 처리
    result += stn[-1]
    if count > 1:
        result += str(count)

    return result


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(compress_string("aaabbc"))    # "a3b2c"
print(compress_string("abcd"))      # "abcd"
print(compress_string("aaaabbbbaa")) # "a4b4a2"
#####################################################
