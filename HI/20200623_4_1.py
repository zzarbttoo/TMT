# 1주자 4번_가장 큰 수

import itertools
numb = [3, 30, 34, 5, 9]

def solution(numbers):
    answer=''
    numb_list = list(map(str, numbers))
    numb_list = list(map(int,map(''.join, itertools.permutations(numb_list))))   #순열 함수
    answer = str(max(numb_list))   #순열 조합 중 가장 큰 수
    return answer
    
print(solution(numb))

""" 순열 함수 permutations으로 모든 조합을 만들어 그 중 가장 큰 값을 return 하도록 했는데,
sample test는 통과하였으나 가능한 모든 순열을 모두 만들어 비교하기 때문에 수행 시간 초과"""