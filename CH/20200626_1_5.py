def solution(n, computers):
    visited=[]
    node=[0]*n                             #방문노드 초기화
    stack=[]
    net=0
    for i in range(n):                     #모든 컴퓨터에 방문
        if node[i]==1:                     #자기자신일 경우 continue
            continue
        if i in visited:                   #방문한 노드일경우 continue
            continue
        net+=1
        stack.append(i)
        visited.append(i)                  #처음 방문시 방문기록
        while stack:                       #스택이 빌 때까지(네트워크 깊이 탐색)
            node=computers[stack.pop(0)]
            for j in range(n):             #방문한 노드의 연결 노드 확인
                if j not in visited:
                    if node[j]==1:         #연결 되어있으면 스택에 추가 & 방문기록
                        stack.append(j)
                        visited.append(j)
    return net
