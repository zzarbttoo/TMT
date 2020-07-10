def solution(prices):
    answer = []
    for i in range(len(prices)) :
        if i==len(prices)-1:                   #마지막 하나가 남으면 0을 넣음
            answer.append(0)
            break
        for j in range(i+1,len(prices)) :
            if prices[i]>prices[j]:            #j가 i보다 작으지면 j-1을 넣음
                answer.append(j-i)
                break
            elif j+1==len(prices) :            #끝까지 안작아지면 j-1을 넣음
                answer.append(j-i)
    return answer
