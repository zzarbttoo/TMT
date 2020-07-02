# 2주차 4번 기능개발

import math

def solution(progresses, speeds):
    answer = []
    day = [] 
    count = 1
    released = [0]*len(speeds)
    
    for k in range(len(speeds)): # 각 기능별 개발 작업일 수 
        day.append(math.ceil((100 - progresses[k]) / speeds[k]))
    
    for i in range(len(day)):
        if released[i] == 1:
            continue
        released[i] = 1
        for j in range(i+1, len(day)):
            if day[i] >= day[j]: 
                released[j] = 1 # 배포 시 1로 변경
                count += 1
            else:
                answer.append(count) # 배포 기능 수
                count = 1
                break
    answer.append(count)

    return answer