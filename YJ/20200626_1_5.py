# def dfs(n, computers):
#     #computers은 2차원 배열

#     sum = 0
#     visited = []
#     stack = []

#     stack.append(computers[0])

#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.append(node)
#             stack.extend([node])
#     return visited

#풀이 1
def dfs(root, visited, computers):

    stack = []
    stack.append(root) 
    visited[root] = True

    for i,j in enumerate (computers[stack.pop()]):
        if visited[i] == False and j == 1:
            visited[i] = True
            stack.append(i)

    while stack:
        visited=dfs(stack.pop(), visited, computers)
    
    return visited

        
def solution(n, computers):

    visited = [False] * n
    answer = 0

    for i in range (0,n) : 
        if(visited[i] == False):
            visited = dfs(i,visited, computers)
            answer += 1

    return answer 




print(solution(3 ,[[1,1,0], [1,1,0], [0,0,1]])) #2
print(solution(3 ,[[1,1,0], [1,1,1], [0,1,1]]))#1


#DFS/BFS: https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html

#다른사람의 풀이(ㄷㄷ)
def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))