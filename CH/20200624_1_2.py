def solution(citations):
    b=[]
    for i in range(len(citations)+1):
        a=len(list(filter(lambda x: x >= i, citations)))
        if a >= i:
            b.append(i)
        i+=1
    answer = max(b)
    return answer
