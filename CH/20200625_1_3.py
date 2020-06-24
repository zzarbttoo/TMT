def solution(bridge_length, weight, truck_weights):
    t=0
    truck=[0]
    time=[0]
    while time:
        t+=1
        while(t-time[0])>=bridge_length:
            truck.pop(0)
            time.pop(0)
            if not time:
                break
        if not truck_weights:
            continue
        if sum(truck, truck_weights[0]) <= weight:
            truck.append(truck_weights.pop(0))
            time.append(t)
    return t
