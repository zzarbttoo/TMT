# 4주차 2번 타겟 넘버

answer = 0

def DFS(idx, numbers, target, value):
        global answer
        N = len(numbers)
        if idx == N:
            if target == value:
                answer += 1
            return
        DFS(idx+1,numbers,target,value+numbers[idx])
        DFS(idx+1,numbers,target,value-numbers[idx])


def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))
