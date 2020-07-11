import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while(True):

        if(scoville[0] > K):
            break

        if len(scoville) ==1:
            if scoville[0] < K:
                return

        heapq.heappush(scoville, heapq.heappop(scoville) + 2* heapq.heappop(scoville))
        answer += 1

    return answer

print(solution([1,2,3,9,10,12], 7)) #2