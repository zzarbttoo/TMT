def solution(citations):
    b=[]
    for i in range(len(citations)+1):                    #0부터 논문들의 수까지
        a=len(list(filter(lambda x: x >= i, citations))) #논문들중 i보다 큰것만 호출
        if a >= i:                                       #i보다 큰 논문의 수가 i보다 크면
            b.append(i)                                  #b에 추가
        i+=1
    answer = max(b)                                      #b중에 제일 큰 놈 소환
    return answer
