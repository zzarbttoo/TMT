import heapq as hq
from collections import deque as dq
def solution(stock, dates, supplies, k):
    answer = 0
    queue=[]
    dates=dq(dates)
    supplies=dq(supplies)
    while stock < k :                             #stock이 k보다 클때까지
        while dates and stock >= dates[0] :       #수입일자가 존재하고 stock이 수입일자[0]보다 크면 돌아감
            dates.popleft()
            val=supplies.popleft()
            hq.heappush(queue,(-val,val))         # -val을 이용해서 최대heap 생성
        stock+=hq.heappop(queue)[1]               # val을 꺼내서 stock에 더해줌
        answer+=1
    return answer
