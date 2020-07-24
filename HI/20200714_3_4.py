# 4주차 3번 소수 찾기

import itertools

def check(N): # 소수인지 확인
    if N == 0 or N == 1:
        return 0
    for i in range(2, int(N/2)+1): # 나누어 떨어지는 수가 있으면 소수가 아님
        if N % i == 0:
            return 0
    return 1 # 나누어 떨어지는 수가 없으면 소수

def solution(numbers):
    answer = 0
    num = list(numbers) # 문자열 리스트로 변형
    P = []
    for i in range(1,len(num)+1):
        P += list(map(''.join, itertools.permutations(num, i))) # 문자열의 순열 조합을 list에 이어붙임
    P = list(set(map(int,P))) # 중복되는 수 제거
    for p in P: # 소수의 개수 구하기
        answer += check(p)
    return answer