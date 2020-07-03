# 2주차 1번 전화번호 목록

def solution(phone_book):
    answer = True
    phone_list = sorted(phone_book, key = lambda x: len(x)) # 길이가 짧은 문자열 부터 오름차순 정렬
    k = 0
    while k < len(phone_list)-1: # k는 비교 기준이 되는 인덱스 값
        prev = phone_list[k]
        i = len(prev)
        for j in range(k+1, len(phone_list)): # k 다음 번호부터 k번째 값과 비교
            curr = phone_list[j] # curr: 비교 대상
            if prev == curr[:i]:
                answer = False
                return answer # False인 경우 바로 answer값 리턴
        k += 1
    return answer