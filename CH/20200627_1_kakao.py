def solution(s):
    temp=[]
    stack=''
    answer=[]
    n=1
    i=1
    if len(s)==1:                           #예시가 하나면 예외처리
        answer.append(1)
    while n<=len(s)//2:                     #슬라이스 최대길이가 문자열의 절반이므로 최대값 설정
        raw=list(s)                         #예시를 리스트 형식으로 쪼개서 삽입
        temp=[]                             #임시 저장소
        while raw:                          #raw가 빌 때 까지
            temp.append("".join(raw[:n]))   #raw의 원소를 n개씩 슬라이싱 후 string형태로 묶어서 temp에 차례로 쌓기
            del raw[:n]                     #쌓은 원소들은 raw에서 삭제
        for k in range(len(temp)):          #temp의 길이만큼 반복
            if k==len(temp)-1:              #temp의 k가 마지막의 앞 원소이면 스택에 쌓기
                    if i==1:
                        stack+=temp[k]
                    else:
                        stack+=str(i)+temp[k]
                        i=1
                    break
            if temp[k]==temp[k+1]:          #temp의 k번째와 k+1번째를 비교
                i+=1                        #같으면 i+1
            else:
                if i==1:                    #다르면 스택에 쌓기 (i==1일때 i 생략)
                    stack+=temp[k]
                else:
                    stack+=str(i)+temp[k]
                    i=1
        answer.append(len(stack))           #스택의 길이를 answer에 저장
        stack=''                            #스택 초기화
        n+=1                                #슬라이싱 범위 1증가
    return min(answer)
