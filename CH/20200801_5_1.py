#1번 여행경로
from collections import deque as dq
import copy
def dfs(start,idx,tickets):        #깊이우선탐색(루트노드,인덱스넘버,티켓리스트)
    st,end = start                 #출발지와 도착지 추출
    lst.append(end)                #리스트에 도착지 추가
    visited.append(idx)            #방문지에 (티켓)인덱스 넘버 추가
    if len(lst)==len(tickets)+1 :  #모든 티켓 소진 시
        answer.append(copy.deepcopy(lst))  # 리스트를 카피해서 정답에 추가
        return
    for t in range(len(tickets)):          #티켓 길이 만큼  
            if end==tickets[t][0] and t not in visited :    #도착지가 티켓에서 출발지랑 같은경우
                dfs(tickets[t],t,tickets)                   #깊이우선탐색 재귀
                lst.pop()                                   #백트래킹
                visited.remove(t)                           #방문지에 인덱스 넘버 제거
                
    
def solution(tickets):
    global answer, visited,lst
    answer = []
    start=dq([])
    for idx in range(len(tickets)):
        visited=[]
        if "ICN"==tickets[idx][0]:
            start=(tickets[idx])
            lst=["ICN"]
            dfs(start,idx,tickets)
    answer=min(answer)
    return answer
