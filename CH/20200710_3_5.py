import heapq as hq
from collections import deque as dq
def solution(jobs):
    answer=0
    t=0
    work=[]
    wait=[]
    hq.heapify(jobs)
    n=len(jobs)
    while True :
        if not work and jobs[0][0] >=t :                 # 대기열도 없고 작업도 안하고있으면 작동 ,t는 누적시간
            work.append(hq.heappop(jobs))                # 최소heap jobs에서 하나 뽑음
            answer+=work[0][1]
            if t<work[0][0]:                             # 누적시간 재설정,누적시간보다 요청시간이 크면 계산하는 법
                t+=work[0][1]+work[0][0]-t
            else :                                       # 누적시간이 더 크면 계산하는법
                t+=work[0][1]+work[0][0]
        while jobs and jobs[0][0] <= t :                 # 대기열 만들기, 누적시간보다 요청시간이 작을경우 대기열로 들어감
            wait.append(hq.heappop(jobs))
        work.pop()                                       #작업끝!
        if wait :                                        #대기열이 존재하면
            wait=sorted(wait, key=lambda x:x[1])         #요청시간을 기준으로 오름차순 정렬
            work.append(hq.heappop(wait))
            answer+=work[0][1]+t-work[0][0]
            t+=work[0][1]
        if not jobs and not wait :                       #대기열도 없고 작업요청도 없으면 끝!
            break
    return answer//n
