def solution(bridge_length, weight, truck_weights):
    t=0
    truck=[0]                                        #다리에 올라온 트럭
    time=[0]                                         #각 트럭이 다리에 올라온 시간
    while time:                                      #시간은 계속 지나감
        t+=1
        while(t-time[0])>=bridge_length:             #다리에 올라온 시간과 현재시간의 차이가 다리 길이보다 크면 탈출
            truck.pop(0)
            time.pop(0)
            if not time:                             #시간 기록이 없으면 탈출
                break
        if not truck_weights:                        #들어올 트럭이 없으면 탈출
            continue
        if sum(truck, truck_weights[0]) <= weight:   #다리지탱 무게보다 높으면 못들어옴
            truck.append(truck_weights.pop(0))       #다리위로 올라오게하고 기록
            time.append(t)                           #올라온 시간도 기록
    return t
