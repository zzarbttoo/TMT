from collections import deque as dq

def solution(num, target):
    answer = 0
    stack=dq([(0,0)])
    temp=0
    ind=0
    while stack :
        temp,ind = stack.popleft()
        if ind ==len(num) and temp==target :
                answer+=1
        elif ind !=len(num) :
            number=num[ind]
            stack.append((temp+number,ind+1))
            stack.append((temp-number,ind+1))

    return answer
