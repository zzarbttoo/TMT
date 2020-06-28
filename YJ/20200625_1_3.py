# 풀이 1 : 오르 내리는 것을 못함 다시 풀자
# def solution(bridge_length, weight, truck_weights):

#     truck_hash = {}
#     wholeSum = 0
#     weightOfQueue = 0 
#     truckNum = 0

#     data_queue = []

#     #truck_hash에 온 순서를 키값으로 truck의 무게와 건너야 할 다리 길이를 넣어놓음
#     for i in truck_weights:
#         truck_hash[truckNum] = truck_hash.get(truckNum, [i, bridge_length]) 
#         truckNum += 1

#     #truck_array 에 hash 의 key값을 넣음
#     truck_array = list(range(len(truck_weights)))

#     while(True):

#         #종료조건
#         if(len(truck_array) == 0 and len(data_queue) == 0):
#             break

#         #pop 조건
#         for i in data_queue:
#             if(truck_hash[i][1] != 0):
#                 truck_hash[i][1] -= 1
#             else:
#                 weightOfQueue -= truck_hash[data_queue.pop(0)][0]



#         #put 조건
#         if len(truck_array) != 0 and weightOfQueue + truck_hash[truck_array[0]][0] <= weight:
#             weightOfQueue += truck_hash[truck_array[0]][0]
#             #바로 줄어들어야 한다는 것이다~
#             truck_hash[truck_array[0]][1]-= 1
#             data_queue.append(truck_array.pop(0))

#         wholeSum +=1

        

    
#     return wholeSum



#list를 Queue로 사용하기
# https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
#list 를 stack으로 사용하기
# https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks


#다시 풀어.2
#리스트로 구현하면 느리다고 하므로 큐로 다시 함 굉굉
from collections import deque
import queue


def solution (bridge_length,  weight, truck_weights):

    truck_wait = []
    time_sum = 0 
    weight_sum = 0
    bridge_queue= deque([])
    truck_hash = {}

    #hash 값 생성
    for i, truckWeight in enumerate(truck_weights):
        truck_hash[i] = truck_hash.get(i, [truck_weights[i], bridge_length])
        truck_wait.append(i)
    
    truck_wait = deque(truck_wait)


    while(True):
 
        #pop 조건
        #파이썬에서는 권장되지 않는 방식이나, 병행 오류가 나서 바꿈
        if(len(bridge_queue) != 0 ):
            if(truck_hash[bridge_queue[0]][1] == 0):
                    weight_sum -= truck_hash[bridge_queue.popleft()][0]
            for i in range(0, len(bridge_queue)):
                    truck_hash[bridge_queue[i]][1] -=1

        #push 조건
        if(len(truck_wait)!= 0 and weight_sum + truck_hash[truck_wait[0]][0] <= weight ):
            weight_sum += truck_hash[truck_wait[0]][0] 
            bridge_queue.append(truck_wait.popleft())

        #종료 조건
        if(len(truck_wait) == 0 and len(bridge_queue) == 0):
            break
    
        time_sum += 1
    return time_sum

    

print(solution(1, 2 ,[1,1,1])) #4
print(solution(1, 1, [1,1,1])) #4
print(solution(4,2, [1,1,1,1])) #10
print(solution(3, 3, [1,1,1])) #6
print(solution( 3, 1, [1,1,1])) #10
print(solution(5,5, [1,1,1,1,1,2,2])) #14



print(solution(7, 7, [1,1,1,1,1,3,3])) #18
print(solution(5, 5, [1,1,1,1,1,2,2,2,2])) #19
print(solution( 5, 5, [2,2,2,2,1,1,1,1,1])) #19
print(solution(2, 10, [7,4,5,6])) #8
print(solution(100, 100, [10])) #101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) #110








