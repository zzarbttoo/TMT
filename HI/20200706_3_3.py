# 3주차 3번 라면공장

import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    j = 0

    while stock < k: # k일까지 공장 운영
        for i in range(j, len(dates)):
            if dates[i] <= stock: # 재고가 0이 될 시점 이전에 공급
                heapq.heappush(heap, -supplies[i]) # 부호를 변경해 최소 힙으로 사용
                j = i + 1
            else:
                break
        stock -= heapq.heappop(heap) # 공급량 만큼 stock 증가
        answer += 1

    return answer
