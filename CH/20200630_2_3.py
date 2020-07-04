def solution(heights):
    answer=[]
    queue=[]
    while heights:
        queue.append(heights.pop())                                   #일단 맨뒤에 하나를 큐에 집어 넣음
        b=[x+1 for x in range(len(heights)) if heights[x]>queue[-1]]  #방금 넣은 거랑 heights에 있는 애들이랑 비교 후 위치 기록
        if not b:
            answer.append(0)                                          #만약 큐에 있는 것보다 높은 애가 없으면 0을 넣음
        else:
            answer.append(max(b))                                     #b에 있는 애들중에 가장 오른쪽에 위치한 탑을 넣음
    answer.reverse()                                                  #좌우반전
    return answer
