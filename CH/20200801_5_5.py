#5번 N으로 표현
from collections import deque as dq
def dfs(N, number) :
    N=str(N)
    stack=dq([(N,1)])   #스택 초기값
    global answer
    answer=0
    while True:
        cur, idx = stack.popleft()   #현재 문자열과 N의개수 저장
        if eval(cur) ==number :      #문자열 계산결과 ==number이면 리턴
            answer=idx
            break
        if cur.startswith('0') :     #0으로 시작하는 문자열은 0없애줌
            cur=str(int(cur))
        if not cur.endswith(')'):    #괄호로 끝나는 문자열은 N을 붙이지 않음
            stack.append((cur+N,idx+1))
        stack.append((cur+'+'+N,idx+1))
        stack.append(('('+cur+'+'+N+')',idx+1))
        stack.append((cur+'*'+N,idx+1))
        stack.append((cur+'-'+N,idx+1))
        stack.append(('('+cur+'-'+N+')',idx+1))
        stack.append((cur+'//'+N,idx+1)) 
        if idx==9:                  #idx==9가 되면 그냥 -1리턴
            answer=-1
            break
def solution(N, number):

    dfs(N,number)
            
    return answer
