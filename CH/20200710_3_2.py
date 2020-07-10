def solution(priorities, location):
    from collections import deque
    pos=[]
    t=0                                                    #t값 초기화
    for k in range(len(priorities)) :                      #현재 위치 기록
        pos.append(k)
    while 1 :
        for j in range(t+1,len(priorities)) :
            if priorities[t] <priorities[j] :              #현재 값보다 우선 순위가 높으면 기준값을 재설정
                val=priorities[j]
                priorities.append(priorities.pop(t))       #뽑아서 뒤쪽으로 이동
                pos.append(pos.pop(t))                     #위치기록도 이동
                break
            elif j==len(priorities)-1 :                    #우선순위가 높은게 없으면 맨앞에 두고 t+1해줌
                t+=1
                val=priorities[t]                          #기준값을 t위치로 바꿔줌
        if priorities==sorted(priorities,reverse=True):    #우선순위값이 정렬되어 있으면 break
            break
    for p in range(len(pos)) :                             #위치 정보 검색하는 기능
        if pos[p]==location:
            answer=p+1
            break
    return answer
