'''
문제 8: 사용자 데이터 검증 (복합 조건)

딕셔너리에서 id와 password가 모두 비어있지 않고, password의 길이가 8자 이상이면 True를 반환하는 함수를 작성하시오.
'''

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def is_user_data_valid(data):
    # 여기에 코드를 작성하세요.
    if data['id'] == '' or data['password'] == '' or len(data['password']) < 8:
        return False
    else:
        return True

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_user_data_valid({'id': 'user1', 'password': '12345678'}))  # True
print(is_user_data_valid({'id': '', 'password': '12345678'}))       # False
print(is_user_data_valid({'id': 'user2', 'password': '1234'}))      # False
#####################################################