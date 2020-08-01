#3번 체육복
def solution(n, lost, reserve):
    answer = n-len(lost)
    lost=sorted(lost)
    reserve=sorted(reserve)
    for r in range(len(reserve) ):
        if reserve[r] in lost :
            answer+=1
            lost.remove(reserve[r])
            reserve[r]=31
    for i in lost :
        if not reserve :
            break
        if i-1 in reserve :
            reserve.remove(i-1)
            answer+=1
        elif i+1 in reserve :    
            reserve.remove(i+1)
            answer+=1
    return answer
