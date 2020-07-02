# 2주차 K사 괄호 변환

def balanced(string): # 균형잡힌 괄호 문자열 확인 함수
    count = 0
    for u in string:
        if u == '(':
            count -= 1
        else:
            count += 1
    if count == 0:
        return True
    else:
        return False

def correct(string): #올바른 괄호 문자열 확인 함수
    stack = []
    for u in string:
        if u == '(':
            stack.append(u)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

def solution(p):
    answer = ''

    if p == '': # 입력이 빈 문자열인 경우
        return answer
    
    for i in range(2,len(p)+1,2): 
        if balanced(p[:i]):
            u = p[:i] # 분리할 수 없는 균형잡힌 문자열
            v = p[i:]
            break
    
    if correct(u): # u가 올바른 괄호 문자열인 경우
        answer = u + solution(v)
        return answer
    else: # u가 올바른 괄호 문자열이 아닌 경우
        u = u[1:-1]
        reversed_u = ""
        for k in range(len(u)):
            if u[k] == '(':
                reversed_u += ')'
            else:
                reversed_u += '('
        answer = '(' + solution(v) + ')' + reversed_u
        return answer
