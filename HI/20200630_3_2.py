# 2주차 3번 탑

def solution(heights):
    answer = []
    stack = []
    i = 1
    for tower in heights: # 스택에 넣음
        stack.append(tower)
    while stack:
        k = 1
        curr = stack.pop() # 위부터 꺼냄
        while k <= len(stack): 
            if stack[-k] > curr: # 현재보다 높은 탑 찾기
                answer.insert(0, len(heights)-i-(k-1)) # 탑의 인덱스 추가
                break
            k += 1
        if k > len(stack): # 신호 수신 탑이 없는 경우
            answer.insert(0,0)
        i += 1
    return answer