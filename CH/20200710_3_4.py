def solution(scoville, K):
    answer = 0
    import heapq as hq
    scoville=sorted(scoville)
    while len(scoville) > 2 :                  #스코빌 지수가 2가 될때까지
        if scoville[0]>=K:                     #모든 스코빌이 k이상이면 끝
            return answer
        hq.heappush(scoville, hq.heappop(scoville)+hq.heappop(scoville)*2)    #스코빌지수 높이기!
        answer+=1
    if scoville[0] >= K:
        return answer
    if scoville[0]+scoville[1]*2 <K :          #두개 남은 상황에서 둘이 섞어도 k보다 낮을때 실패
        return -1
    else :                                     # 높으면 결과 출력
        answer+=1
        return answer
