# 6주차 4번 구명보트

from collections import deque as dq

def solution(people, limit):
    answer = 0
    people.sort() # 오름차순 정리
    queue = dq(people)
    
    while len(queue) > 1:
        if queue.pop() + queue[0] <= limit: # 제일 큰 것, 작은 것 합이 limit을 넘지 않으면
                queue.popleft() # 작은 것도 함께 구출
        answer += 1
    
    if len(queue) == 1: return answer + 1 # 하나가 남아있다면 한 번 더 사용
   
    return answer # 없다면 그대로 answer return
