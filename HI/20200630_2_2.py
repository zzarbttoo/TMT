# 2주차 2번 위장

def solution(clothes):
    answer = 0
    count = 1
    type_c = [] # 의상의 종류를 겹치지 않도록 저장
    type_w = [] # 각 의상별 의상의 종류를 저장한 list
    clothes_dic = {} # 딕셔너리
    
    clothes_dic.update(clothes) # 리스트를 딕셔너리로 저장

    for i in clothes_dic.values(): # 딕셔너리의 값(의상의 종류)
        type_w.append(i)
        if i not in type_c:
            type_c.append(i)

    for c in type_c: # 의상의 종류별 수로 경우의 수 계산
        count *= type_w.count(c)+1
    
    answer = count - 1 
    return answer
