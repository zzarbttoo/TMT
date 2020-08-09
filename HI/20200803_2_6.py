# 6주차 2번 큰 수 만들기
from collections import deque as dq

def solution(number, k):
    stack = dq(number[0])
    for n in number[1:]:
        while stack and stack[-1] < n and k > 0: # 들어있는 수가 뒤의 수보다 작은 경우
            k -= 1 # 제거
            stack.pop()
        stack.append(n)
    if k != 0 : # 숫자가 내림차순인 경우
	    return "".join(stack)[:-k]

    return "".join(stack)
    

