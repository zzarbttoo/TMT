# 5주차 1번 여행 경로

def solution(tickets):
    route = []
    s = "ICN"
    tickets.sort()
    while len(tickets) > 1:
        for t in tickets:
            if t[0] == s: # s로 시작하는 경로
                for k in tickets:
                    if t[1] in k[0]:  # 그 후의 경로도 이어지는 게 있다면
                        tickets.remove(t)
                        route.append(s)
                        s = t[1]
                        break
    route += tickets[0]
    return route