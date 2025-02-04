'''
문제 10: 소수 판별 함수

주어진 숫자가 소수(prime number) 인지 확인하는 함수를 작성하시오.
'''

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def is_prime(num):
    # 여기에 코드를 작성하세요.
    if num < 2:
        return False
    if num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(2))   # True
#####################################################

