# 5주차 5번 N으로 표현

def solution(N, number):
    dp = [{N}]
    if N == number : return 1
    
    for k in range(2, 9):
        curr = {int(str(N) * k)}
        for i in range(int(k / 2)):
            for x in dp[i]:
                for y in dp[k - i - 2]:
                    curr.update([x + y, x - y, y - x, x * y, x // y, y // x])
                    if 0 in curr: curr.remove(0)
        if number in curr:
            return k
        dp.append(curr)
    return -1

