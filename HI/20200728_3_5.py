# 5주차 3번 체육복

def solution(n, lost, reserve):
    answer = 0
    
    # 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우 다른 학생에게는 체육복을 빌려줄 수 없음
    cannot = set(lost) & set(reserve) # 여벌이 있지만 도난당한 경우
    lost = list(set(lost) - cannot) # lost - 교집합
    reserve = list(set(reserve) - cannot) # reserve - 교집합

    for res in reserve:
        if (res - 1) in lost:
            lost.remove(res - 1) # 빌릴 수 있다면 lost에서 제거
        elif (res + 1) in lost:
            lost.remove(res + 1)
    
    answer = n - len(lost)
    return answer

print(solution(5, [1, 2, 3, 4],  [2, 4, 5]))