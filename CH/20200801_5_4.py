#4번 단어변환
from collections import deque as dq

def solution(begin, target, words):
    answer = []
    stack=dq([(begin,0)])       #스택의 초기값은 begin,0
    if target not in words:
        return 0
    while stack :
        temp, idx=stack.popleft()  #현재값을 temp와 idx에 저장 
        if temp==target :       
            answer.append(idx)
        else :
            for word in words :
                num=0
                for j in range(len(temp)) :  #temp와 words의 단어들과 비교
                    if word[j] != temp[j]:
                        num+=1
                if num==1 :                  #하나만 다르면 스택에 추가, words에서 제
                    stack.append((word,idx+1))
                    words.remove(word)
    if not answer :
        return 0
    return min(answer)

