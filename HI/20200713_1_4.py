# 4주차 1번 쇠막대기

from collections import deque

def solution(arrangement):
    answer = 0
    arr = deque(arrangement)
    nslice = []
    i = 0
    while i < len(arrangement):
        if arr[i] == '(':
            if arr[i+1] == ')': # 레이저면 막대 조각 만큼 개수 증가
                answer += len(nslice)
                i += 2
            else: # 아니라면 막대 조각 추가
                nslice.append('(')
                i += 1
        else: # 막대가 끝나면 조각 제거 및 1개 추가
            nslice.pop()
            answer += 1
            i += 1

    return answer

'''
replace를 사용해 ()를 다른 문자로 바꾸면 중첩 if문이 아니기 때문에 
시간이 더 짧게 걸리고 for문을 사용해 간결하게 코드를 짤 수 있다.

def solution(arrangement):
    answer = 0
    arr = arrangement.replace('()','L')
    nslice = []
    for i in arr:
        if i == '(': nslice.append(i)
        elif i == 'L': answer += len(nslice)
        else:
            nslice.pop()
            answer += 1
            
    return answer
'''