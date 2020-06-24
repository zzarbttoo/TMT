# 1주차 3번_다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 0  #경과 시간
    tot_weight = 0  #다리를 건너는 트럭 무게
    bridge_queue = [0 for i in range(bridge_length)] #다리 길이만큼의 큐
    while truck_weights: #대기 트럭이 없어질 때 까지
        answer += 1
        tot_weight -= bridge_queue[0]
        bridge_queue.pop(0)

        if tot_weight+truck_weights[0] <= weight:
            tot_weight += truck_weights[0]
            bridge_queue.append(truck_weights.pop(0))
        else:
            bridge_queue.append(0)
            
    while tot_weight != 0: #다리 위의 트럭이 없어질 때 까지
        answer += 1
        tot_weight -= bridge_queue[0]
        bridge_queue.pop(0)        
    return answer

print(solution(2, 10, [7,4,5,6]))