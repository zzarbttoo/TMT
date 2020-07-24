# 4주차 4번 숫자 야구

import itertools

def solution(baseball):
    answer = 0
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    case = list(map(''.join, itertools.permutations(num,3))) # 가능한 모든 세자리 수
    answer = case.copy()
    
    for b in baseball:
        b[0] = str(b[0]) # 질문한 세자리 수 문자열로 변환

    # 모든 세자리 수에 대해 질문의 답을 만족하는 것만 남기고 그렇지 않은 것 제거
    for c in case: 
        for b in baseball:
            S, B = 0, 0
            for i in range(3):
                if c[i] == b[0][i]:
                    S += 1
                elif c[i] in b[0]:
                    B += 1
            if b[1] != S or b[2] != B:
                answer.remove(c)
                break
    return len(answer) # 가능한 답의 개수
