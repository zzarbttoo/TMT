# 3주차 2번 프린터

def solution(priorities, location):
    answer = 0
    out = -1
    index = [i for i in range(len(priorities))] # 인덱스 리스트
    while out != location: # out: 프린트 되는 문서 인덱스
        curr = priorities.pop(0)
        curr_index = index.pop(0)
        if priorities == []: # 마지막 순번일 때 인쇄 후 종료
            return answer + 1
        if curr >= max(priorities): # 중요도가 가장 높을 때 인쇄
            answer += 1
            out = curr_index
        else:
            priorities.append(curr) # 더 높은 게 있을 때 대기목록 마지막에 삽입
            index.append(curr_index)
    return answer
