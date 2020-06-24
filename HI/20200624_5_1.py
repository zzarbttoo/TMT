#1주차 5번_네트워크

def solution(n, computers):
    answer = 0
    visit = [0]*n   #방문:1/ 방문하지 않음:0
    queue = []   #DFS 탐색 큐

    for i in range(n):   #모든 컴퓨터에 대해 탐색
    
        if visit[i] == 1:
            continue

        answer += 1   #DFS 탐색 횟수가 네트워크의 수가 됨
        queue.append(i)   #방문하지 않은 노드 추가

        while queue:   #DFS 탐색
            t_node = queue.pop(0)
            visit[t_node] = 1   #큐에서 뽑은 노드를 방문
            for j in range(n):
                if computers[t_node][j] == 1 and visit[j] == 0:   #방문하지 않은 자식 노드를 큐에 추가
                    queue.append(j)
    
    return answer

