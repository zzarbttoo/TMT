# 1주차 2번_H-Index
cit = [2, 2, 0, 0, 0]
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for citation in citations:
        if citation > answer:
            answer += 1
    return answer
print(solution(cit))