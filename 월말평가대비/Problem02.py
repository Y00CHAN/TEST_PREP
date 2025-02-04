'''
문제 2: 비밀번호 길이 검증

딕셔너리의 password 값이 8자 이상인지 확인하는 함수를 작성하시오.
'''

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def is_password_strong(dic):
    # 여기에 코드를 작성하세요.
    for item in dic:
        password = dic['password']
        if len(password) >= 8:
            return True
        else:
            return False


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_password_strong({'password': '12345678'}))  # True
print(is_password_strong({'password': 'abc'}))       # False
#####################################################