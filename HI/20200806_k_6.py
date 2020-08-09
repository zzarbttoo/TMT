# 6주차 K사 외벽점검

from bisect import bisect_left, bisect_right

def solution(n, weak, dist):
    answer = []
    dist.sort()
    for i in range(len(weak)): # 취약 지점 거리 계산 시 시작 기준
        weak[0] += n
        weak.sort()
        weak2 = weak.copy()
        dist2 = dist.copy()
        answer.append(check(weak2, dist2))
    
    answer = list(set(answer))
    answer.sort()
    if len(answer) == 1 : # 답이 하나밖에 없다면 반환
        return answer[0]
    else:  # 답이 여러개
        if answer[0] == -1 : # -1이 있다면 다음 답 반환
            return answer[1]
        else: return answer[0] # 없다면 최소 값 반환

def check(min_arr, dist):
    answer = 0
    for k in range(len(dist)):
        if not min_arr: return answer # 점검 완료 시 답 반환
        s = min_arr.pop()
        e = 0
        while min_arr:
            if s - min_arr[-1] <= dist[-1]: # dist의 최댓값을 넘지 않는 범위까지
                e = min_arr.pop()
            else:
                break
        if e == 0 and dist: # 두 지점 사이의 거리가 dist 최댓값을 넘는 경우
            del dist[0] # dist 가장 작은 값 사용
            answer += 1
        elif len(dist) == 0: # 모두 투입해도 전부 점검할 수 없는 경우
            return -1
        else: # 두 지점 사이의 거리 보다 크거나 같은 값 중 가장 작은 dist 값 사용
            i = bisect_left(dist, s - e) 
            if i != len(dist):
                del dist[i]
                answer += 1
    if not min_arr: return answer
    return -1 