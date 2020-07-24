# 4주차 5번 이중우선순위 큐

import heapq as hq

def solution(operations):
    h = []
    for o in operations:
        if o[:1] == 'I': # 숫자면 힙에 추가
            hq.heappush(h,int(o[2:]))
        elif h and o == 'D -1': # 최소힙의 루트노드(최솟값) 제거
            hq.heappop(h)
        elif h and o == 'D 1': # 최댓값 제거
            h.remove(max(h))
    if h:
        return[max(h),h[0]]
    else:
        return [0,0]