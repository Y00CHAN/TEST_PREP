'''
문제 12: 괄호 유효성 검사 (Valid Parentheses)

'(', ')', '{', '}', '[', ']'로 이루어진 문자열이 올바른 괄호 구조인지 확인하는 함수를 작성하시오.
'''

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def is_valid_parentheses(col):
    stack = []  # 괄호를 저장할 스택
    mapping = {')': '(', '}': '{', ']': '['}  # 닫는 괄호에 대한 매칭 정보

    for char in col:
        if char in mapping.values():  # 여는 괄호일 경우 스택에 추가
            stack.append(char)
        elif char in mapping:  # 닫는 괄호일 경우
            if not stack or stack[-1] != mapping[char]:  # 매칭 안 되면 False
                return False
            stack.pop()  # 매칭되면 스택에서 제거
        else:
            return False  # 유효하지 않은 문자 처리

    return not stack  # 스택이 비어있으면 유효한 괄호 구조


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_valid_parentheses("()[]{}"))     # True
print(is_valid_parentheses("(]"))         # False
print(is_valid_parentheses("([{}])"))     # True
print(is_valid_parentheses("((()))["))    # False
#####################################################
