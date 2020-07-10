# 3주차 4번 더 맵게

import heapq as hq # 힙 모듈

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville) # 기존 리스트를 힙 형태로 변경
    
    while scoville[0] < K: 
        if len(scoville) == 1: # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
            return -1
        hq.heappush(scoville, hq.heappop(scoville) + (hq.heappop(scoville)*2)) # 새로운 음식
        answer += 1
        
    return answer
