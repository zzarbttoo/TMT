# 3주차 1번 주식가격

def solution(prices):
    answer = []
    count = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]: # 가격이 떨어지지 않을 경우 
                count += 1
            else: # 가격이 떨어진 경우 
                count += 1
                break
        answer.append(count)
        count = 0
    return answer