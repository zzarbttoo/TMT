# 3주차 5번 디스크 컨트롤러

import heapq as hq

def solution(jobs):
    answer = 0
    h = [] # 힙
    time = 0
    count = len(jobs)
    
    jobs.sort() # 요청 시간 순으로 정렬

    while jobs: 
        for j in jobs:
            if j[0] <= time: # 현재 시간 전에 요청된 목록들 중
                if j[-1::-1] not in h: # heap에 추가되지 않은 목록 추가
                    hq.heappush(h, [j[1], j[0]]) # 소요시간이 적은 것 부터 힙 정렬
                else:
                    continue
            else: break
        if h:
            curr = hq.heappop(h)
            jobs.remove(curr[-1::-1]) # 수행 한 것 삭제
            time += curr[0] # 수행 후 시간
            answer += time - curr[1] # 수행 후 시간 - 요청 시간 = 총 소요 시간
        else:
            time += 1 # 요청 된 것이 없으면 시간 1 증가
            
    answer /= count # 평균
    return int(answer)

