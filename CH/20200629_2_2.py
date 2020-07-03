def solution(clothes):
    hash_stack={}
    hash_num={}
    temp=[]
    answer=1
    n=0
    hash_stack=dict(clothes)                        #dictionary 생성
    for k in range(len(clothes)):
        if hash_stack[clothes[k][0]] in temp:       #스택에 같은 옷이 있으면 continue
            continue
        temp.append(hash_stack[clothes[k][0]])      #스택에 옷 추가
        for j in range(len(clothes)):
            if hash_stack[clothes[j][0]] in temp:   #스택에 이미 같은 옷이 있으면  경우의 수+1
                n+=1
        hash_num[hash_stack[clothes[k][0]]]=n       #k번째 옷으로 만들 수 있는 경우의 수 n 스택
        n=0
        temp=[]
    for val in hash_num.values():                   #경우의 수 n값만 꺼내서 전체 경우의 수 계산
        answer*=(val+1)
    answer=answer-1
    return answer
