def solution(p):
    u=''
    if len(p)==0:                       #빈 문자열이면 그대로 반환
        return p
    for i in p :                        #p에 있는거 그대로 u에 계속 넣어줌
        u=u+i
        if u.count('(')==u.count(')'):  #(의 개수와 )의 개수가 같아지면 그만
            break
    v=p[len(u):]                        #v = p에서u를 뺸 나머지
    if u[0]=='(' and u[-1]==')':        #u가 (로 시작해서 )로 끝나면(올바른)
        answer=u+solution(v)            #v를 solution함수에 넣고 결과를 u에 붙힘
        return answer
    else :                              #u가 '균형잡힌' 이면
        u=u[1:-1]                       #앞뒤를 짜름
        k=len(u)                        #u의 길이를 고정시키기위해 상수화
        for j in range(k):              #u의 요소를 뒤집어서 붙여준다.
            if u[j]=='(':
                u+=')'
            else:
                u+='('
        u=u[k:]                         #뒤집어진것만 선택해준다.
        answer='('+ solution(v)+')'+u   #v는 재귀처리하고 나머지 붙여준다.
    return answer
