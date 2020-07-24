from collections import deque as dq
def solution(arr):
    cnt=0
    answer=0
    stack=''
    arr=dq(arr)
    while arr:
        stack+=arr.popleft()
        if stack.endswith('()'):
            cnt-=1
            answer+=cnt
            continue
        elif stack[-1]=='(':
            cnt+=1
            continue
        elif stack[-1]==')':
            cnt-=1
            if stack[-2]==')':
                answer+=1
        if stack.count('(')==stack.count(')'):
            cnt=0
            stack=''
    return answer
