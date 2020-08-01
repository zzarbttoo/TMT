# 5주차 4번 단어변환

def diff(str1, str2):
    cnt = 0
    for i in range (len(str1)):
        if str1[i] != str2[i]:
            cnt += 1
    if cnt == 1:
        return True # 단어가 하나만 다를 경우
    return False # 그렇지 않을 경우

def solution(begin, target, words):
    visit = [0 for _ in range(len(words))]
    ans = []
    def dfs(temp, depth):
        if temp == target: # target에 도달하면
            ans.append(depth) # 단계 저장
        else:
            for i in range(len(words)):
                if visit[i] == 0: # 아직 방문하지 않았다면
                    if diff(temp, words[i]):
                        visit[i] = 1
                        dfs(words[i], depth + 1) # 깊이 탐색
                        visit[i] = 0
    dfs(begin, 0)
    if len(ans) != 0:
        return min(ans)
    return 0
            
    

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))