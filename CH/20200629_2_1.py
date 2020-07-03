def solution(phone_book):
    phone_book=sorted(phone_book)                     #전화번호 길이가 작은거 순으로 정렬
    answer=True                                       #기본값은 True
    for i in range(len(phone_book)-1):
        j=i+1
        while j<len(phone_book):
            if phone_book[i] in phone_book[j]:        #i번째 전화번호가 뒷쪽에 포함되는지 여부를 확인
                answer=False                          #포함되면 False, while문 탈출
                break
            j+=1
        if not answer:                                #answer가 False이면 종료
            break
    return answer
