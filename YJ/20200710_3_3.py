import collections
import heapq

def solution(stock, dates, supplies, k):

    answer = 0
    heap_plus= []

    dates = collections.deque(dates)
    supplies = collections.deque(supplies)

   
    while(stock < k):

        while(True):
 
            if(len(dates) >0):
                if(dates[0] <= stock):
                    heapq.heappush(heap_plus, -supplies.popleft())
                    dates.popleft()
                else:
                    break
            else:
                break

                
                
        stock -= heapq.heappop(heap_plus)
        answer += 1

    return answer
        
# print(solution(4, [4,10,15] , [20, 5, 1] , 30))
# print(solution(4, [4, 10, 15, 30], [26, 5, 10, 10], 30)) # 답은 1
print(solution(4, [4, 10, 15], [20, 5, 10], 30)) #2


# import heapq

# def solution(stock, dates, supplies, k):
#     answer = 0
#     idx = 0
#     candidates = []
#     supplies = [-x for x in supplies]
#     while stock < k:
#         # 현재 stock으로 버틸 수 있는 날 중에 추가로 밀가루 수령이 가능한 날과 그 날의 수량 저장
#         for i in range(idx, len(dates)):
#             if stock >= dates[i]:
#                 idx = i + 1
#                 heapq.heappush(candidates, supplies[i])  # 해당일의 공급 가능 물량을 candidates heap에 추가
#             else:
#                 break

#         # stock = stock + heapq._heappop_max(candidates)
#         stock = stock + heapq.heappop(candidates) * -1
#         answer = answer + 1

#     return answer